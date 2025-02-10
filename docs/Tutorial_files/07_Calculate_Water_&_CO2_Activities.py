# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 18:48:55 2021

@author: adedapo.awolayo
"""
import numpy as np
from pygcc.pygcc_utils import Henry_duan_sun, drummondgamma, Helgeson_activity, convert_temperature


T = np.array([  0.010,   25 ,  60,  100, 150,  175,  200,  250])
P = 250*np.ones(np.size(T))

TK = convert_temperature(T, Out_Unit = 'K')

#%% Calculate CO2 activity and molality at ionic strength of 0.5M
# with Duan_Sun
log10_co2_gamma, mco2 = Henry_duan_sun(TK, P, 0.5)
co2_activity = 10**log10_co2_gamma

# with Drummond
log10_co2_gamma = drummondgamma(TK, 0.5)
co2_activityD = 10**log10_co2_gamma

for i in range(len(T)):
    print('Fluid Temperature [C]: ', T[i])
    print('Fluid Pressure [bar]: ', P[i])
    print('Molality of CO2 in aqueous phase: ', mco2.ravel()[i])
    print('Activity of CO2 in aqueous phase (Duan_Sun): ', co2_activity.ravel()[i])
    print('Activity of CO2 in aqueous phase (Drummond): ', co2_activityD.ravel()[i])
    print('\n')

#%% Calculate Water activity, osmotic coefficient and NaCl mean activity coefficient at an ionic strength of 0.5M
aw, phi, mean_act = Helgeson_activity(T, P, 0.5, Dielec_method = 'JN91')
for i in range(len(T)):
    print('Fluid Temperature [C]: ', T[i])
    print('Fluid Pressure [bar]: ', P[i])
    print('Water activity: ', aw.ravel()[i])
    print('Water osmotic coefficient: ', phi.ravel()[i])
    print('NaCl mean activity coefficient: ', mean_act.ravel()[i])
    print('\n')


