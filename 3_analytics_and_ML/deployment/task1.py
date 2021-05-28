# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading data from csv file
houseprice = pd.read_csv("houseprice.csv", sep=";", decimal=",")

# Show head of file and column names
print(houseprice.head())
print(houseprice.columns)
print(houseprice.dtypes)
print(houseprice.shape)

# Analyse target variable SalePrice
print(houseprice.SalePrice.describe())
plt.hist(houseprice.SalePrice, bins=20)
plt.show()

# Remove outliers
houseprice = houseprice[
    (houseprice.SalePrice > 500000000) & (houseprice.SalePrice < 2400000000)
]
print(houseprice.SalePrice.describe())
plt.hist(houseprice.SalePrice, bins=20)
plt.show()

# Analyse quantitatve and qualitative variables
quantitative = [f for f in houseprice.columns if houseprice.dtypes[f] != "object"]
quantitative.remove("SalePrice")
quantitative.remove("Id")
print(quantitative)
print(len(quantitative))
qualitative = [f for f in houseprice.columns if houseprice.dtypes[f] == "object"]
print(qualitative)
print(len(qualitative))

