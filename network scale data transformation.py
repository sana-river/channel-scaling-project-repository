# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 11:50:54 2021

@author: sanakhan
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
%matplotlib auto

#import dataset as dataframe
df=pd.read_excel((r"C:\UCD scaling work\network scale prediction.xlsx"),sheet_name='data+scalar')


#AREA
Ac=df['AREA']
log_scalar_Ac=np.log10(Ac)
fitted_Ac, fitted_lambda_Ac = stats.boxcox(Ac)

#SLOPE
SLOPE=df['SLOPE']
log_scalar_SLOPE=np.log10(SLOPE)
fitted_SLOPE, fitted_lambda_SLOPE = stats.boxcox(SLOPE)

#CONFINEMEN
CONFINEMEN=df['CONFINEMEN']
log_scalar_CONFINEMEN=np.log10(CONFINEMEN)
fitted_CONFINEMEN, fitted_lambda_CONFINEMEN = stats.boxcox(CONFINEMEN)

#RUSLE
RUSLE=df['RUSLE']
log_scalar_RUSLE=np.log10(RUSLE)
fitted_RUSLE, fitted_lambda_RUSLE = stats.boxcox(RUSLE)

# creating axes to draw plots
fig, ax = plt.subplots(4, 3)
  
#plus_AREA- non-normal, log and box-cox
sns.distplot(Ac, hist = True, kde = True, kde_kws = {'shade': True, 'linewidth': 2}, label = "Non-Normal", color ="grey", ax = ax[0,0])
sns.distplot(log_scalar_Ac, hist = True, kde = True,  kde_kws = {'shade': True, 'linewidth': 2}, label = "log", color ="red", ax = ax[0,1])
sns.distplot(fitted_Ac, hist = True, kde = True,  kde_kws = {'shade': True, 'linewidth': 2}, label = "Box-cox", color ="blue", ax = ax[0,2])
  
#SLOPE- non-normal, log and box-cox
sns.distplot(SLOPE, hist = True, kde = True, kde_kws = {'shade': True, 'linewidth': 2}, label = "Non-Normal", color ="grey", ax = ax[1,0])
sns.distplot(log_scalar_SLOPE, hist = True, kde = True,  kde_kws = {'shade': True, 'linewidth': 2}, label = "log", color ="red", ax = ax[1,1])
sns.distplot(fitted_SLOPE, hist = True, kde = True,  kde_kws = {'shade': True, 'linewidth': 2}, label = "Box-cox", color ="blue", ax = ax[1,2])
  
#plus_CONFINEMEN- non-normal, log and box-cox
sns.distplot(CONFINEMEN, hist = True, kde = True, kde_kws = {'shade': True, 'linewidth': 2}, label = "Non-Normal", color ="grey", ax = ax[2,0])
sns.distplot(log_scalar_CONFINEMEN, hist = True, kde = True,  kde_kws = {'shade': True, 'linewidth': 2}, label = "log", color ="red", ax = ax[2,1])
sns.distplot(fitted_CONFINEMEN, hist = True, kde = True,  kde_kws = {'shade': True, 'linewidth': 2}, label = "Box-cox", color ="blue", ax = ax[2,2])
 
#plus_RUSLE- non-normal, log and box-cox
sns.distplot(RUSLE, hist = True, kde = True, kde_kws = {'shade': True, 'linewidth': 2}, label = "Non-Normal", color ="grey", ax = ax[3,0])
sns.distplot(log_scalar_RUSLE, hist = True, kde = True,  kde_kws = {'shade': True, 'linewidth': 2}, label = "log", color ="red", ax = ax[3,1])
sns.distplot(fitted_RUSLE, hist = True, kde = True,  kde_kws = {'shade': True, 'linewidth': 2}, label = "Box-cox", color ="blue", ax = ax[3,2])
  


# adding legends to the subplots
#plt.legend(loc = "upper right")
  
# rescaling the subplots
fig.set_figheight(5)
fig.set_figwidth(10)
  
#print(f"Lambda value used for Transformation: {fitted_lambdaAc}")

fig.set(ylabel=None)