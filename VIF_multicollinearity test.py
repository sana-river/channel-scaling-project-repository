# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 22:54:28 2021

@author: 45026556
"""

#import packages
import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor
import numpy as np

#construct a function for VIF calculation
def calc_vif(X):
    # Calculating VIF
    vif = pd.DataFrame()
    vif["variables"] = X.columns
    X_values=np.array(X, dtype=float)
    vif["VIF"] = [variance_inflation_factor(X_values, i) for i in range(X.shape[1])]

    return(vif)

#import dataset as dataframe
data=pd.read_excel((r"C:\Users\45026556\Desktop\channel cross section data.xlsx"),sheet_name='Sheet1') 
#revised_data= data[['slope','CV_bf.d','CV_bf.w','CCHEM','ICI','WCHEM']].copy()

#river_df=data.drop(columns='SiteID')

#slice dataframe to select specific columns needed to be transformed
X = data.iloc[:,:-1]

#save VIF results in an array
VIF_results=calc_vif(X)




