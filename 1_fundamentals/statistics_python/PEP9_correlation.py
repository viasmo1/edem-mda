# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:08:04 2019
@author: Alberto Sanz
Percentage Comparison
MDA EDEM
"""
# Resets ALL (Careful This is a "magic" function then it doesn't run as script)
# reset -f

# load basiclibraries
import os
import numpy as np
import pandas as pd
from pandas.api.types import (
    CategoricalDtype,
)  # For definition of custom categorical data types (ordinal if necesary)
import matplotlib.pyplot as plt
import seaborn as sns  # For hi level, Pandas oriented, graphics
import scipy.stats as stats  # For statistical inference
from scipy.stats.stats import pearsonr

# Get working directory
os.getcwd()

# Change working directory
os.chdir(
    "/Users/vicent/repos-github/edem-mda/1_fundamentals/statistics_python/data/lessons"
)
os.getcwd()

# Reads data from CSV file and stores it in a dataframe called rentals_2011
# Pay atention to the specific format of your CSV data (; , or , .)
wbr = pd.read_csv("WBR_11_12_denormalized_temp.csv", sep=";", decimal=",")
wbr.shape
wbr.head()
# QC OK

###########################
# Recoding DV for analysis
res = wbr.cnt.describe()
print(res)
# Store parameters as numbers
m = res[1]
sd = res[2]
n = res[0]

### Recode cnt to string
wbr.loc[(wbr["cnt"] < (m - sd)), "cnt_str"] = "Low rentals"
wbr.loc[
    ((wbr["cnt"] > (m - sd)) & (wbr["cnt"] < (m + sd))), "cnt_str"
] = "Average rentals"
wbr.loc[(wbr["cnt"] > (m + sd)), "cnt_str"] = "High rentals"

### Recode cnt to ordinal
my_categories = ["Low rentals", "Average rentals", "High rentals"]
my_rentals_type = CategoricalDtype(categories=my_categories, ordered=True)
wbr["cnt_cat"] = wbr.cnt_str.astype(my_rentals_type)
wbr.info()

# frequencies & barchart
mytable = pd.crosstab(wbr.cnt_cat, columns="count", normalize="columns") * 100
print(mytable)
print(round(mytable, 1))
plt.bar(mytable.index, mytable["count"])

#######################
# Recode  working day (Independent variable)
# To string
wbr["wd_st"] = wbr.workingday
wbr.wd_st = wbr.wd_st.replace(to_replace=0, value="No")
wbr.wd_st = wbr.wd_st.replace(to_replace=1, value="Yes")
# To category
my_categories = ["No", "Yes"]
my_datatype = CategoricalDtype(categories=my_categories, ordered=True)
wbr["wd_cat"] = wbr.wd_st.astype(my_datatype)
wbr.info()

# Barchart for Working day
mytable = pd.crosstab(index=wbr["wd_cat"], columns="count")  # Crosstab
n = mytable.sum()
mytable2 = (mytable / n) * 100
print(mytable2)
plt.bar(mytable2.index, mytable2["count"])
plt.xlabel("Working Day")
plt.title("Figure 5. Percentage of Working Days")


#######################
# Describe cnt_cat DV (dependent variable) by IV wd_cat (independent variable): crosstab
# frequencies
ct_freq = pd.crosstab(wbr.cnt_cat, wbr.wd_cat, margins=True)
print(ct_freq)
# percentages
ct_perc = (
    pd.crosstab(wbr.cnt_cat, wbr.wd_cat, normalize="columns", margins=True) * 100
).round(2)
print(ct_perc)

# Chi2 test: ALWAYS CROSSTAB WITH FREQUENCIES
ct = pd.crosstab(wbr.cnt_cat, wbr.wd_cat)
stats.chi2_contingency(ct)

# CONCLUSION: p-value>0.05 -> H0: equal means

# Represent ct_perc in a bar plot
# Transpose
ct_perc2 = ct_perc.transpose()
# plot
ct_perc2.plot(kind="bar", edgecolor="black")


#######################
# Describe cnt_cat DV (dependent variable) by IV ws_cat (independent variable): crosstab

# Recode weathersit
# To string
wbr["ws_cat"] = wbr.weathersit
wbr.ws_cat = wbr.ws_cat.replace(to_replace=1, value="Sunny")
wbr.ws_cat = wbr.ws_cat.replace(to_replace=2, value="Cloudy")
wbr.ws_cat = wbr.ws_cat.replace(to_replace=3, value="Rainy")
wbr.ws_cat.describe(include="all")

# frequencies
ct_freq = pd.crosstab(wbr.cnt_cat, wbr.ws_cat, margins=True)
print(ct_freq)
# percentages
ct_perc = (
    pd.crosstab(wbr.cnt_cat, wbr.ws_cat, normalize="columns", margins=True) * 100
).round(2)
print(ct_perc)

# Chi2 test: ALWAYS CROSSTAB WITH FREQUENCIES
ct = pd.crosstab(wbr.cnt_cat, wbr.ws_cat)
stats.chi2_contingency(ct)

# CONCLUSION: p-value<0.05 -> H1: different means

# Represent ct_perc in a bar plot
# Transpose
ct_perc2 = ct_perc.transpose()
# plot
ct_perc2.plot(kind="bar", edgecolor="black", colormap="Blues")
props = dict(boxstyle="round", facecolor="white", lw=0.5)
plt.text(-0.4, 70, "Chi2: 68.76\n" "p-value: 4.13e-14\n" "n: 731\n", bbox=props)
plt.xlabel("Weather Situation")
plt.title("Figure 7. Rentals by Weather Situation.\n")
plt.show()


####################
# CORRELATION

# cnt vs temp_celsius
# HO: no linear association (r=0) vs H1: linear association (r<>0)

# Hitogram of cnt
plt.hist(wbr.cnt, bins=10, edgecolor="black")

# Histogram of temp_celsius
plt.hist(wbr.temp_celsius, bins=10, edgecolor="black")
# temp_celsius seems to have two modes

# Plot a scatter plot
fig1 = plt.figure(figsize=(5, 5))
ax1 = fig1.add_subplot(111)
ax1.scatter(x=wbr.temp_celsius, y=wbr.cnt, facecolors="none", edgecolor="C0")
ax1.set(xlabel="Temperature (ºC)", ylabel="# Daily Rentals")
plt.show()

# Compute Pearson's R
res = pearsonr(x=wbr.temp_celsius, y=wbr.cnt)
print(res)

# RESULT: p-value < 0.05 -> we reject H0

# We see that there are two "groups" in the plot -> the years
# Histogram by year
fig1 = plt.figure(figsize=(5, 5))
ax1 = fig1.add_subplot(111)
ax1.scatter("temp_celsius", "cnt", data=wbr, c="yr")
plt.show()
# Both are convergent when it's cold but when is hotter, the second year we sell more
# BECAUSE: second year there are more stations and bikes.

# Beautify scatter
fig1 = plt.figure(figsize=(5, 5))
ax1 = fig1.add_subplot(111)
ax1.scatter(
    wbr.temp_celsius[wbr.yr == 0],
    wbr.cnt[wbr.yr == 0],
    s=20,
    marker="s",
    facecolors="none",
    edgecolor="C0",
    label="2011",
)
ax1.scatter(
    wbr.temp_celsius[wbr.yr == 1],
    wbr.cnt[wbr.yr == 1],
    s=20,
    marker="^",
    facecolors="none",
    edgecolor="C1",
    label="2012",
)
ax1.set(
    title="Number of rentals vs temperature",
    xlabel="Temperature (ºC)",
    ylabel="# Rentals",
)
ax1.legend(loc="upper right")
plt.show()


# cnt vs windspeed_km
# HO: no linear association (r=0) vs H1: linear association (r<>0)

# Histogram of windspeed_kh
plt.hist(wbr.windspeed_kh, bins=10, edgecolor="black")

# Plot a scatter plot
fig1 = plt.figure(figsize=(5, 5))
ax1 = fig1.add_subplot(111)
ax1.scatter(x=wbr.windspeed_kh, y=wbr.cnt, facecolors="none", edgecolor="C0")
ax1.set(xlabel="Windspeed (km/h)", ylabel="# Daily Rentals")
plt.show()

# Compute Pearson's R
res = pearsonr(x=wbr.windspeed_kh, y=wbr.cnt)
print(res)

# RESULT: p-value < 0.05 -> we reject H0

# We see that there are two "groups" in the plot -> the years
# Histogram by year
fig1 = plt.figure(figsize=(5, 5))
ax1 = fig1.add_subplot(111)
ax1.scatter("windspeed_kh", "cnt", data=wbr, c="yr")


# Both scatters in the same figure
fig = plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(121)
ax1.scatter(x=wbr.temp_celsius, y=wbr.cnt, facecolors="none", edgecolor="C0")
ax1.set(xlabel="Temperature (ºC)", ylabel="# Daily Rentals")
ax2 = fig.add_subplot(122)
ax2.scatter(x=wbr.windspeed_kh, y=wbr.cnt, facecolors="none", edgecolor="C0")
ax2.set(xlabel="Windspeed (km/h)", ylabel="# Daily Rentals")
plt.show()
