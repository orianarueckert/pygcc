# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 18:48:55 2021

@author: adedapo.awolayo
"""
import numpy as np
from pygcc.pygcc_utils import write_database


T = np.array([  0.010,   25.0000 ,  60.0000,  100.0000, 150.0000,  200.0000,  250.0000,  300.0000])
P = 250*np.ones(np.size(T))
nCa = 0.4


#%% Pflotran thermodynamic database
# 1. write Pflotran using user-specified EQ3/6 database
write_database(T = T, P = P, clay_thermo = 'Yes', sourcedb = '../database/data0.dat',
                dataset = 'Pflotran', sourceformat = 'EQ36')

# 2. write Pflotran using user-specified GWB database
write_database(T = [0, 500], P = 500, cpx_Ca = nCa, solid_solution = True, clay_thermo = True,
               sourcedb = '../database/thermo.com.tdat', dataset = 'Pflotran', sourceformat = 'GWB')


