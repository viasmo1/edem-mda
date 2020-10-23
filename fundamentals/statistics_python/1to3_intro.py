#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 10:14:42 2020
@author: vicent

EDEM
Master Data Analytics
Statistics with Python
Lessons 1 to 3
Intro
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a dataframe for the class
# Lists are defined in Python with [], separated by commas

name = ['Yaling', 'Sofia', 'María', 'Pablo', 'Inés']
age = [28, 23, 25, 23, 25]
gender = ['Female', 'Female', 'Female', 'Male', 'Female']

class2020 = pd.DataFrame({'name': name, 'age': age, 'gender': gender})

# Clean up
del (name, age, gender)

class2020.shape
class2020.head(3)
class2020.tail(3)
# QC OK

# Get working directory
os.getcwd()
# Change working directory
os.chdir('/Users/vicent/repos-github/mda/statistics_python/data/data_1to3')
os.getcwd()

# Save csv file
class2020.to_csv("class2020.csv")
