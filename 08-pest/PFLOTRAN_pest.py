# PFLOTRAN Fitting Routine with PEST
# 1D column flow and transport model
# Authors: Katie Muller, Pin Shuai
# 04/13/25

# Import
import pandas as pd
from pathlib import Path
import numpy as np
import subprocess
import os
import matplotlib.pyplot as plt
import math as math

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

BTC_obs = pd.read_csv(f_obs_BTC)
time_BTC_obs = BTC_obs['Time [d]']

####### Path to folder locations
dir_model = Path('./')

### 2.0 Post-Process PFLOTRAN outputs to match experimental data format
# Simulation Results, BTC -- Aqueous concentration at the end of the column
f_out_btc = './pflotran-obs-0.pft'
pf_out_btc = read_pflotran_output(f_out_btc)

# BTC data obsevations:
observations = []
observations.append(BTC_obs['Total Tracer [M]'].tolist())
observations = np.concatenate(observations)

weights = []
wt = np.ones(len(BTC_obs['Total Tracer [M]']))
weights.append(wt.tolist())
weights = np.concatenate(weights)

## PFLOTRAN Model Output
model_output = []
# BTC sim output -- inter to exp data point time/locations
model_output.append(np.interp(BTC_obs['Time [d]'],pf_out_btc.index, pf_out_btc['Total Tracer [M] middle (50) (19.8 0.5 0.5)']).tolist())

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
# initial Marquardt lambda, adjustment factor for lambda, 
# PHIRATSUF: phi ratio sufficient--if the ratio of current and the lowest phi is less than this set ratio (i.e. 0.3) then iteration stops; 
# PHIREDLAM: relative reduction in phi is less than 0.03, then iteration stops
# NUMLAM: max number of lambdas for each iteration
  5.0   2.0   0.3  0.03    10
# RELPARMAX FACPARMAX FACORIG [IBOUNDSTICK UPVECBEND]
# RELPARMAX/FACPARMAX --max allowed relative/factor change for parameters, FACORIG is the factor used to times original parameter value to set the lower limit for parameters
  3.0   3.0 0.001  0
# PHIREDSWH [NOPTSWITCH]
  0.1
# NOPTMAX PHIREDSTP NPHISTP NPHINORED RELPARSTP NRELPAR
# NOPTMAX--set max number of interations; 0--stop after one model run (useful for testing PEST setup)
# PHIREDSTP--relative reduction in phi is less than 0.01 after NPHISTP (i.e., 3) iterations, then optimal parameters found.
# NPHINORED--after this number of iterations (3), PEST will stop when phi is not lowered
# RELPARSTP and NRELPAR -- stop if maximum relative parameter change between iterations is less than RELPARSTP over NRELPAR successive iterations
   30  0.01     3     3  0.01     3
# ICOV ICOR IEIG 
    1     1     1
* parameter groups
dgr         relative 0.01  0.0  switch  2.0 parabolic
* parameter data
# PARNME PARTRANS PARCHGLIM PARVAL1 PARLBND PARUBND PARGP SCALE OFFSET DERCOM
# parameter name, transformation (none, log,), change lmit, initial, lower bnd, upper bnd
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
