import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

#first row and first column are eliminated as they are synthetic names  and ID
default =pd.read_csv('../data/CreditCard_train.csv',header = 1,usecols=range(1,25))

ColNames=list(default.columns.values)
print(ColNames)

# Repayment status
figs, axs = plt.subplots(3, 2, figsize=(12, 10))
axs = axs.ravel()

for counter in range(6):
    col = default.columns[5+counter]
    distinct=len(default[col].unique())
    sns.set(style="darkgrid")
    sns.countplot(x=str(col), data=default,ax=axs[counter])
    # axs[counter].hist(default[col], bins=distinct,alpha=0.7)
    # axs[counter].grid(axis='y',alpha=0.75)
    # axs[counter].set_title("Repayment status "+col)
plt.show()

#Social Status(SEX, EDUCATION, MARRIAGE)

figs, axs = plt.subplots(1, 3, figsize=(12, 10))
axs = axs.ravel()

for counter in range(3):
    col = default.columns[1+counter]
    distinct=len(default[col].unique())
    sns.set(style="darkgrid")
    sns.countplot(x=str(col), data=default,ax=axs[counter])
    # axs[counter].hist(default[col], bins=distinct,alpha=0.7)
    # axs[counter].grid(axis='y',alpha=0.75)
    # axs[counter].set_title("Repayment status "+col)
plt.show()