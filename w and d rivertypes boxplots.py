# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 18:20:00 2021

@author: sanakhan
"""

#import packages
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import seaborn as sns


#import dataset as dataframe
df=pd.read_excel((r"C:\UCD scaling work\SFE scaling statistical work v2\excel files\Network scale full data.xlsx"),sheet_name='Sheet2')


#create color dictionary for each sub-group
color_dict= {1: 'hotpink', 2: 'purple', 3: 'brown', 4: 'green', 5: 'blue', 6: 'yellow', 7: 'crimson'}

#create structure for inserting subplots
# here 1*2 matrix is created i.e. one row and two columns
f, ax = plt.subplots(1, 2, figsize=(8,4))

#create box plots to insert in each of the above created subplot matrics
p1 = sns.boxplot(x="Herve group", y="width", data=df, palette=color_dict, linewidth=1.5, showfliers=True, ax= ax[0])
p2 = sns.boxplot(x="Herve group", y="depth", data=df, palette=color_dict, linewidth=1.5, showfliers=True, ax= ax[1])



#label the axis
p1.set_ylabel('predicted width')    
p1.set_xlabel('stream order')
p2.set_ylabel('predicted depth')    
p2.set_xlabel('stream order')