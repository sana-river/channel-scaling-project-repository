# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 21:52:39 2021

@author: 45026556
"""

import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt')


#import dataset as dataframe
df=pd.read_excel((r"D:\UCD postdoc stuff\SFE scaling\collated data\SFE Colin and Herve data.xlsx"),sheet_name='Sheet1') 
df.dropna(inplace=True)

ward_grp=df['wardgrp']
model = smf.ols(formula='Ac ~ w + d', data=df)
results = model.fit()
label = [1,2,3,4,5,6,7]
colors = ['1','2','3','4','5','6','7']


x, y = model.exog_names[1:]

x_range = np.arange(df[x].min(), df[x].max())
y_range = np.arange(df[y].min(), df[y].max())

X, Y = np.meshgrid(x_range, y_range)

exog = pd.DataFrame({x: X.ravel(), y: Y.ravel()})
Z = results.predict(exog = exog).values.reshape(X.shape)

fig = plt.figure(figsize=plt.figaspect(1)*2)
ax = plt.axes(projection='3d')
ax.scatter(df[x].values, df[y].values,  results.fittedvalues.values, c=ward_grp,
           marker='o', cmap=plt.cm.get_cmap('cubehelix', 7))
cond = df[model.endog_names].values > results.fittedvalues.values
ax.scatter(df[x][cond].values, df[y][cond].values, df[model.endog_names]
           [cond].values, c=df['wardgrp'][cond].values, cmap=plt.cm.get_cmap('cubehelix', 7))
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, alpha = 0.4)
scat=ax.scatter(df[x][cond == False].values, df[y][cond == False].values,
           df[model.endog_names][cond == False].values, c=df['wardgrp'][cond == False].values, cmap=plt.cm.get_cmap('cubehelix', 7))

N=7
bounds = np.linspace(0,N,N+1)
cb = plt.colorbar(scat,ticks=range(7))

ax.set_xlabel('log w')

ax.set_ylabel('log d')

ax.set_zlabel('log Ac')
print(results.summary())

print('Parameters: ', results.params)
print('Standard errors: ', results.bse)
print('Predicted values: ', results.predict())



ax.legend()
plt.show()
