# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 11:57:26 2021

@author: sanakhan
"""

# scatter_plotting.py

import pandas as pd
import matplotlib.pyplot as plt
%matplotlib auto


# read the csv file to extract data

#import dataset as dataframe
d=pd.read_excel((r"C:\UCD scaling work\SFE scaling statistical work v2\post outlier accuracy assessment v2.xlsx"),sheet_name='log depth')

x = d['actual d']
y = d['pred d']
z = d['% accuracy']

plt.scatter(x, y, c=z, cmap="coolwarm", s=50, alpha=0.6, edgecolor='black', linewidth=1)

cbar = plt.colorbar()
cbar.set_label('% accuracy')

plt.xscale('log')
plt.yscale('log')
#plt.title('actual vs predicted')
plt.xlabel('actual depth')
plt.ylabel('predicted depth')

plt.tight_layout()
plt.show()