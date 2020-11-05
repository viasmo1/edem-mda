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

# Represent ct_perc in a bar plot
# Transpose
ct_perc2 = ct_perc.transpose()
# plot
ct_perc2.plot(kind="bar", edgecolor="black")

