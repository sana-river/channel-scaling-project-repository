# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 11:43:15 2021

@author: sanakhan
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib auto

#import dataset as dataframe
cleaned=pd.read_excel((r"C:\UCD scaling work\SFE scaling statistical work v2\post outlier assessment SFE transformed data v2 .xlsx"),sheet_name='cleaned')
log=pd.read_excel((r"C:\UCD scaling work\SFE scaling statistical work v2\post outlier assessment SFE transformed data v2 .xlsx"),sheet_name='log')

# creating axes to draw plots
fig, ax = plt.subplots(2, 6)

#create probablity density plots
g1=sns.kdeplot(cleaned['w'], shade=True, color="black", label=False, ax = ax[0,0])
g1.set(label=None)
g1.set(ylabel=None)
g2=sns.kdeplot(log['w'], shade=True, color="b", ax = ax[1,0])
g2.set(xlabel=None)
g2.set(ylabel=None)
g3=sns.kdeplot(cleaned['d'], shade=True, color="black", ax = ax[0,1])
g3.set(xlabel=None)
g3.set(ylabel=None)
g4=sns.kdeplot(log['d'], shade=True, color="b", ax = ax[1,1])
g4.set(xlabel=None)
g4.set(ylabel=None)
g5=sns.kdeplot(cleaned['Ac'], shade=True, color="black", ax = ax[0,2])
g5.set(xlabel=None)
g5.set(ylabel=None)
g6=sns.kdeplot(log['Ac'], shade=True, color="b", ax = ax[1,2])
g6.set(xlabel=None)
g6.set(ylabel=None)
g7=sns.kdeplot(cleaned['% slope'], shade=True, color="black", ax = ax[0,3])
g7.set(xlabel=None)
g7.set(ylabel=None)
g8=sns.kdeplot(log['% slope'], shade=True, color="b", ax = ax[1,3])
g8.set(xlabel=None)
g8.set(ylabel=None)
g9=sns.kdeplot(cleaned['confinement'], shade=True, color="black", ax = ax[0,4])
g9.set(xlabel=None)
g9.set(ylabel=None)
g10=sns.kdeplot(log['confinement'], shade=True, color="b", ax = ax[1,4])
g10.set(xlabel=None)
g10.set(ylabel=None)
g11=sns.kdeplot(cleaned['RUSLE'], shade=True, color="black", ax = ax[0,5])
g11.set(xlabel=None)
g11.set(ylabel=None)
g12=sns.kdeplot(log['RUSLE'], shade=True, color="b", ax = ax[1,5])
g12.set(xlabel=None)
g12.set(ylabel=None)










