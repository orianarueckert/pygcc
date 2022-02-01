# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 18:48:55 2021

@author: adedapo.awolayo
"""
import numpy as np
from pygcc.pygcc_utils import write_database

#%% Vectors for Temperature (K) and Pressure (bar) inputs
T = np.array([  0.010,   25.0000 ,  60.0000,  100.0000, 150.0000,  200.0000,  250.0000,  300.0000])
P = 200*np.ones(np.size(T))
nCa = 0.1


#%% Examples of generating ToughReact thermodynamic database
# 1. write ToughReact using user-specified EQ3/6 database
write_database(T = T, P = P, cpx_Ca = nCa, solid_solution = 'Yes', sourcedb = '../database/data0.dat',
                dataset = 'ToughReact', sourceformat = 'EQ36')

# 2. write ToughReact using user-specified GWB database
write_database(T = [0, 500], P = 250, cpx_Ca = 0.25, clay_thermo = 'Yes', dataset = 'ToughReact',
                sourcedb = '../database/thermo.com.tdat', sourceformat = 'GWB')

# 3. write EQ3/6 user-specified Ptizer sourced database and JN91 dielectric constant
write_database(T = [0, 600], P = 300, sourceformat = 'EQ36', sourcedb = '../database/data0.hmw',
                dataset = 'ToughReact', Dielec_method = 'JN91')

