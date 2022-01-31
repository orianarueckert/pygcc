#!/usr/bin/env python
# coding: utf-8

# # General Usage

# #### Import pygcc

# In[1]:


#import pygcc
#print(pygcc.__version__)
from pygcc.pygcc_utils import *


# #### Read database by specifying the direct-access and source database

# In[2]:


ps = db_reader(sourcedb = './database/thermo.2021.dat', sourceformat = 'gwb')
# ps.dbaccessdic, ps.sourcedic,  ps.specielist


# ### Example: calculating water properties

# With IAPWS95

# In[3]:


water = iapws95(T = np.array([  0.01, 25, 60,  100, 150,  200,  250,  300]), P = 200)
print(water.rho)
print(water.G)
print(water.H)
print(water.S)


# With ZhangDuan

# In[4]:


water = ZhangDuan(T= np.array([1000, 1050]), P = np.array([1000, 2000]))
print(water.rho, water.G)


# ### Example: calculating water dielectric constants

# In[5]:


dielect = water_dielec(T= np.array([1000, 1050]), P = np.array([1000, 2000]), Dielec_method = 'DEW')
dielect.E, dielect.rhohat, dielect.Ah, dielect.Bh


# In[6]:


dielect = water_dielec(T= np.array([100, 150]), P = np.array([100, 200]), Dielec_method = 'JN91')
dielect.E, dielect.rhohat, dielect.Ah, dielect.Bh


# ### Example: calculation for olivine solid solutions

# In[7]:


calc = calcRxnlogK( X = 0.85,T = np.array([300, 400, 450]), P = np.array([200, 200, 200]),
                   Specie = 'olivine', dbaccessdic = ps.dbaccessdic, densityextrap = True)
calc.logK, calc.Rxn


# ### Example: create new reactions and calculate equilibrium constants

# In[8]:


# An example with PPM
ps.sourcedic['Pyrite'] = ['', 4, '4', 'H2S(aq)', '1', 'Magnetite',  '-2', 'Pyrrhotite', '-4', 'H2O']
Temp = np.array([300.0000, 325, 350.0000, 400.0000, 415, 425.0000, 435, 450.0000])
Press = 500*np.ones(np.size(Temp))
log_K_PPM = calcRxnlogK( T = Temp, P = Press, Specie = 'Pyrite', dbaccessdic = ps.dbaccessdic,
                        sourcedic = ps.sourcedic, specielist = ps.specielist).logK
log_K_PPM


# ### Example: Generate GWB thermodynamic database

# In[9]:


# Vectors for Temperature (K) and Pressure (bar) inputs
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

# In[14]:


get_ipython().run_cell_magic('time', '', "write_database(T = [0, 400], P = 300, cpx_Ca = 0.5, solid_solution = 'Yes', Dielec_method = 'FGL97',\n                dbaccess = './database/slop07.dat',\n                sourcedb = './database/thermo.29Sep15.dat', dataset = 'GWB')")


# write GWB using default sourced database and direct-access database (slop07 with Berman mineral data) and FGL97 dielectric constant

# In[15]:


get_ipython().run_cell_magic('time', '', "write_database(T = [0, 340], P = 150, Dielec_method = 'FGL97',  dbaccess = './database/slop07.dat',\n                dbBerman_dir = './database/Berman.dat', dataset = 'GWB',\n                mineral_eos = 'Berman88')")


# write GWB using user-specified sourced Pitzer database and default direct-access database along the saturation curve

# In[16]:


get_ipython().run_cell_magic('time', '', "write_database(T = [0, 350], P = 'T', dataset = 'GWB',  sourcedb = './database/thermo_hmw.tdat')")


# write GWB using user-specified sourced EQ3/6 Pitzer database and default direct-access database

# In[17]:


get_ipython().run_cell_magic('time', '', "write_database(T = [0, 350], P = 250, dataset = 'GWB', sourcedb = './database/data0.fmt',\n               sourceformat = 'EQ36')")


# ### Example: Generate EQ3/6 thermodynamic database

# write EQ3/6 using default sourced database

# In[18]:


get_ipython().run_cell_magic('time', '', "write_database(T = T, P = P, cpx_Ca = 1, solid_solution = 'Yes', clay_thermo = 'Yes', \n               dataset = 'EQ36')")


# write EQ3/6 user-specified sourced database

# In[19]:


get_ipython().run_cell_magic('time', '', "write_database(T = [0, 400], P = 350, cpx_Ca = 0.5, solid_solution = 'Yes', clay_thermo = 'Yes',\n                sourcedb = './database/data0.geo', dataset = 'EQ36')")


# write EQ3/6 using user-specified sourced Pitzer database

# In[20]:


get_ipython().run_cell_magic('time', '', "write_database(T = [0, 350], P = 200, sourcedb = './database/data0.hmw', dataset = 'EQ36')")


# write EQ3/6 user-specified sourced database using FGL97 dielectric constant

# In[21]:


get_ipython().run_cell_magic('time', '', "write_database(T = [0, 400], P = 300, cpx_Ca = 0.1, sourcedb = './database/data0.geo', \n               dataset = 'EQ36', solid_solution = 'Yes', Dielec_method = 'FGL97', clay_thermo = 'Yes')")


# write EQ3/6 user-specified sourced database using DEW model

# In[22]:


get_ipython().run_cell_magic('time', '', "Temp = np.array([50, 100, 150, 300, 450, 500, 600, 700])\nwrite_database(T = Temp, P = 1500, sourcedb = './database/data0.geo', dataset = 'EQ36', \n               Dielec_method = 'DEW')")


# ### Example: Generate ToughReact thermodynamic database

# write ToughReact using user-specified EQ3/6 database

# In[23]:


get_ipython().run_cell_magic('time', '', "write_database(T = T, P = P, cpx_Ca = nCa, solid_solution = 'Yes', sourcedb = './database/data0.dat',\n                dataset = 'ToughReact', sourceformat = 'EQ36')")


# write ToughReact using user-specified GWB database

# In[24]:


get_ipython().run_cell_magic('time', '', "write_database(T = [0, 350], P = 250, cpx_Ca = 0.25, clay_thermo = 'Yes', dataset = 'ToughReact',\n                sourcedb = './database/thermo.com.tdat', sourceformat = 'GWB')")


# write ToughReact using EQ3/6 user-specified Ptizer sourced database and JN91 dielectric constant

# In[25]:


get_ipython().run_cell_magic('time', '', "write_database(T = [0, 300], P = 200, sourceformat = 'EQ36', sourcedb = './database/data0.hmw',\n                dataset = 'ToughReact', Dielec_method = 'JN91')")


# ### Example: Generate Pflotran thermodynamic database

#  write Pflotran using user-specified EQ3/6 database

# In[26]:


get_ipython().run_cell_magic('time', '', "write_database(T = T, P = P, clay_thermo = 'Yes', sourcedb = './database/data0.dat',\n                dataset = 'Pflotran', sourceformat = 'EQ36')")


# write Pflotran using user-specified GWB database

# In[27]:


get_ipython().run_cell_magic('time', '', "write_database(T = [0, 350], P = 250, cpx_Ca = 0.1, solid_solution = True, clay_thermo = True,\n               sourcedb = './database/thermo.com.tdat', dataset = 'Pflotran', sourceformat = 'GWB')")


# ### Example: Calculate clay mineral thermodynamics

# In[28]:


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


# ### Example: Calculate Plagioclase solid-solution thermodynamics

# In[29]:


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

# In[30]:


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


# In[31]:


for i in range(len(T)):
    print('Fluid Temperature [C]: ', T[i])
    print('Fluid Pressure [bar]: ', P[i])
    print('Molality of CO2 in aqueous phase: ', mco2.ravel()[i])
    print('Activity of CO2 in aqueous phase (Duan_Sun): ', co2_activity.ravel()[i])
    print('Activity of CO2 in aqueous phase (Drummond): ', co2_activityD.ravel()[i])
    print('\n')


# In[32]:


#%% Calculate Water activity, osmotic coefficient and NaCl mean activity coefficient at an ionic strength of 0.5M
aw, phi, mean_act = Helgeson_activity(T, P, 0.5, Dielec_method = 'JN91')
for i in range(len(T)):
    print('Fluid Temperature [C]: ', T[i])
    print('Fluid Pressure [bar]: ', P[i])
    print('Water activity: ', aw.ravel()[i])
    print('Water osmotic coefficient: ', phi.ravel()[i])
    print('NaCl mean activity coefficient: ', mean_act.ravel()[i])
    print('\n')


# In[ ]:




