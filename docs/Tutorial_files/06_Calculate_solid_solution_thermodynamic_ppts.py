# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 18:48:55 2021

@author: adedapo.awolayo
"""
import os, numpy as np
from pygcc.pygcc_utils import calcRxnlogK, outputfmt, db_reader


#%% specify the direct access thermodynamic database
dbaccess = '../database/speq21.dat'
dbaccessdic = db_reader(dbaccess = dbaccess).dbaccessdic


#%% Vectors for Temperature (K) and Pressure (bar) inputs
T = np.array([  0.00,   25.0000 ,  60.0000,  100.0000, 150.0000,  200.0000,  250.0000,  300.0000])
nCa = 1


#%% Examples of calculating Plagioclase mineral thermodynamics
folder_to_save = 'output'
if os.path.exists(os.path.join(os.getcwd(), folder_to_save)) == False:
    os.makedirs(os.path.join(os.getcwd(), folder_to_save))
filename = './output/logK_06.txt'
fid = open(filename, 'w')

logKRxn = calcRxnlogK(T = T, P = 'T', X = 0.634, Specie = 'Plagioclase', dbaccessdic = dbaccessdic,
                      densityextrap = True)
logK, Rxn = logKRxn.logK, logKRxn.Rxn


# output in EQ36 format
outputfmt(fid, logK, Rxn, dataset = 'EQ36')
# output in GWB format
outputfmt(fid, logK, Rxn, dataset = 'GWB')
# output in Pflotran format
outputfmt(fid, logK, Rxn, dataset = 'Pflotran')

fid.close()




