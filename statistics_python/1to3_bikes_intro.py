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
os.chdir("/Users/vicent/repos-github/mda/statistics_python/data/data_1to3")
print("Data directory: ", os.getcwd())
print("\n")

# %%
# Read csv file and stores it in a dataframe called rentals_2011
rentals_2011 = pd.read_csv("washington_bike_rentals_2011.csv", sep=";", decimal=",")
print("Rentals 2011 Dataframe info:")
print("Shape: ", rentals_2011.shape)
print(rentals_2011.head())
print(rentals_2011.tail())
print("\n")
# QC OK


# %%
# Plotting histograms
# Select the variable to plot
x = rentals_2011.cnt

# Plot
plt.hist(x, edgecolor="black")
plt.xticks(np.arange(0, 7000, step=1000))
plt.title("Figure 1. Registered rentals in Washington")
plt.show()


# %%
# Read weather info from weather_washington_2011.csv
weather_2011 = pd.read_csv("weather_washington_2011.csv", sep=";", decimal=",")
print("Weather 2011 Dataframe info:")
print("Shape: ", weather_2011.shape)
print(weather_2011.head())
print(weather_2011.tail())
print("\n")
# QC OK


# %%
# Merge rentals_2011 & weather_2011
rentals_weather_2011 = pd.merge(weather_2011, rentals_2011, on="day")
print("rentals_weather_2011 df info:")
print("Shape: ", rentals_weather_2011.shape)
rentals_weather_2011.head()

# Date is duplicated! Remove second version and rename the other one
rentals_weather_2011 = rentals_weather_2011.drop(columns=["dteday_y"])
rentals_weather_2011 = rentals_weather_2011.rename(columns={"dteday_x": "dteday"})
rentals_weather_2011.shape
rentals_weather_2011.head()
print("\n")


#%%
# Create new dataframe with info about 2012 weather
rentals_weather_2012 = pd.read_csv("rentals_weather_2012.csv", sep=";", decimal=",")
print("rentals_weather_2012 df info:")
print("Shape: ", rentals_weather_2012.shape)
rentals_weather_2012.head()
print("\n")
# QC OK

# %%
# Check dimensionality of both dataframes
print("Shape 2011: ", rentals_weather_2011.shape)
print("Shape 2012: ", rentals_weather_2012.shape)
print("\n")
# QC OK


#%% 
# Merge 2011 & 2012 dataframes
rentals_weather_11_12 = rentals_weather_2011.append(rentals_weather_2012, ignore_index=True)
print("rentals_weather_11_12 df info:")
print("Shape: ", rentals_weather_11_12.shape)
print(rentals_weather_11_12.head())
print(rentals_weather_11_12.tail())
print("\n")
# QC OK rentals_weather_11_12


#%%
# LESSON 3

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
