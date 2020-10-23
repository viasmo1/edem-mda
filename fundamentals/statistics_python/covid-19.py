# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 14:42:01 2020

@author: vicent

EDEM
Master Data Analytics
Statistics with Python
Analysis Covid-19 in Spain
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %%
# Get working directory
print("Current Working directory: ", os.getcwd())
# Change working directory
os.chdir("/Users/vicent/repos-github/mda/statistics_python/data/covid-19_spain")
print("Data directory: ", os.getcwd())
print("\n")

# %%
# Read csv file and stores it in a dataframe called rentals_2011
covid = pd.read_csv("nacional_covid19_rango_edad.csv", sep=",", decimal=".")
print("Covid-19 Dataframe info:")
print("Shape: ", covid.shape)
print("Columns: ", covid.columns)
print(covid.head())
print(covid.tail())
print("\n")
# QC OK


#%%
# Describe cnt variable (numerical/quantitative variable)
covid_per_day = covid.groupby(["fecha"]).sum()
covid_per_day_desc = covid_per_day.casos_confirmados.describe()
print(covid_per_day_desc)
print(covid_per_day_desc[["mean", "std"]])


# Plot histogram

# Select variable to plot
x = covid["casos_confirmados"]

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
# %%
