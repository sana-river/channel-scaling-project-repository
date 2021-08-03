# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 15:41:09 2021

@author: 45026556
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#import dataset as dataframe
w=pd.read_excel((r"C:\UCD scaling work\SFE scaling statistical work v2\post outlier accuracy assessment v2.xlsx"),sheet_name='log width')
d=pd.read_excel((r"C:\UCD scaling work\SFE scaling statistical work v2\post outlier accuracy assessment v2.xlsx"),sheet_name='log depth')





fig, ax = plt.subplots(2, 1)

#create probablity density plots
p1=sns.kdeplot(w['actual w'], shade=True, color="r", ax = ax[0])
p1=sns.kdeplot(w['pred w'], shade=True, color="black", ax = ax[0])

#create probablity density plots
p2=sns.kdeplot(d['actual d'], shade=True, color="r", ax = ax[1])
p2=sns.kdeplot(d['pred d'], shade=True, color="black", ax = ax[1])

#insert labels
#plt.xlabel('width')
#plt.ylabel('Probability Density')