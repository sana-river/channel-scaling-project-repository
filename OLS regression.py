# -*- coding: utf-8 -*-
"""
Created on Thu May 13 15:54:00 2021

@author: 45026556
"""
#import packages
import pandas as pd
import numpy as np
#import seaborn as sns
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt')
from matplotlib import cm

#import dataset as dataframe
df=pd.read_excel((r"C:\UCD scaling work\SFE scaling statistical work v2\post outlier assessment SFE transformed data v2 .xlsx"),sheet_name='Box-Cox')


#create OLS regression model and save+print results
model = smf.ols(formula='w ~ Ac + percnt_slope + CONFINEMEN + RUSLE', data=df)
results = model.fit()
print(results.summary())

#model = smf.ols(formula='BC_w ~ BC_Ac + BC_CONFINEMEN + BC_SLOPE + BC_RUSLE + BC_D84', data=df)
#model = smf.ols(formula='w ~ Ac + SLOPE + CONFINEMEN + RUSLE + slope_rstr', data=df', data=df)




