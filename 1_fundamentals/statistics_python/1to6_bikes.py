# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 10:14:42 2020
@author: vicent

EDEM
Master Data Analytics
Statistics with Python
Lessons 1 to 5 (without introduction steps)
Working with the Washington Bike Rentals dataset
"""

#%%

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Get working directory
print("Current Working directory: ", os.getcwd())
# Change working directory
os.chdir(
    "/Users/vicent/repos-github/edem-mda/1_fundamentals/statistics_python/data/lessons"
)
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
plt.hist(x, bins=12, edgecolor="black", color="skyblue")
ticks = np.arange(0, 10000, 1000)
plt.xticks(ticks)
plt.title(
    "Figure 1. Daily Bicylce rentals in Washington DC \n by Capital bikeshare. 2011-2012"
)
plt.xlabel("Number of rented bicycles")
plt.ylabel("Frecuency (days)")
# Add text with main statistics to the plot
# count, mean, std
n = wbr_desc["count"]
m = wbr_desc["mean"].round(1)
std = wbr_desc["std"].round(1)
textstr = "$\mathrm{n}=%.0f$\n$\mathrm{mean}=%.1f$\n$\mathrm{std}=%.1f$" % (n, m, std)
props = dict(boxstyle="round", facecolor="white", lw=0.5)
plt.text(0, 95, textstr, bbox=props)
# Add vertical line in mean, -1std & +1std
plt.axvline(x=m, linewidth=1, linestyle="solid", color="red", label="Mean")
plt.axvline(x=m - std, linewidth=1, linestyle="dashed", color="green", label="-1std")
plt.axvline(x=m + std, linewidth=1, linestyle="dashed", color="green", label="+1std")
# Add legend
plt.legend(loc="upper left", bbox_to_anchor=(0.73, 0.98))

plt.show()


#%%
# Describe weather variable (nominal/qualitative variable)
# frequencies
weather_freq = wbr.groupby(["weathersit"]).size()
print(weather_freq)

# percentage
total = weather_freq.sum()
weather_perc = weather_freq / total * 100
weather_perc = weather_perc.round(1)
print(weather_perc)

# Barchart
bar_list = ["Sunny", "Cloudy", "Rainy"]
plt.bar(bar_list, weather_perc, color="skyblue", edgecolor="black")
plt.title(
    "Figure 2. Percentage of weather situations Washington DC \n by Capital bikeshare. 2011-2012"
)
plt.xlabel("Weather Situations")
plt.ylabel("Percentage")
# Add legend
props = dict(boxstyle="round", facecolor="white", lw=0.5)
textstr = "$\mathrm{n}=%.0f$" % (n)
plt.text(2, 60, textstr, bbox=props)

plt.show()


# %%

# LESSON 5: SUB-SETTING/SLICING


# %%
# Select a subsample from our data
# 1 Explore year
# Describe year variable (nominal/qualitative variable)
# frequencies
year_freq = wbr.groupby(["yr"]).size()
print(year_freq)

# percentage
total_year = year_freq.sum()
year_perc = year_freq / total_year * 100
year_perc = year_perc.round(1)
print(year_perc)


# %%
# Slicing/Sub-setting our dataframe
# year 2011
wbr_2011 = wbr[wbr.yr == 0]
wbr_2011_desc = wbr_2011.cnt.describe()
print("Describe wbr_2011_desc: ", wbr_2011_desc)
plt.hist(wbr_2011.cnt)
plt.show()

# year 2012
wbr_2012 = wbr[wbr.yr == 1]
wbr_2012_desc = wbr_2012.cnt.describe()
print("Describe wbr_2012_desc: ", wbr_2012_desc)
plt.hist(wbr_2012.cnt)
plt.show()

# Histogram of the bike rentals in Washington on the winter 2012
wbr_2012_winter = wbr[(wbr.yr == 1) & (wbr.season == 1)]
print("wbr_2012_winter shape: ", wbr_2012_winter.shape)
wbr_2012_winter_desc = wbr_2012_winter.cnt.describe()
print("wbr_2012_winter describe: ", wbr_2012_winter_desc)
# Plot histogram
plt.title("Rentals in winter 2012")
plt.hist(wbr_2012_winter.cnt)
plt.show()

# Histogram of the bike rentals in Washington in winter and fall
wbr_winter_autumn = wbr[(wbr.season == 1) | (wbr.season == 4)]
print("wbr_winter_autumn shape: ", wbr_winter_autumn.shape)
wbr_winter_autumn_freq = wbr_winter_autumn.groupby(["season"]).size()
print("Frequency table of seasons: ", wbr_winter_autumn_freq)
wbr_winter_autumn_desc = wbr_winter_autumn.cnt.describe()
print("wbr_winter_autumn_desc describe: ", wbr_winter_autumn_desc)
# Plot histogram
plt.title("Rentals in winter and fall 2011-2012")
plt.hist(wbr_winter_autumn.cnt)
plt.show()


# %%
# Analysing new dataframe wbr_ue.csv

# Charge new dataframe
wbr_ue = pd.read_csv("wbr_ue.csv", sep=";", decimal=",")
print("wbr_ue shape: ", wbr_ue.shape)
print(wbr_ue.head())
print(wbr_ue.tail())

#%%
# Selecting only some columns of the dataframe
my_vars = ["temp_celsius", "cnt"]
wbr_ue_minimal = wbr_ue[my_vars]
print("wbr_ue_minimal shape: ", wbr_ue_minimal.shape)
print(wbr_ue_minimal.head())
# Describe temp_celsius
wbr_ue_minimal_desc = wbr_ue_minimal.temp_celsius.describe()
print("wbr_ue_minimal_desc describe: ", wbr_ue_minimal_desc)
# CAUTION!!! Max temperature = 99 -> there are outliers!!! -> plot an histogram

# There are some outliers!!! Always plot data
plt.hist(wbr_ue_minimal.temp_celsius)
plt.show()

#%%
# Replace outliers with nan
# Clean dataset
wbr_ue["temp_celsius_c"] = wbr_ue.temp_celsius.replace(99, np.nan)
# Describe temp_celsius
wbr_ue_desc = wbr_ue.temp_celsius_c.describe()
print("wbr_ue_desc describe: ", wbr_ue_desc)
# Plot histogram
plt.hist(wbr_ue.temp_celsius_c)
plt.show()
# Drop rows with nan
wbr_ue.temp_celsius_c.dropna()
# Now we can plot the histogram
plt.hist(wbr_ue.temp_celsius_c)
plt.show()

#%%
# Remove all nan of the dataframe
wbr_ue2 = wbr_ue.dropna()
print("wbr_ue shape: ", wbr_ue.shape)
print("wbr_ue2 shape: ", wbr_ue2.shape)

#%%
# Remove duplicated values
print("Duplicates: \n", wbr_ue[wbr_ue.duplicated(keep=False)])
wbr_ue = wbr_ue[wbr_ue.duplicated() == False]
print("wbr_ue2 shape: ", wbr_ue.shape)


# %%

# LESSON 6: CLEANNING & FORMATTING DATA


#%%
# COMPUTING NEW VARIABLES IN OUR DATAFRAME
# casual vs registered rentals ratio
wbr["cs_ratio"] = wbr.casual / wbr.registered
print("cs_ratio:\n", wbr["cs_ratio"])
print('describe wbr["cs_ratio"]:\n', wbr["cs_ratio"].describe())
plt.hist(wbr["cs_ratio"])
plt.show()

# It seems that the cs_ratio has 2 populations
# Analyse working day populations
wbr.groupby(["workingday"]).cs_ratio.describe()


#%%
# RECODING VARIABLES
# season variable
freq_table = wbr.groupby(["season"]).size()
print("season frequencies:\n", freq_table)
# 1st way
season_dict = {1: "Winter", 2: "Spring", 3: "Summer", 4: "Autumn"}
wbr["season_cat"] = wbr.season.replace(season_dict)
wbr.drop(columns="season_cat", inplace=True)
# 2nd way
wbr["season_cat"] = None
wbr.loc[wbr["season"] == 1, "season_cat"] = "Winter"
wbr.loc[wbr["season"] == 2, "season_cat"] = "Spring"
wbr.loc[wbr["season"] == 3, "season_cat"] = "Summer"
wbr.loc[wbr["season"] == 4, "season_cat"] = "Autumn"

# Quality control???
pd.crosstab(wbr.season, wbr.season_cat)
# QC OK

#%%
# cnt variable: from quantitative to qualitative
# 2 ways: mean+/-std or quartiles
wbr_cnt_desc = wbr.cnt.describe()
print("wbr_cnt_desc describe:\n", wbr_cnt_desc)
mean = wbr_cnt_desc["mean"]
std = wbr_cnt_desc["std"]

# Recode 1
wbr.loc[(wbr.cnt < mean - std), "cnt_cat"] = "low rentals"
wbr.loc[
    (wbr.cnt >= mean - std) & (wbr.cnt <= mean + std), "cnt_cat"
] = "average rentals"
wbr.loc[(wbr.cnt > mean + std), "cnt_cat"] = "high rentals"

# Quality control???
plt.scatter(wbr.cnt, wbr.cnt_cat)
plt.axvline(x=mean - std, linewidth=1, linestyle="-", color="red", label="-1std")
plt.axvline(x=mean + std, linewidth=1, linestyle="-", color="red", label="+1std")
plt.show()
# QC OK

# show grouped cnt by new variable cnt_cat
wbr_cnt_cat_grouped = wbr.groupby("cnt_cat").size()
# show datatype
wbr.info()
# change cnt_cat datatype by coercion & order the variable categories
categories = ["low rentals", "average rentals", "high rentals"]
wbr["cnt_cat"] = pd.Categorical(wbr["cnt_cat"], ordered=True, categories=categories)
# show datatype
wbr.info()
# show grouped cnt by new variable cnt_cat
wbr_cnt_cat_grouped = wbr.groupby("cnt_cat").size()
