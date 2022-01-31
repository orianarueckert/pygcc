# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 17:54:19 2021

@author: adedapo.awolayo
"""

import os, sys, re, numpy as np
import pandas as pd
import xml.etree.ElementTree as ET
from lxml import etree

def read_gwboutput(fname):
    root = ET.parse(fname).getroot()
    doc = etree.parse(fname)
    colname_cp = []; colname_ms = []; colname_act = []; colname_comp = []; colname_conc = []
    param = ['Chemical parameters', 'Components in fluid', 'Mineral saturation', 
             'Species activity', 'Species concentration']
    prefix = ['', 'TotMolal_', 'SI_', 'Activity_', 'Molal_']
    colname = [ [] for _ in range(len(param)) ] 
    for elem in root:
        for subelem in elem:
            for i, k in enumerate(param):
                if subelem.get('type') in [k]:
                    for sub in subelem:
                        colname[i].append('%s%s' % (prefix[i], sub.get('name')) )
                        
    result = pd.DataFrame([])
    for i, k in enumerate(param):
        #if k == 'Chemical parameters':
        dframe = pd.DataFrame([])
        for Elem in doc.findall('TimeSlice/NodalBlock/Values'):
            if Elem.get('type') == k: # attribute
                lst = [float(i) for i in Elem.text.split()]        # element text
                dframe = pd.concat([dframe, pd.DataFrame(lst, index = colname[i]).T])
                dframe.reset_index(drop=True, inplace=True)
        result = pd.concat([result, dframe], axis=1)

    return result

	
def read_eq36output(fname):
    keywords = [['Distribution of Aqueous Solute Species',
                 'Species with molalities less than  1.000E-12 are not listed.'],
                ['Numerical Composition of the Aqueous Solution',
                 'Some of the above data may not be physically significant.'],
                ['Grand Summary of Solid Phases (ES + PRS + Reactants)',
                 'Mass, grams       Volume, cm3'],
                ['Saturation States of Pure Solids',
                 'Phases with affinities less than -10 kcal are not listed.']
                ]
    locator, prefix = [1, 2, 3, 1], ['M', 'TotM', 'MinMass', 'SI']
    dframe = pd.DataFrame()
    for num, k in enumerate(keywords):
        molality = []; counter = 0
        fid = open(fname, 'r')
        for i in range(500000) :
            s = fid.readline()
            if s.lstrip().rstrip('\n').strip(' --- ') == k[0]:
                counter += 1
                molality.append(s)
                for j in range(50):
                    s = fid.readline()
                    if s.lstrip().rstrip('\n') == k[1]:
                        break
                    elif not s.lstrip().startswith(('Species', 'Phase')) | (s.rstrip('\n') == ""):
                        molality.append(s)

        colname = list(np.unique(['%s_%s' % (prefix[num], x.split()[0]) for x in molality
                            if not x.lstrip().startswith('--')]))
        df = pd.DataFrame(np.zeros([counter, len(colname)]), columns=colname)

        steps = [ y for y, x in enumerate(molality) if x.lstrip().startswith('--')] + [len(molality)]
        for i in range(len(steps)):
            for j in colname:
                if i < len(steps)-1:
                    finder = [y for y in [ x if x.split()[0] == j[len(prefix[num])+1:] else 0
                                          for x in molality[steps[i]:steps[i+1]]] if y!=0 ]
                    df.loc[i, j] = float(finder[0].split()[locator[num]]) if len(finder)!=0 else 0

        dframe = pd.concat([dframe, df], axis=1)


    pH, Step, Temperature, Pressure, Water_mass, Rock_mass = [], [], [], [], [], []
    with open(fname, 'r') as fid:
            for i, line in enumerate(fid, 1):
                if re.compile(r"Xi").search(line) != None:
                    if line.lstrip().startswith('Xi='):
                        Step.append(float(line.split()[1]))
                if re.compile(r"B-dot pH scale").search(line) != None:
                    if line.lstrip().startswith('B-dot pH scale'):
                        pH.append(float(re.sub('[^0123456789\.  ]', '', line).split()[0]))
                if re.compile(r"Temperature=").search(line) != None:
                    if len(Step) != 0:
                        Temperature.append(float(line.split()[1]))
                if re.compile(r"Pressure=").search(line) != None:
                    if len(Step) != 0:
                        Pressure.append(float(line.split()[1]))
                if re.compile(r"Solvent mass=").search(line) != None:
                    if len(re.sub('[^0123456789\.  ]', '', line).lstrip()) > 7:
                        Water_mass.append(float(re.sub('[^0123456789\.  ]', '', line).split()[0]))
                if re.compile(r"Solutes  mass=").search(re.sub(r"[\(\[].*?[\)\]]", "", line)) != None:
                    if len(re.sub('[^0123456789\.  ]', '', line).lstrip()) > 7:
                        Rock_mass.append(float(re.sub('[^0123456789\.  ]', '', line).split()[0]))

    df = pd.DataFrame(np.column_stack([Step, pH, Temperature, Pressure, Water_mass, Rock_mass]),
                               columns=['Xi', 'pH', 'Temperature_C', 'Pressure_bars',
                                        'Water_mass_g', 'Rock_mass_g'])
    dframe = pd.concat([df, dframe], axis=1)

    return dframe


