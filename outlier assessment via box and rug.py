# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 11:39:36 2021

@author: 45026556
"""

#import packages

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import seaborn as sns


#import dataset as dataframe
df=pd.read_excel((r"D:\SFE scaling analysis\post outlier assessment SFE transformed data.xlsx"),sheet_name='Box-cox (original+scalar)')  


#create color dictionary for each sub-group
color_dict= {1: 'steelblue', 2: 'white', 3: 'salmon'}

#create structure for inserting subplots
# here 1*2 matrix is created i.e. one row and two columns
f, ax = plt.subplots(1, 2, figsize=(4,2))

#create box plots to insert in each of the above created subplot matrics
p1 = sns.boxplot(x="confinment class", y="BC_w", data=df, palette=color_dict, linewidth=1.5, showfliers=False, ax= ax[0])
p2 = sns.boxplot(x="confinment class", y="BC_d", data=df, palette=color_dict, linewidth=1.5, showfliers=False, ax= ax[1])
#p3 = sns.boxplot(x="confinment class", y="BC_wintod", data=df, palette=color_dict, linewidth=1.5, showfliers=False, ax= ax[0,1])
#p4 = sns.boxplot(x="confinment class", y="BC_wbyd", data=df, palette=color_dict, linewidth=1.5, showfliers=False, ax= ax[1,1])
#p5 = sns.boxplot(x="confinment class", y="BC_CV_w", data=df, palette=color_dict, linewidth=1.5, showfliers=False, ax= ax[0,2])
#p6 = sns.boxplot(x="confinment class", y="BC_CV_d", data=df, palette=color_dict, linewidth=1.5, showfliers=False, ax= ax[1,2])
#p7 = sns.boxplot(x="confinment class", y="BC_Std_w", data=df, palette=color_dict, linewidth=1.5, showfliers=False, ax= ax[0,3])
#p8 = sns.boxplot(x="confinment class", y="BC_Std_d", data=df, palette=color_dict, linewidth=1.5, showfliers=False, ax= ax[1,3])

#create rug plots overlaid over each of the above created boxplots in their respective subplot matrics
p1 = sns.stripplot(x="confinment class", y="BC_w", data=df, size=4, color=".3", linewidth=0, ax= ax[0])
p2 = sns.stripplot(x="confinment class", y="BC_d", data=df, size=4, color=".3", linewidth=0, ax= ax[1])
#p3 = sns.stripplot(x="confinment class", y="BC_wintodw", data=df, size=3, color=".3", linewidth=0, ax= ax[0,1])
#p4 = sns.stripplot(x="confinment class", y="BC_wbyd", data=df, size=3, color=".3", linewidth=0, ax= ax[1,1])
#p5 = sns.stripplot(x="confinment class", y="BC_CV_w", data=df, size=3, color=".3", linewidth=0, ax= ax[0,2])
#p6 = sns.stripplot(x="confinment class", y="BC_CV_d", data=df, size=3, color=".3", linewidth=0, ax= ax[1,2])
#p7 = sns.stripplot(x="confinment class", y="BC_Std_w", data=df, size=3, color=".3", linewidth=0, ax= ax[0,3])
#p8 = sns.stripplot(x="confinment class", y="BC_Std_d", data=df, size=3, color=".3", linewidth=0, ax= ax[1,3])


#label the axis
p1.set_ylabel('transformed width')    
p1.set_xlabel('')
p2.set_ylabel('transformed depth')    
p2.set_xlabel('')
#p3.set_ylabel('transformed width*depth')    
#p3.set_xlabel('')
#p4.set_ylabel('transformed width/depth')    
#p4.set_xlabel('')