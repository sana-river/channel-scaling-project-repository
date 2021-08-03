# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 15:43:41 2021

@author: sanakhan
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
%matplotlib auto

#import dataset as dataframe
w=pd.read_excel((r"C:\UCD scaling work\SFE scaling statistical work v2\post outlier accuracy assessment v2.xlsx"),sheet_name='log width')
d=pd.read_excel((r"C:\UCD scaling work\SFE scaling statistical work v2\post outlier accuracy assessment v2.xlsx"),sheet_name='log depth')

fig, ax = plt.subplots(2, 1)

#create lineplots
p1=sns.lineplot(x="S.No.", y="actual w", color='red', data=w, ax = ax[0])
p1=sns.lineplot(x="S.No.", y="pred w", color='black', data=w, ax = ax[0])
p1=sns.lineplot(x="S.No.", y="high w", color='grey', data=w, ax = ax[0])
p1=sns.lineplot(x="S.No.", y="low w", color='grey', data=w, ax = ax[0])


#create lineplots
p2=sns.lineplot(x="S.No.", y="actual d", color='red', data=d, ax = ax[1])
p2=sns.lineplot(x="S.No.", y="pred d", color='black', data=d, ax = ax[1])
p2=sns.lineplot(x="S.No.", y="high d", color='grey', data=d, ax = ax[1])
p2=sns.lineplot(x="S.No.", y="low d", color='grey', data=d, ax = ax[1])

#set labels
p2.set_ylabel('depth (m)') 
p2.set_xlabel('')

#insert legend
#p2.legend(['actual d', 'predicted d', 'high and low SD predicted d'])

