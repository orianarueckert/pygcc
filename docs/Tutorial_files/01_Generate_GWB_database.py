#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 18:48:55 2021

@author: adedapo.awolayo
"""
import numpy as np
from pygcc.pygcc_utils import write_database


# Vectors for Temperature (K) and Pressure (bar) inputs
T = np.array([  0.010,   25.0000 ,  60.0000,  100.0000, 120.0000,  150.0000,  250.0000,  300.0000])
P = 350*np.ones(np.size(T))
nCa = 1

#%% Examples of generating GWB thermodynamic database

# 1.  write GWB using default sourced database, with inclusion of solid_solution and clay thermo properties
write_database(T = T, P = P, cpx_Ca = nCa, solid_solution = 'Yes', clay_thermo = 'Yes', dataset = 'GWB')

# 2.  write GWB using user-specified sourced database, with inclusion of solid_solution and clay thermo properties
write_database(T = T, P = 175, cpx_Ca = nCa, solid_solution = 'Yes', clay_thermo = 'Yes',
                sourcedb = '../database/thermo.29Sep15.dat', dataset = 'GWB')

# 3.  write GWB using Jan2020 formatted sourced database
write_database(T = T, P = 125, cpx_Ca = nCa, solid_solution = True, clay_thermo = True,
                sourcedb = '../database/thermo.com.tdat', dataset = 'GWB')

# 4.  write GWB using Jan2020 formatted sourced database with logK as polynomial coefficients, using Tmax and Tmin
write_database(T = [0, 450], P = 200, cpx_Ca = nCa, solid_solution = 'Yes', clay_thermo = 'Yes',
                logK_form = 'polycoeffs', sourcedb =  '../database/thermo.com.tdat', dataset = 'GWB')

# 5. write GWB using user-specified sourced database and direct-access database (slop07) and FGL97 dielectric constant
write_database(T = [0, 600], P = 300, cpx_Ca = 0.5, solid_solution = 'Yes', Dielec_method = 'FGL97',
                dbaccess = '../database/slop07.dat',
                sourcedb = '../database/thermo.29Sep15.dat', dataset = 'GWB')

# 6. write GWB using default sourced database and direct-access database (slop07 with Berman mineral data) and FGL97 dielectric constant
write_database(T = [0, 340], P = 150, Dielec_method = 'FGL97',  dbaccess = '../database/slop07.dat',
                dbBerman_dir = '../database/berman.dat', dataset = 'GWB',
                mineral_eos = 'Berman88')

# 7. write GWB using user-specified sourced Pitzer database and default direct-access database along the saturation curve
write_database(T = [0, 350], P = 'T', dataset = 'GWB',  sourcedb = '../database/thermo_hmw.tdat')


# 8. write GWB using user-specified sourced EQ3/6 Pitzer database and default direct-access database
write_database(T = [0, 350], P = 250, dataset = 'GWB', sourcedb = '../database/data0.fmt',
               sourceformat = 'EQ36', sourcedb_codecs = 'latin-1')


