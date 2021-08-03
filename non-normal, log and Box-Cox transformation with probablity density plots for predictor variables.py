# -*- coding: utf-8 -*-
"""
Created on Wed May 12 16:31:25 2021

@author: 45026556
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

#import dataset as dataframe
df=pd.read_excel((r"C:\UCD scaling work\SFE transformed data.xlsx"),sheet_name='original+scalar')


#width
w=df['w']
log_scalar_w=np.log10(w)
fitted_w, fitted_lambda_w = stats.boxcox(w)

#depth
d=df['d']
log_scalar_d=np.log10(d)
fitted_d, fitted_lambda_d = stats.boxcox(d)

#w*d
wd=df['w*d']
log_scalar_wd=np.log10(wd)
fitted_wd, fitted_lambda_wd = stats.boxcox(wd)

#w/d
wbyd=df['w/d']
log_scalar_wbyd=np.log10(wbyd)
fitted_wbyd, fitted_lambda_wbyd = stats.boxcox(wbyd)

#CV_w
CV_w=df['width Cv.']
log_scalar_CV_w=np.log10(CV_w)
fitted_CV_w, fitted_lambda_CV_w = stats.boxcox(CV_w)

#CV_d
CV_d=df['depth Cv.']
log_scalar_CV_d=np.log10(CV_d)
fitted_CV_d, fitted_lambda_CV_d = stats.boxcox(CV_d)

#Std_w
Std_w=df['width Std. deviation']
log_scalar_Std_w=np.log10(Std_w)
fitted_Std_w, fitted_lambda_Std_w = stats.boxcox(Std_w)

#Std_d
Std_d=df['depth Std. deviation']
log_scalar_Std_d=np.log10(Std_d)
fitted_Std_d, fitted_lambda_Std_d = stats.boxcox(Std_d)

#D50
D50=df['D50']
log_scalar_D50=np.log10(D50)
fitted_D50, fitted_lambda_D50 = stats.boxcox(D50)

#D84
D84=df['D84']
log_scalar_D84=np.log10(D84)
fitted_D84, fitted_lambda_D84 = stats.boxcox(D84)

#SLOPE
SLOPE=df['slope']
log_scalar_SLOPE=np.log10(SLOPE)
fitted_SLOPE, fitted_lambda_SLOPE = stats.boxcox(SLOPE)

#Ac
Ac=df['contributing catchment area']
log_scalar_Ac=np.log10(Ac)
fitted_Ac, fitted_lambda_Ac = stats.boxcox(Ac)

#CONFINEMEN
CONFINEMEN=df['confinement']
log_scalar_CONFINEMEN=np.log10(CONFINEMEN)
fitted_CONFINEMEN, fitted_lambda_CONFINEMEN = stats.boxcox(CONFINEMEN)

#RUSLE
RUSLE=df['RUSLE']
log_scalar_RUSLE=np.log10(RUSLE)
fitted_RUSLE, fitted_lambda_RUSLE = stats.boxcox(RUSLE)

#slope_mean_rstr
slope_mean_rstr=df['valley slope']
log_scalar_slope_mean_rstr=np.log10(slope_mean_rstr)
fitted_slope_mean_rstr, fitted_lambda_slope_mean_rstr = stats.boxcox(slope_mean_rstr)

# creating axes to draw plots
fig, ax = plt.subplots(4, 3)
  
#plus_d- non-normal, log and box-cox
sns.distplot(Ac, hist = True, kde = True, kde_kws = {'shade': True, 'linewidth': 2}, label = "Non-Normal", color ="grey", ax = ax[0,0])
sns.distplot(log_scalar_Ac, hist = True, kde = True,  kde_kws = {'shade': True, 'linewidth': 2}, label = "log", color ="red", ax = ax[0,1])
sns.distplot(fitted_Ac, hist = True, kde = True,  kde_kws = {'shade': True, 'linewidth': 2}, label = "Box-cox", color ="blue", ax = ax[0,2])
  
#w- non-normal, log and box-cox
sns.distplot(SLOPE, hist = True, kde = True, kde_kws = {'shade': True, 'linewidth': 2}, label = "Non-Normal", color ="grey", ax = ax[1,0])
sns.distplot(log_scalar_SLOPE, hist = True, kde = True,  kde_kws = {'shade': True, 'linewidth': 2}, label = "log", color ="red", ax = ax[1,1])
sns.distplot(fitted_SLOPE, hist = True, kde = True,  kde_kws = {'shade': True, 'linewidth': 2}, label = "Box-cox", color ="blue", ax = ax[1,2])
  
#wd- non-normal, log and box-cox
sns.distplot(wd, hist = True, kde = True, kde_kws = {'shade': True, 'linewidth': 2}, label = "Non-Normal", color ="grey", ax = ax[2,0])
sns.distplot(log_scalar_wd, hist = True, kde = True,  kde_kws = {'shade': True, 'linewidth': 2}, label = "log", color ="red", ax = ax[2,1])
sns.distplot(fitted_wd, hist = True, kde = True,  kde_kws = {'shade': True, 'linewidth': 2}, label = "Box-cox", color ="blue", ax = ax[2,2])
  
#plus_CV_d- non-normal, log and box-cox
sns.distplot(wbyd, hist = True, kde = True, kde_kws = {'shade': True, 'linewidth': 2}, label = "Non-Normal", color ="grey", ax = ax[3,0])
sns.distplot(log_scalar_wbyd, hist = True, kde = True,  kde_kws = {'shade': True, 'linewidth': 2}, label = "log", color ="red", ax = ax[3,1])
sns.distplot(fitted_wbyd, hist = True, kde = True,  kde_kws = {'shade': True, 'linewidth': 2}, label = "Box-cox", color ="blue", ax = ax[3,2])
 

# adding legends to the subplots
#plt.legend(loc = "upper right")
  
# rescaling the subplots
fig.set_figheight(5)
fig.set_figwidth(10)
  
#print(f"Lambda value used for Transformation: {fitted_lambdaAc}")

fig.set(ylabel=None)
