# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 08:35:27 2022

@author: adedapo.awolayo
"""

import numpy as np
from pygcc.pygcc_utils import water_dielec, calcRxnlogK, db_reader, iapws95, ZhangDuan

# %% Various functions within pygcc

# read database - direct-access and source
ps = db_reader(sourcedb = '../database/thermo.2021.dat',
               sourceformat = 'gwb', dbaccess = '../database/speq21.dat')
ps.dbaccessdic, ps.sourcedic,  ps.specielist

# water equation of states
water = iapws95(T = np.array([  0.01, 25, 60,  100, 150,  200,  250,  300]),
                P = 200)
print(water.rho, water.G, water.H, water.S)

water = ZhangDuan(T= np.array([1000, 1050]), P = np.array([1000, 2000]))
print(water.rho, water.G)

# Water dielectric constants
dielect = water_dielec(T= np.array([1000, 1050]), P = np.array([1000, 2000]), Dielec_method = 'DEW')
dielect.E, dielect.rhohat, dielect.Ah, dielect.Bh

# LogK and Rxn calculation for solid solutions
calc = calcRxnlogK( X = 0.85,T = np.array([300, 400, 450]), P = np.array([200, 200, 200]),
                   Specie = 'olivine', dbaccessdic = ps.dbaccessdic, densityextrap = True)
calc.logK, calc.Rxn

# add new reactions and calculate logK
ps.sourcedic['Pyrite'] = ['', 4, '4', 'H2S(aq)', '1', 'Magnetite',  '-2', 'Pyrrhotite', '-4', 'H2O']
Temp = np.array([300.0000, 325, 350.0000, 400.0000, 415, 425.0000, 435, 450.0000])
Press = 500*np.ones(np.size(Temp))
log_K_PPM = calcRxnlogK( T = Temp, P = Press, Specie = 'Pyrite', dbaccessdic = ps.dbaccessdic,
                        sourcedic = ps.sourcedic, specielist = ps.specielist).logK
