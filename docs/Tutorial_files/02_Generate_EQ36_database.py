# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 18:48:55 2021

@author: adedapo.awolayo
"""

import numpy as np
from pygcc.pygcc_utils import write_database


# Vectors for Temperature (K) and Pressure (bar) inputs
T = np.array([  0.010,   25.0000 ,  60.0000,  100.0000, 150.0000,  200.0000,  250.0000,  300.0000])
P = 250*np.ones(np.size(T))


#%% Examples of generating EQ3/6 thermodynamic database
# 1. write EQ3/6 using default sourced database
write_database(T = T, P = P, cpx_Ca = 1, solid_solution = 'Yes', clay_thermo = 'Yes', dataset = 'EQ36')

# 2. write EQ3/6 user-specified sourced database
write_database(T = [0, 600], P = 350, cpx_Ca = 0.5, solid_solution = 'Yes', clay_thermo = 'Yes',
                sourcedb = '../database/data0.geo', dataset = 'EQ36', sourcedb_codecs = 'latin-1')

# 3. write EQ3/6 using user-specified sourced Pitzer database
write_database(T = [0, 350], P = 200, sourcedb = '../database/data0.hmw', dataset = 'EQ36')

# 4. write EQ3/6 user-specified sourced database using FGL97 dielectric constant
write_database(T = [0, 600], P = 300, cpx_Ca = 0.1, sourcedb = '../database/data0.geo', dataset = 'EQ36',
               solid_solution = 'Yes', Dielec_method = 'FGL97', clay_thermo = 'Yes', sourcedb_codecs = 'latin-1')

# 5. write EQ3/6 user-specified sourced database using DEW model
T = np.array([50, 100, 150, 300, 450, 500, 600, 700])
write_database(T = T, P = 1500, sourcedb = '../database/data0.geo', sourcedb_codecs = 'latin-1',
               dataset = 'EQ36', Dielec_method = 'DEW')

# 6. write EQ3/6 using user-specified sourced GWB database and default direct-access database
write_database(T = np.array([0.010, 25, 60, 100, 150, 200, 250, 300]), P = 250, dataset = 'EQ36', 
               sourcedb = 'thermo.2021', sourceformat = 'gwb', solid_solution = True, clay_thermo = True, 
               print_msg = True)
