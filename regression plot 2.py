# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 15:37:04 2021

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
from matplotlib import cm

#import dataset as dataframe
df=pd.read_excel((r"D:\SFE scaling analysis\SFE data.xlsx"),sheet_name='log') 
df.dropna(inplace=True)

ward_grp=df['wardgrp']
model = smf.ols(formula='D84 ~ Ac + vc', data=df)
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
           cmap="RdBu_r", marker='o', alpha=0.6, s=40, edgecolors='black')
cond = df[model.endog_names].values > results.fittedvalues.values
ax.scatter(df[x][cond].values, df[y][cond].values, df[model.endog_names]
           [cond].values, c=df['wardgrp'][cond].values, cmap="RdBu_r", marker='o', alpha=0.6, s=40, edgecolors='black')
ax.plot_surface(X, Y, Z, rstride=10, cstride=10, alpha = 0.5, linewidth=0, antialiased=False, cmap=cm.coolwarm)
scat=ax.scatter(df[x][cond == False].values, df[y][cond == False].values,
           df[model.endog_names][cond == False].values, c=df['wardgrp'][cond == False].values, cmap="RdBu_r", marker='o', alpha=0.6, s=40, edgecolors='black')

N=8
bounds = np.linspace(0,N,N+1)
cb = plt.colorbar(scat,ticks=range(8),shrink=0.4, extend='both')

#cb.ax.set_ylabel('ward group', rotation=270)



ax.set_xlabel('log Ac')

ax.set_ylabel('log Vc')

ax.set_zlabel('log D84')
print(results.summary())

print('Parameters: ', results.params)
print('Standard errors: ', results.bse)
print('Predicted values: ', results.predict())



ax.legend()
plt.show()

