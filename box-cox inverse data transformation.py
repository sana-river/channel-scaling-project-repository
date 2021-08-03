# -*- coding: utf-8 -*-
"""
Created on Thu May 27 15:44:12 2021

@author: 45026556
"""
#import packages
import scipy
from scipy import stats
import pandas as pd


#import dataset as dataframe
data=pd.read_excel((r"C:\UCD scaling work\SFE scaling statistical work v2\post outlier accuracy assessment v2.xlsx"),sheet_name='Box-Cox width') 

#convert dataframe into Box-Cox transformed dataset
boxcox_predicted_width = data.iloc[:,13:16]


inv_boxcox_predicted_width = scipy.special.inv_boxcox(boxcox_predicted_width, -0.25733450298198557)


#Y = data['BC_w']
#a = scipy.special.inv_boxcox(1.658735049, -0.380993994)

#log_data=pd.DataFrame()
#log_xdata=np.log10(X)
#log_ydata=np.log10(Y)
