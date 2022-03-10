#!/usr/bin/env python
# coding: utf-8

# # General Usage

# #### Import pygcc

# In[1]:


import pygcc
print(pygcc.__version__)
from pygcc.pygcc_utils import *


# #### Read database by specifying the direct- or sequential- access and source database

# ##### Using the default sequential-access database - speq21.dat

# In[3]:


ps = db_reader(sourcedb = './database/thermo.2021.dat', sourceformat = 'gwb')
# ps.dbaccessdic, ps.sourcedic,  ps.specielist


# ##### Using the user-specified sequential-access database

# In[4]:


ps = db_reader(dbaccess = './database/slop07.dat', sourcedb = './database/thermo.2021.dat', sourceformat = 'gwb')
# ps.dbaccessdic, ps.sourcedic,  ps.specielist


# ### Example: Calculate water properties

# *With IAPWS95*

# In[26]:


water = iapws95(T = np.array([  0.01, 25, 60,  100, 150,  200,  250,  300]), P = 200)
print(water.rho)
print(water.G)
print(water.H)
print(water.S)


# *With ZhangDuan*

# In[27]:


water = ZhangDuan(T= np.array([1000, 1050]), P = np.array([1000, 2000]))
print(water.rho, water.G)


# ### Example: Calculate water dielectric constants

# In[28]:


dielect = water_dielec(T= np.array([1000, 1050]), P = np.array([1000, 2000]), Dielec_method = 'DEW')
dielect.E, dielect.rhohat, dielect.Ah, dielect.Bh


# In[29]:


dielect = water_dielec(T= np.array([100, 150]), P = np.array([100, 200]), Dielec_method = 'JN91')
dielect.E, dielect.rhohat, dielect.Ah, dielect.Bh


# ### Example: Calculate olivine solid solutions

# In[30]:


calc = calcRxnlogK( X = 0.85,T = np.array([300, 400, 450]), P = np.array([200, 200, 200]),
                   Specie = 'olivine', dbaccessdic = ps.dbaccessdic, densityextrap = True)
calc.logK, calc.Rxn


# ### Example: Create new reactions and calculate equilibrium constants

# #### An example with pyrite, pyrrhotite, magnetite (PPM) reaction
# Pyrite + 4 H<sub>2</sub>O + 2 Pyrrhotite &rarr; 4 H<sub>2</sub>S<sub>(aq)</sub> + Magnetite
# 
# Then we can include the reaction in sourcedic, one of the output of db_reader, which is a dictionary of list of reaction coefficients and species. An example with the format for sourcedic is as follows:
# 
# > ps.sourcedic['Name'] = ['formula', number of reactants in the reaction, 'coefficient of specie 1', 'specie 1', 'coefficient of specie 2', 'specie 2']
# 
# > AB &rarr; 0.5 A<sub>2</sub><sub>(aq)</sub> + B
# 
# > ps.sourcedic['AB'] = ['AB', 2, '0.5', 'A2(aq), '1', 'B']

# In[31]:


ps.sourcedic['Pyrite'] = ['', 4, '4', 'H2S(aq)', '1', 'Magnetite',  '-2', 'Pyrrhotite', '-4', 'H2O']
Temp = np.array([300.0000, 325, 350.0000, 400.0000, 415, 425.0000, 435, 450.0000])
Press = 500*np.ones(np.size(Temp))
log_K_PPM = calcRxnlogK( T = Temp, P = Press, Specie = 'Pyrite', dbaccessdic = ps.dbaccessdic,
                        sourcedic = ps.sourcedic, specielist = ps.specielist).logK
log_K_PPM


# ### Example: Generate GWB thermodynamic database

# In[9]:


# Vectors for Temperature (C) and Pressure (bar) inputs
T = np.array([  0.010,   25.0000 ,  60.0000,  100.0000, 120.0000,  150.0000,  250.0000,  300.0000])
P = 350*np.ones(np.size(T))
nCa = 1


# write GWB using default sourced database, with inclusion of solid_solution and clay thermo properties

# In[10]:


get_ipython().run_cell_magic('time', '', "write_database(T = T, P = P, cpx_Ca = nCa, solid_solution = 'Yes',  clay_thermo = 'Yes', \n               dataset = 'GWB')")


# write GWB using user-specified sourced database, with inclusion of solid_solution and clay thermo properties

# In[11]:


get_ipython().run_cell_magic('time', '', "write_database(T = T, P = 175, cpx_Ca = nCa, solid_solution = 'Yes', clay_thermo = 'Yes',\n                sourcedb = './database/thermo.29Sep15.dat', dataset = 'GWB')")


# write GWB using Jan2020 formatted sourced database

# In[12]:


get_ipython().run_cell_magic('time', '', "write_database(T = T, P = 125, cpx_Ca = nCa, solid_solution = True, clay_thermo = True,\n                sourcedb = './database/thermo.com.tdat', dataset = 'GWB')")


# write GWB using Jan2020 formatted sourced database with logK as polynomial coefficients, using Tmax and Tmin

# In[13]:


get_ipython().run_cell_magic('time', '', "#write_database(T = [0, 450], P = 200, cpx_Ca = nCa, solid_solution = 'Yes', clay_thermo = 'Yes',\n#                logK_form = 'polycoeffs', sourcedb =  './database/thermo.com.tdat', dataset = 'GWB')")


# write GWB using user-specified sourced database and direct-access database (slop07) and FGL97 dielectric constant

# In[3]:


get_ipython().run_cell_magic('time', '', "write_database(T = [0, 400], P = 300, cpx_Ca = 0.5, solid_solution = 'Yes', Dielec_method = 'FGL97',\n                dbaccess = './database/slop07.dat',\n                sourcedb = './database/thermo.29Sep15.dat', dataset = 'GWB')")


# write GWB using default sourced database and direct-access database (slop07 with Berman mineral data) and FGL97 dielectric constant

# In[17]:


get_ipython().run_cell_magic('time', '', "write_database(T = [0, 340], P = 150, Dielec_method = 'FGL97',  dbaccess = './database/slop07.dat',\n                dbBerman_dir = './database/berman.dat', dataset = 'GWB',\n                mineral_eos = 'Berman88')")


# write GWB using user-specified sourced Pitzer database and default direct-access database along the saturation curve

# In[16]:


get_ipython().run_cell_magic('time', '', "write_database(T = [0, 350], P = 'T', dataset = 'GWB',  sourcedb = './database/thermo_hmw.tdat')")


# write GWB using user-specified sourced EQ3/6 Pitzer database and default direct-access database

# In[38]:


get_ipython().run_cell_magic('time', '', "write_database(T = [0, 350], P = 250, dataset = 'GWB', sourcedb = './database/data0.hmw',\n               sourceformat = 'EQ36')")


# ### Example: Generate EQ3/6 thermodynamic database

# write EQ3/6 using default sourced database

# In[18]:


get_ipython().run_cell_magic('time', '', "write_database(T = T, P = P, cpx_Ca = 1, solid_solution = 'Yes', clay_thermo = 'Yes', \n               dataset = 'EQ36')")


# write EQ3/6 user-specified sourced database

# In[37]:


get_ipython().run_cell_magic('time', '', "write_database(T = [0, 400], P = 350, cpx_Ca = 0.5, solid_solution = 'Yes', clay_thermo = 'Yes',\n                sourcedb = './database/data0.geo', dataset = 'EQ36', sourcedb_codecs = 'latin-1')")


# write EQ3/6 using user-specified sourced Pitzer database

# In[20]:


get_ipython().run_cell_magic('time', '', "write_database(T = [0, 350], P = 200, sourcedb = './database/data0.hmw', dataset = 'EQ36')")


# write EQ3/6 user-specified sourced database using FGL97 dielectric constant

# In[9]:


get_ipython().run_cell_magic('time', '', "write_database(T = [0, 400], P = 300, cpx_Ca = 0.1, sourcedb = './database/data0.geo', \n               dataset = 'EQ36', solid_solution = 'Yes', Dielec_method = 'FGL97', clay_thermo = 'Yes')")


# write EQ3/6 user-specified sourced database using DEW model

# In[29]:


get_ipython().run_cell_magic('time', '', "Temp = np.array([50, 100, 150, 300, 450, 500, 600, 700])\nwrite_database(T = Temp, P = 1500, sourcedb = './database/data0.geo', dataset = 'EQ36', \n               Dielec_method = 'DEW')")


# ### Example: Generate ToughReact thermodynamic database

# write ToughReact using user-specified EQ3/6 database

# In[24]:


get_ipython().run_cell_magic('time', '', "write_database(T = T, P = P, cpx_Ca = nCa, solid_solution = 'Yes', sourcedb = './database/data0.dat',\n                dataset = 'ToughReact', sourceformat = 'EQ36')")


# write ToughReact using user-specified GWB database

# In[15]:


get_ipython().run_cell_magic('time', '', "write_database(T = [0, 350], P = 250, cpx_Ca = 0.25, clay_thermo = 'Yes', dataset = 'ToughReact',\n                sourcedb = './database/thermo.com.tdat', sourceformat = 'GWB')")


# write ToughReact using EQ3/6 user-specified Ptizer sourced database and JN91 dielectric constant

# In[11]:


get_ipython().run_cell_magic('time', '', "write_database(T = [0, 300], P = 200, sourceformat = 'EQ36', sourcedb = './database/data0.hmw',\n                dataset = 'ToughReact', Dielec_method = 'JN91')")


# ### Example: Generate Pflotran thermodynamic database

#  write Pflotran using user-specified EQ3/6 database

# In[30]:


get_ipython().run_cell_magic('time', '', "write_database(T = T, P = P, clay_thermo = 'Yes', sourcedb = './database/data0.dat',\n                dataset = 'Pflotran', sourceformat = 'EQ36')")


# write Pflotran using user-specified GWB database

# In[13]:


get_ipython().run_cell_magic('time', '', "write_database(T = [0, 350], P = 250, cpx_Ca = 0.1, solid_solution = True, clay_thermo = True,\n               sourcedb = './database/thermo.com.tdat', dataset = 'Pflotran', sourceformat = 'GWB')")


# ### Example: Calculate clay mineral thermodynamics

# In[32]:


#%% specify the direct access thermodynamic database
db_dic = db_reader(dbaccess = './database/speq21.dat').dbaccessdic

folder_to_save = 'output'
if os.path.exists(os.path.join(os.getcwd(), folder_to_save)) == False:
    os.makedirs(os.path.join(os.getcwd(), folder_to_save)) 
fid = open('./output/logK_05.txt', 'w')

logKRxn = calcRxnlogK(T = T, P = P, Specie = 'Clay', dbaccessdic = db_dic,
                        elem = ['Clinochlore', '3', '2', '0', '0', '5', '0', '0', '0', '0'],
                        densityextrap = True,  group = '14A')
logK, Rxn = logKRxn.logK, logKRxn.Rxn

# output in EQ36 format
outputfmt(fid, logK, Rxn, dataset = 'EQ36')
# output in GWB format
outputfmt(fid, logK, Rxn, dataset = 'GWB')
# output in Pflotran format
outputfmt(fid, logK, Rxn, dataset = 'Pflotran')
# output in ToughReact format
outputfmt(fid, logK, Rxn, dataset = 'ToughReact')
fid.close()


# ### Example: Calculate plagioclase solid-solution thermodynamics

# In[33]:


#%% specify the direct access thermodynamic database
db_dic = db_reader(dbaccess = './database/speq21.dat').dbaccessdic

folder_to_save = 'output'
if os.path.exists(os.path.join(os.getcwd(), folder_to_save)) == False:
    os.makedirs(os.path.join(os.getcwd(), folder_to_save)) 
fid = open('./output/logK_05.txt', 'w')

logKRxn = calcRxnlogK(T = T, dbaccessdic = db_dic, P = 'T', X = 0.634, Specie = 'Plagioclase',
                        densityextrap = True)
logK, Rxn = logKRxn.logK, logKRxn.Rxn

# output in EQ36 format
outputfmt(fid, logK, Rxn, dataset = 'EQ36')
# output in GWB format
outputfmt(fid, logK, Rxn, dataset = 'GWB')
# output in Pflotran format
outputfmt(fid, logK, Rxn, dataset = 'Pflotran')
# output in ToughReact format
outputfmt(fid, logK, Rxn, dataset = 'ToughReact')
fid.close()


# ### Example: Calculate CO$_2$ activity and molality

# In[34]:


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


# In[35]:


for i in range(len(T)):
    print('Fluid Temperature [C]: ', T[i])
    print('Fluid Pressure [bar]: ', P[i])
    print('Molality of CO2 in aqueous phase: ', mco2.ravel()[i])
    print('Activity of CO2 in aqueous phase (Duan_Sun): ', co2_activity.ravel()[i])
    print('Activity of CO2 in aqueous phase (Drummond): ', co2_activityD.ravel()[i])
    print('\n')


# ### Example: Calculate water activity

# In[36]:


#%% Calculate Water activity, osmotic coefficient and NaCl mean activity coefficient at an ionic strength of 0.5M
aw, phi, mean_act = Helgeson_activity(T, P, 0.5, Dielec_method = 'JN91')
for i in range(len(T)):
    print('Fluid Temperature [C]: ', T[i])
    print('Fluid Pressure [bar]: ', P[i])
    print('Water activity: ', aw.ravel()[i])
    print('Water osmotic coefficient: ', phi.ravel()[i])
    print('NaCl mean activity coefficient: ', mean_act.ravel()[i])
    print('\n')

