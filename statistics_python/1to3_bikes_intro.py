#!/usr/bin/env python3
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
os.getcwd()
# Change working directory
os.chdir('/Users/vicent/repos-github/mda/statistics_python/data/data_1to3')
os.getcwd()

# %%
# Read csv file and stores it in a dataframe called rentals_2011
rentals_2011 = pd.read_csv('washington_bike_rentals_2011.csv', sep=';', decimal=',')
rentals_2011.shape
rentals_2011.head()
rentals_2011.tail()
# QC OK


# %%
# Plotting histograms
# Select the variable to plot
x = rentals_2011.cnt

# Plot
plt.hist(x, edgecolor='black')
plt.xticks(np.arange(0, 7000, step=1000))
plt.title('Figure 1. Registered rentals in Wachington')
plt.show()


# %%
# Read weather info from weather_washington_2011.csv
weather_2011 = pd.read_csv('weather_washington_2011.csv', sep=';', decimal=',')
weather_2011.shape
weather_2011.head()
weather_2011.tail()
# QC OK


# %%
# Merge rentals_2011 & weather_2011
rentals_weather_2011 = pd.merge(weather_2011, rentals_2011, on='day')
rentals_weather_2011.shape
rentals_weather_2011.head()

# Date is duplicated! Remove second version and rename the other one
rentals_weather_2011 = rentals_weather_2011.drop(columns=['dteday_y'])
rentals_weather_2011 = rentals_weather_2011.rename(columns={'dteday_x': 'dteday'})
rentals_weather_2011.shape
rentals_weather_2011.head()


# %%
# Scatter plot to analyse relationship between temp and rentals
scatter = plt.scatter(x=rentals_weather_2011.temp_celsius, y=rentals_weather_2011.cnt)
scatter.xlabel('Temperature')
scatter.ylabel('# rentals')
scatter.show()
