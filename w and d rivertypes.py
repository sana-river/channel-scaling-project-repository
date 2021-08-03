# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 16:30:32 2021

@author: sanakhan
"""

# scatter_plotting.py

import pandas as pd
import matplotlib.pyplot as plt
%matplotlib auto


# read the csv file to extract data

#import dataset as dataframe
df=pd.read_excel((r"C:\UCD scaling work\SFE scaling statistical work v2\excel files\Network scale full data.xlsx"),sheet_name='Sheet2')

x = df['width']
y = df['depth']
z = df['Herve group']

color_dict= {1: 'hotpink', 2: 'purple', 3: 'brown', 4: 'green', 5: 'blue', 6: 'yellow', 7: 'crimson'}

plt.scatter(x, y, c=z.apply(lambda x: color_dict[x]), s=50, alpha=0.6, edgecolor='black', linewidth=1)

cbar = plt.colorbar()
cbar.set_label('Herve group')

#plt.xscale('log')
#plt.yscale('log')
#plt.title('actual vs predicted')
plt.xlabel('predicted width')
plt.ylabel('predicted depth')

plt.tight_layout()
plt.show()
