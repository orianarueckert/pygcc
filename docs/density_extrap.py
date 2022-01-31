# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 09:37:41 2022

@author: adedapo.awolayo
"""

import numpy as np, pandas as pd
from pygcc.pygcc_utils import iapws95, calcRxnlogK, db_reader
import matplotlib.pyplot as plt

TC = 400 #need to be above steam saturation limits to get this to make sense

rhoextrap=np.linspace(350,600,10)

Textrap = TC*np.ones(np.size(rhoextrap))
Pextrap = iapws95(T = Textrap, rho = rhoextrap).P
dframe = pd.DataFrame([Textrap, Textrap + 273.15, rhoextrap, Pextrap]).T
dframe.columns = ['TC', 'TK', 'rho', 'P']

water = iapws95( T = dframe.TC, P = dframe.P)
dframe['dG'] = water.G
dframe['rhohat'] = water.rho/1000 # kg/m3 -> g/cm3

db = db_reader(dbaccess = './database/speq21.dat', sourcedb = './database/thermo.com.tdat', sourceformat = 'GWB')

dframe['logK_NaCl'] = calcRxnlogK( T = dframe.TC, P = dframe.P, Specie = 'NaCl(aq)', dbaccessdic = db.dbaccessdic, 
                                  sourcedic = db.sourcedic, specielist = db.specielist).logK

dframe['logK_NaCl_Ho'] = -(0.997 - 650.07/dframe.TK - (10.420 - 2600.5/dframe.TK)*np.log10(dframe.rhohat))

def plot_densityextrap():
    rhoextrap = np.linspace(100,600,50)
    plt.figure()
    plt.plot( dframe.rho/1000, dframe.logK_NaCl,'mo') #, dframe.rho, dframe.logK_NaCl_Ho,'mv-.')
    plt.plot(rhoextrap/1000, np.polyval(np.polyfit(np.log10(dframe.rho), dframe.logK_NaCl, 1), 
                                        np.log10(rhoextrap)),'m-')
    plt.ylabel('log K [NaCl(aq)]')
    plt.xlabel('rho [g/cm3]')
    plt.legend([ 'HKF data' , 'density extrap'])
    plt.gca().tick_params(direction = 'in', which='both', top=True, right=True)



