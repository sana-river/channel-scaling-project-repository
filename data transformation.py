# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 13:46:08 2021

@author: sanakhan
"""
#import packages
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

#import dataset as dataframe
df=pd.read_excel((r"C:\UCD scaling work\SFE scaling statistical work v2\post outlier assessment SFE transformed data v2 .xlsx"),sheet_name='cleaned')

#slice dataframe to select specific columns needed to be transformed
data = df.iloc[:,5:]


#log transform the above sliced dataframe
log=np.log10(data)

#Box-cox transform the above sliced dataframe by individua column (representing each variable) and save each lambda value simultaneously
BoxCox_w, lambda_w = stats.boxcox(data.iloc[:,0])
BoxCox_d, lambda_d = stats.boxcox(data.iloc[:,1])
BoxCox_Ac, lambda_Ac = stats.boxcox(data.iloc[:,2])
BoxCox_SLOPE, lambda_SLOPE = stats.boxcox(data.iloc[:,5])
BoxCox_CONFINEMEN, lambda_CONFINEMEN = stats.boxcox(data.iloc[:,3])
BoxCox_RUSLE, lambda_RUSLE = stats.boxcox(data.iloc[:,4])
BoxCox_valleyslope, lambda_valleyslope = stats.boxcox(data.iloc[:,6])







