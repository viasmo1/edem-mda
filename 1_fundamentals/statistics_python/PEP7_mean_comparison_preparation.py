# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:08:04 2019
@author: Alberto Sanz
Mean Comparison
MDA EDEM
"""
# Resets ALL (Careful This is a "magic" function then it doesn't run as script)
# reset -f

# load basiclibraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# New libraries
from pandas.api.types import (
    CategoricalDtype,
)  # For definition of custom categorical data types (ordinal if necesary)
import scipy.stats as stats  # For statistical inference
import seaborn as sns  # For hi level, Pandas oriented, graphics

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
print(wbr.shape)
print(wbr.head())
print(wbr.info())
# QC OK

# Recode  working day
# To string
wbr["wd_st"] = wbr.workingday
wbr.wd_st = wbr.wd_st.replace(to_replace=0, value="No")
wbr.wd_st = wbr.wd_st.replace(to_replace=1, value="Yes")
# To category
my_categories = ["No", "Yes"]
my_datatype = CategoricalDtype(categories=my_categories, ordered=True)
wbr["wd_cat"] = wbr.wd_st.astype(my_datatype)
wbr.info()

# frequencies
mytable = pd.crosstab(index=wbr["wd_cat"], columns="count")  # Crosstab
n = mytable.sum()
mytable2 = (mytable / n) * 100
print(mytable2)
plt.bar(mytable2.index, mytable2["count"])
plt.xlabel("Working Day")
plt.title("Figure 5. Percentage of Working Days")


# Perform numeric test t.test: working vs non-working days
# Descriptive comparison
wbr.groupby("wd_cat").cnt.mean()  # Working days have higher mean
# Statistics comparison
# H0: equal means | H1: different means
# Extract the two sub samples and store in two objects
cnt_wd = wbr.loc[wbr.wd_cat == "Yes", "cnt"]
cnt_nwd = wbr.loc[wbr.wd_cat == "No", "cnt"]
# Perform t_test
stats.ttest_ind(cnt_wd, cnt_nwd, equal_var=False)
# Comparison in plot
plt.figure(figsize=(5, 5))
ax = sns.pointplot(x="wd_cat", y="cnt", data=wbr, ci=95, join=0)
plt.yticks(np.arange(3000, 7000, step=500))
plt.ylim(2800, 6200)
plt.axhline(y=wbr.cnt.mean(), linewidth=1, linestyle="dashed", color="green")
props = dict(boxstyle="round", facecolor="white", lw=0.5)
plt.text(
    0.85, 5400, "Mean: 4504.3\n" "n: 731\n" "t: 1.601\n" "Pval.: 0.110\n", bbox=props
)
plt.xlabel("Working Day")
plt.title("Figure 6. Average rentals by Working Day.\n")
plt.show()
# CONCLUSION: p-value>0.05 -> H0: equal means


# Perform numeric test t.test: year 2011 vs year 2012
# Descriptive comparison
wbr.groupby("yr").cnt.mean()
# Statistics comparison
# H0: equal means | H1: different means
# Extract the two sub samples and store in two objects
cnt_2011 = wbr.loc[wbr.yr == 0, "cnt"]
cnt_2012 = wbr.loc[wbr.yr == 1, "cnt"]
# Perform t_test
stats.ttest_ind(cnt_2011, cnt_2012, equal_var=False)
# Comparison in plot
plt.figure(figsize=(5, 5))
ax = sns.pointplot(x="yr", y="cnt", data=wbr, ci=95, join=0)
plt.yticks(np.arange(3000, 7000, step=500))
plt.ylim(2800, 6200)
plt.axhline(y=wbr.cnt.mean(), linewidth=1, linestyle="dashed", color="green")
props = dict(boxstyle="round", facecolor="white", lw=0.5)
plt.text(
    -0.4, 5400, "Mean: 4504.3\n" "n: 731\n" "t: 18.57\n" "Pval.: 1e-6\n", bbox=props
)
plt.xlabel("Year")
plt.title("Figure 6. Average rentals by Year.\n")
plt.show()
# CONCLUSION: p-value<0.05 -> H1: different means


# Perform numeric test ANOVA: weather

# Recode weathersit
# To string
wbr["ws_cat"] = wbr.weathersit
wbr.ws_cat = wbr.ws_cat.replace(to_replace=1, value="Sunny")
wbr.ws_cat = wbr.ws_cat.replace(to_replace=2, value="Cloudy")
wbr.ws_cat = wbr.ws_cat.replace(to_replace=3, value="Rainy")

# Descriptive comparison
wbr.groupby("ws_cat").cnt.mean()

# Statistical comparison
cnt_sunny = wbr.loc[wbr.ws_cat == "Sunny", "cnt"]
cnt_cloudy = wbr.loc[wbr.ws_cat == "Cloudy", "cnt"]
cnt_rainy = wbr.loc[wbr.ws_cat == "Rainy", "cnt"]
# One-way ANOVA
stats.f_oneway(cnt_sunny, cnt_cloudy, cnt_rainy)

# Graphic comparison
plt.figure(figsize=(5, 5))
ax = sns.pointplot(x="ws_cat", y="cnt", data=wbr, ci=95, join=0)
plt.yticks(np.arange(1000, 7000, step=500))
plt.ylim(1000, 6500)
plt.axhline(y=wbr.cnt.mean(), linewidth=1, linestyle="dashed", color="green")
props = dict(boxstyle="round", facecolor="white", lw=0.5)
plt.text(
    -0.4, 5200, "Mean: 4504.3\n" "n: 731\n" "t: 18.57\n" "Pval.: 1e-6\n", bbox=props
)
plt.xlabel("Weather Situation")
plt.title("Figure 7. Average rentals by Weather Situation.\n")
plt.show()
# CONCLUSION: p-value<0.05 -> H1: different means
