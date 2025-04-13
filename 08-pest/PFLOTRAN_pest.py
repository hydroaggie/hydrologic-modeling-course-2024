# PFLOTRAN Fitting Routine with PEST
# Specific for Column 3- mZVI + XG
# Katie Muller
# 05/08/24

# Import
import pandas as pd
from pathlib import Path
import numpy as np
import subprocess
import os
import matplotlib.pyplot as plt
import math as math

# dir_code = '~/projects/DVZ_Particle/src'
# import sys
# sys.path.append(dir_code)

##### Functions to read PFLOTRAN pft and tec files ######
def read_pflotran_output(fname):
    '''Function for reading the pflotran output'''
    header = pd.read_csv(fname, nrows=0)
    data   = pd.read_csv(fname, sep='\s+', skiprows=1, names=list(header))
    data.index = data.iloc[:,0]
    return data
######################
def tec_to_dataframe(file_path, no_skiprow, column_headers):
    '''function to convert a tec PFLTORAN outfile to a dataframe'''
    df = pd.read_csv(file_path, skiprows=no_skiprow, delim_whitespace=True, header=None, names=column_headers)
    return df
#####################

### 1.0 Import Experimental Data
dir_data = Path('./')
f_obs_BTC = os.path.join(dir_data, 'observation.csv')
# f_obs_RP = os.path.join(dir_data, 'RP_Col3_mZVI_XG.xlsx')

BTC_obs = pd.read_csv(f_obs_BTC)
time_BTC_obs = BTC_obs['Time [d]']

# RP_obs = pd.read_excel(f_obs_RP)

####### Path to folder locations
dir_model = Path('./')

### 2.0 Post-Process PFLOTRAN outputs to match experimental data format
# Simulation Results, BTC -- Aqueous concentration at the end of the column
f_out_btc = './pflotran-obs-0.pft'
pf_out_btc = read_pflotran_output(f_out_btc)
# print(pf_out_btc.head())
# print(pf_out_btc.index)
## Simulation Results, Ret. Profile -- Retention Profile at final time
## FLAG - HARDCODED
#f_out_rp = os.path.join(dir_model, "{}".format('pflotran-010.tec'))

##### FLAG - Will need to make this flexible in the future #####
#column_headers = ['X [m]', 'Y [m]', 'Z [m]', 'Total Particle_aq [M]', 'Total Br- [M]', 'Particle_im [mol/m^3]','Material ID']

##Conversions
## FLAG - pb is HARDCODED
#pb = 1490 #kg/m^3
#MW_Fe = 55.845 #g/mol

# # Retention Profile
# pf_out_rp = tec_to_dataframe(f_out_rp, no_skiprow = 3, column_headers = column_headers)
# Vt_section = pf_out_rp['X [m]'].iloc[0]*2 * pf_out_rp['Y [m]'].iloc[0]*2 * pf_out_rp['Z [m]'].iloc[0]*2
# g_sand_section = Vt_section*pb*1000


# BTC data obsevations:
observations = []
observations.append(BTC_obs['Total Tracer [M]'].tolist())
# # RF data observations:
# observations.append(RP_obs['Solid Phase Iron Content [mg-Fe/g-sediment]'].tolist())
observations = np.concatenate(observations)

## 4.1 Computing weights
### Weights have been set based on the fraction of mass associated with the BTC vs RP and the number of data points for each data type, see below:
### 43% mass associated with BTC
### 57% mass associated with RF

weights = []
# wt = np.ones(len(BTC_obs['mZVI [M]']))*(43/len(BTC_obs['mZVI [M]']))
wt = np.ones(len(BTC_obs['Total Tracer [M]']))
weights.append(wt.tolist())
# wt = np.ones(len(RP_obs['Solid Phase Iron Content [mg-Fe/g-sediment]']))*(57/len(RP_obs['Solid Phase Iron Content [mg-Fe/g-sediment]']))
# weights.append(wt.tolist())
weights = np.concatenate(weights)

## PFLOTRAN Model Output
model_output = []
# BTC sim output -- inter to exp data point time/locations
model_output.append(np.interp(BTC_obs['Time [d]'],pf_out_btc.index, pf_out_btc['Total Tracer [M] middle (50) (19.8 0.5 0.5)']).tolist())

# # RP sim output -- inter to exp data point time/locations
# model_output.append(np.interp(RP_obs['distance from inlet [m]'],pf_out_rp['X [m]'],pf_out_rp['Particle_im [mol/m^3]']*MW_Fe*1000*Vt_section/g_sand_section).tolist())
model_output = np.concatenate(model_output)

### 5.0 Write PEST Files ##############################
    ## 5.1 Processed Observation Data File (txt) #################
with open("processed_observations.txt","w") as txt_file:
    for concentration in observations:
        txt_file.write('%.20f' % concentration + '\n')
    
    ## 5.2 write PEST instruction file--trial.ins (txt) #####################
i=0
with open("trial.ins","w") as txt_file:
    txt_file.write('pif @' + '\n')
    for concentration in observations:
        i += 1
        txt_file.write('l1 [obs'+str(i) + ']1:22' + '\n')
    
    ## 5.3 write PEST control file (Old protocal)--trial.pst (txt) ################
    # see doc: https://help.pesthomepage.org/index.html?structure-of-pest-control-file.html
with open("trial.pst","w") as txt_file:
    block = """pcf
* control data
# RSTFLE PESTMODE
norestart  estimation
# Number of parameters, number of observations, number of parameter groups, number of prior information, number of observation groups
    1     """ + str(i) + """     1     0     1
# Number of pairs of input template files, number of model output reading instruction files, 
# NTPLFLE NINSFLE    PRECIS   DPOINT [NUMCOM JACFILE MESSFILE] [OBSREREF]
    1     1 single point   1   0   0
# RLAMBDA1 RLAMFAC PHIRATSUF PHIREDLAM NUMLAM 
  5.0   2.0   0.3  0.03    10
# RELPARMAX FACPARMAX FACORIG [IBOUNDSTICK UPVECBEND]
  3.0   3.0 0.001  0
# PHIREDSWH [NOPTSWITCH]
  0.1
# NOPTMAX PHIREDSTP NPHISTP NPHINORED RELPARSTP NRELPAR
   30  0.01     3     3  0.01     3
# ICOV ICOR IEIG 
    1     1     1
* parameter groups
dgr         relative 0.01  0.0  switch  2.0 parabolic
* parameter data
# PARNME PARTRANS PARCHGLIM PARVAL1 PARLBND PARUBND PARGP SCALE OFFSET DERCOM
aL          none  relative    1      0.1   10 dgr             1.0000        0.0000      1
* observation groups
obsgroup
* observation data
# Obs Name  Observation        Weight    Group
"""
    i = 0
    txt_file.write(block)
    for concentration in observations:
        i += 1
        txt_file.write('obs'+str(i) + '   %.20f' % concentration + '    '+ str(weights[i-1]) +'    obsgroup' + '\n')
    block = """* model command line
./trial.sh
* model input/output
pflotran.tpl  pflotran.in
trial.ins output_processed.txt
* prior information"""
    txt_file.write(block)    
    ## 5.4 processed output (txt)

with open("output_processed.txt", "w") as txt_file:
    for model_sim in model_output:
        txt_file.write('   %.20f' % model_sim + '\n')   
