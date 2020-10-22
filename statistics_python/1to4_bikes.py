# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 10:14:42 2020
@author: vicent

EDEM
Master Data Analytics
Statistics with Python
Lessons 1 to 3
Working with the Washington Bike Rentals dataset
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Get working directory
print("Current Working directory: ", os.getcwd())
# Change working directory
os.chdir("/Users/vicent/repos-github/mda/statistics_python/data/lessons")
print("Data directory: ", os.getcwd())
print("\n")


#%%
# LESSON 4

#%%
# Charge new dataframe to work with (WBR_11_12_denormalized_temp.csv) and describe some variables
wbr = pd.read_csv("WBR_11_12_denormalized_temp.csv", sep=";", decimal=",")
print("Shape: ", wbr.shape)
print(wbr.head())
print(wbr.tail())

#%%
# Describe cnt variable (numerical/quantitative variable)
wbr_desc = wbr.cnt.describe()
print(wbr_desc)
print(wbr_desc[["mean", "std"]])


# Plot histogram

# Select variable to plot
x = wbr["cnt"]

# Plot
plt.hist(x, bins=12, edgecolor='black', color='skyblue')
ticks = np.arange(0, 10000, 1000)
plt.xticks(ticks)
plt.title('Figure 1. Daily Bicylce rentals in Washington DC \n by Capital bikeshare. 2011-2012')
plt.xlabel('Number of rented bicycles')
plt.ylabel('Frecuency (days)')
# Add text with main statistics to the plot
# count, mean, std
n = wbr_desc['count']
m = wbr_desc['mean'].round(1)
std = wbr_desc['std'].round(1)
textstr = '$\mathrm{n}=%.0f$\n$\mathrm{mean}=%.1f$\n$\mathrm{std}=%.1f$'%(n, m ,std)
props = dict(boxstyle='round', facecolor='white', lw=0.5)
plt.text(0, 95, textstr, bbox=props)
# Add vertical line in mean, -1std & +1std
plt.axvline(x=m, linewidth=1, linestyle='solid', color='red', label='Mean')
plt.axvline(x=m-std, linewidth=1, linestyle='dashed', color='green', label='-1std')
plt.axvline(x=m+std, linewidth=1, linestyle='dashed', color='green', label='+1std')
# Add legend
plt.legend(loc='upper left', bbox_to_anchor=(0.73, 0.98))

plt.show()


#%%
# Describe weather variable (nominal/qualitative variable)
# frequencies
weather_freq = wbr.groupby(['weathersit']).size()
print(weather_freq)

# percentage
total = weather_freq.sum()
weather_perc = weather_freq / total * 100
weather_perc = weather_perc.round(1)
print(weather_perc)

# Barchart
bar_list = ['Sunny', 'Cloudy', 'Rainy']
plt.bar(bar_list, weather_perc, color='skyblue', edgecolor='black')
plt.title('Figure 2. Percentage of weather situations Washington DC \n by Capital bikeshare. 2011-2012')
plt.xlabel('Weather Situations')
plt.ylabel('Percentage')
# Add legend 
props = dict(boxstyle='round', facecolor='white', lw=0.5)
textstr = '$\mathrm{n}=%.0f$'%(n)
plt.text(2, 60, textstr, bbox=props)

plt.show()
