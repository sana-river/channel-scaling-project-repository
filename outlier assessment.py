# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 18:29:02 2021

@author: sanakhan
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
#%matplotlib auto

#import dataset as dataframe
df=pd.read_excel((r"C:\UCD scaling work\SFE scaling statistical work v2\SFE transformed data v2.xlsx"),sheet_name='Box-Cox')

color_dict= {1: 'steelblue', 2: 'white', 3: 'salmon'}

#slice dataframe to select specific columns needed to be transformed
data = df.iloc[:,4:]
f, ax = plt.subplots(1, 2, figsize=(4,2))

p1 = sns.boxplot(x="confinment class", y="w", data=df, palette=color_dict, linewidth=1.5, showfliers=False, ax= ax[0])
p2 = sns.boxplot(x="confinment class", y="d", data=df, palette=color_dict, linewidth=1.5, showfliers=False, ax= ax[1])

p1 = sns.stripplot(x="confinment class", y="w", data=df, size=4, color=".3", linewidth=0, ax= ax[0])
p2 = sns.stripplot(x="confinment class", y="d", data=df, size=4, color=".3", linewidth=0, ax= ax[1])

p1.set_ylabel('width')    
p1.set_xlabel('')
p2.set_ylabel('depth')    
p2.set_xlabel('')



