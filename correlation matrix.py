# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 13:23:30 2021

@author: sanakhan
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib auto

cleaned=pd.read_excel((r"C:\UCD scaling work\SFE scaling statistical work v2\post outlier assessment SFE transformed data v2 .xlsx"),sheet_name='cleaned')
lg=pd.read_excel((r"C:\UCD scaling work\SFE scaling statistical work v2\post outlier assessment SFE transformed data v2 .xlsx"),sheet_name='log')

data = lg.iloc[:,6:11]


correlation=data.corr()

sns.heatmap(correlation, annot=True)

