# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 11:41:44 2023

@author: mddean
"""

# import packages
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#%% exploratory

# Read in a small dataset 
# sample of customers
cust = pd.read_csv('./data/customer_sample.csv')
cust.info()

print(cust.describe(include='all'))

# Create histograms for 'Age' and 'Income'
sns.displot(data=cust,
           x='Age',
           kind='hist',
           kde=True)

plt.figure()
sns.displot(data=cust,
           x='Income',
           kind='hist',
           kde=True)

# Correlation matrix
cust.corr()

# heatmap of correlations
plt.figure()
sns.heatmap(cust.corr(),
           annot=True,
           cmap='PuOr',
           vmin=-1,
           vmax=1)

# Scatter of age and income
sns.relplot(data=cust,
           x='Age',
           y='Income')

#%% imputing

# How many missing values?
print(cust.isna().sum())

# describe them
print(cust.describe(include=object))

# Both are categorical
# Cannot use mean or median
# Look at those rows
print(cust[cust.isnull().values.any(axis=1)])

# Approach 1 - most common class
df_most_common_imputed = cust.apply(
    lambda x: x.fillna(x.value_counts().index[0]))
print(df_most_common_imputed.loc[
    cust[cust.isnull().values.any(axis=1)].index])

# Approach 2 - Use 'Unknown'
df_unknown_imputed = cust.fillna('Unknown')
print(df_unknown_imputed.loc[
    cust[cust.isnull().values.any(axis=1)].index])

# Look rows 4, 5, and 6
# Row 5 has empty Profession
print(cust[4:7])

# Approach 3 - forward fill
df_ffill_imputed = cust.fillna(method='ffill')
print(df_ffill_imputed.loc[
    cust[cust.isnull().values.any(axis=1)].index])

# Approach 4 - backward fill
df_ffill_imputed = cust.fillna(method='bfill')
print(df_ffill_imputed.loc[
    cust[cust.isnull().values.any(axis=1)].index])

## sklearn has SimpleImputer, IterativeImputer, and KNNImputer
## You should investigate those classes

#%% encoding
# import Ordinal Encoder
from sklearn.preprocessing import OrdinalEncoder

# Create an instance
enc = OrdinalEncoder()
# fit and transform two columns
print(enc.fit_transform(cust[['Profession','Graduated_College']]))

# What are the categories?
print(enc.categories_)

# Undo transformed data
print(enc.inverse_transform([[6,1]]))

# Make a nice DataFrame
o_encoded = pd.DataFrame(
    enc.fit_transform(cust[['Profession','Graduated_College']]),
    columns=['Profession_Coded', 'Graduated_College_Coded'])
print(o_encoded.head())

# Add coded variables 
cust2 = pd.concat([cust, o_encoded], axis=1)
print(cust2.head())

## Creating Dummy Variables
# pandas makes this easy
print(pd.get_dummies(cust.Graduated_College))

# apply to entire DataFrame
dummy_data = pd.get_dummies(cust)
# look at 3 rows
print(dummy_data[4:7])

# Drop one dummy from each category
# can use drop_first=True
print(pd.get_dummies(cust.Graduated_College,
              drop_first=True))

## If you want a specific base, then create 
## all dummies and manually drop the base 

## One-Hot Encoding (ML speak)
# import OneHotEncoder
from sklearn.preprocessing import OneHotEncoder

# one-hot encode 'Profession'
ohe = OneHotEncoder(sparse=False)
ohe_results = ohe.fit_transform(cust[['Profession']])

# Converting OneHotEncoded results into an dataframe
# Set the column names to the categories it used
df_ohe_results = pd.DataFrame(ohe_results, 
                              columns=ohe.categories_)

# Viewing first few rows of data
print(df_ohe_results.head(10))


ohe2_results = ohe.fit_transform(cust[['Graduated_College']])
# Converting OneHotEncoded results into an dataframe
df_ohe2_results = pd.DataFrame(ohe2_results,
                               columns=ohe.categories_)
# Viewing first few rows of data
print(df_ohe2_results.head(10))

#%% training and test sets

# import train_test_split
from sklearn.model_selection import train_test_split

# Read in bigger and different customer dataset
customers = pd.read_csv('./data/customers.csv',
                  parse_dates=['join_date', 'last_purchase_date'])
customers.info()

# Look at 7 rows
print(customers.sample(7))

# summary statisticd for numerical columns
print(customers.describe())

# Using .value_counts is useful for categorical columns
print(customers.gender.value_counts(normalize=True))

print(customers.value_counts(subset=['gender',
                               'marital_status',
                               'home_ownership'],
                             normalize=True))

## Time to split the data
# define the output variable, y
y = customers.spend

# define the X
X = customers.drop('spend', axis=1)

# Look at shapes
print(y.shape)
print(X.shape)

# Time to split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                   test_size=0.2,
                                                   random_state=42)

# Look at shape of X_train
print(X_train.shape)

# Look at shape of X_test
print(X_test.shape)

# See split of gender in test set
print(X_test.gender.value_counts(normalize=True))

## Looks okay for this dataset
## If not, you can use the argument stratify when splitting

#%% scaling

# Import 2 different scalers
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Read in the small customer sample again
cust2 = pd.read_csv('./data/customer_sample.csv')

# drop the 2 object columns
cust2.drop(columns=['Profession','Graduated_College'], inplace=True)
cust2.info()

## Going to scale entire very small dataset
## In general, this is a BAD idea for supervised methods
## We are going to use unsupervised for this dataset,
## so, it's "okay"

# Create a StandardScaler and fit cust2
s_scaler = StandardScaler().fit(cust2)

## Create DataFrame with transformed data
s_scaled_cust = pd.DataFrame(s_scaler.transform(cust2),
                             columns=cust2.columns)
print(s_scaled_cust.head())

# Let's plot original and transformed
fig, ax = plt.subplots(2)

ax[0].hist(cust2.Age)
ax[1].hist(s_scaled_cust.Age)

plt.show()

# Create a MinMaxScaler and fit cust2
m_scaler = MinMaxScaler().fit(cust2)

# Create DataFrame wtih transformed data
m_scaled_cust = pd.DataFrame(m_scaler.transform(cust2),
                             columns=cust2.columns)
print(m_scaled_cust.head())


# Let's plot original and transformed
fig, ax = plt.subplots(2)

ax[0].hist(cust2.Age)
ax[1].hist(m_scaled_cust.Age)

plt.show()

#%% pipelines
# imports
from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression

# manually create a Pipeline
print(Pipeline([
    ('scale', StandardScaler()),
    ('lr', LinearRegression())
]))

# make_pipeline stramlines this process
print(make_pipeline(StandardScaler(), LinearRegression()))


## Can use Pipeline inside a ColumnTransformer
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

ct = ColumnTransformer([
    ('impute', Pipeline([
        ('impute', SimpleImputer()),
        ('scale', StandardScaler())
    ]), [0]),
    ('standard_scale', StandardScaler(), [1]),
    ('min_mix', MinMaxScaler(), [3])
])

print(ct.fit_transform(cust))






