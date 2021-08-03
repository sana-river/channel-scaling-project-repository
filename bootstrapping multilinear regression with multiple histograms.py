# -*- coding: utf-8 -*-
"""
Created on Wed May 26 13:29:34 2021

@author: 45026556
"""

#import packages
import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from IPython import get_ipython
from matplotlib import cm

#import dataset as dataframe
df=pd.read_excel((r"C:\UCD scaling work\SFE scaling statistical work v2\post outlier assessment SFE transformed data v2 .xlsx"),sheet_name='log') 

#create empty list that will later contain each bootstrapped value of each independent variable
param1 = []
param2 = []
param3 = []
param4 = []
param5 = []

np.random.seed(1000)

#insert the number of bootstrap runs to undertake
ntrials = 1000

#create a loop to run the regression model 'ntrials' bumber of times using 'frac' as the sptitting datset ratio
for trial in range(ntrials):
    data_sample = df.sample(frac=0.8, replace=True)

    res = smf.ols('d ~ Ac + CONFINEMEN + percnt_slope + RUSLE', data=data_sample).fit()

    param1.append(res.params['Intercept'])
    param2.append(res.params['Ac'])
    param3.append(res.params['CONFINEMEN'])
    param4.append(res.params['percnt_slope'])
    param5.append(res.params['RUSLE'])
    
# end for
#_ = plt.hist(param2, edgecolor='w')


#create histograms enveloping the distribution of coffficent for each independent variable with mean OLS estimate of the cofficient marked as a line 
fig1, ax = plt.subplots(figsize=(5, 5))
sns.distplot(param1, rug=True, hist_kws={'edgecolor': 'w'}, ax=ax)
ax.set_xlabel('Distribution of Intercept coefficient')
ax.set_ylabel('Relative vc Probability')
#ax.set_title('Distribution of Intercept coefficient Value (by Bootstrapping)')
ax.axvline(res.params['Intercept'],color='g',label='OLS estimate of Intercept coefficient')
ax.legend(loc='best')

fig2, ax = plt.subplots(figsize=(5, 5))
sns.distplot(param2, rug=True, hist_kws={'edgecolor': 'w'}, ax=ax)
ax.set_xlabel('Distribution of BC_Ac coefficient')
ax.set_ylabel('Relative vc Probability')
#ax.set_title('Distribution of BC_Ac coefficient Value (by Bootstrapping)')
ax.axvline(res.params['Ac'],color='g',label='OLS estimate of BC_Ac coefficient')
ax.legend(loc='best')

fig3, ax = plt.subplots(figsize=(5, 5))
sns.distplot(param3, rug=True, hist_kws={'edgecolor': 'w'}, ax=ax)
ax.set_xlabel('Distribution of BC_CONFINEMEN coefficient')
ax.set_ylabel('Relative vc Probability')
#ax.set_title('Distribution of BC_CONFINEMEN coefficient Value (by Bootstrapping)')
ax.axvline(res.params['CONFINEMEN'],color='g',label='OLS estimate of BC_CONFINEMEN coefficient')
ax.legend(loc='best')

fig4, ax = plt.subplots(figsize=(5, 5))
sns.distplot(param4, rug=True, hist_kws={'edgecolor': 'w'}, ax=ax)
ax.set_xlabel('Distribution of BC_SLOPE coefficient')
ax.set_ylabel('Relative vc Probability')
#ax.set_title('Distribution of BC_SLOPE coefficient Value (by Bootstrapping)')
ax.axvline(res.params['percnt_slope'],color='g',label='OLS estimate of SLOPE coefficient')
ax.legend(loc='best')

fig5, ax = plt.subplots(figsize=(5, 5))
sns.distplot(param5, rug=True, hist_kws={'edgecolor': 'w'}, ax=ax)
ax.set_xlabel('Distribution of BC_RUSLE coefficient')
ax.set_ylabel('Relative vc Probability')
#ax.set_title('Distribution of BC_RUSLE coefficient Value (by Bootstrapping)')
ax.axvline(res.params['RUSLE'],color='g',label='OLS estimate of BC_RUSLE coefficient')
ax.legend(loc='best')

print(res.summary())