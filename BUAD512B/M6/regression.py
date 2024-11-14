# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 17:34:09 2023

@author: mddean
"""

# imports
import pandas as pd
import seaborn as sns
import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

from statsmodels.formula.api import ols

# Read in the dataset
cust = pd.read_csv('./data/new_cust.csv')
cust.info()

sns.heatmap(cust.corr(),
            annot=True,
            linewidth=0.5,
            cmap='PuOr',
            vmin=-1,
            vmax=1)

sns.pairplot(cust)


## Time to split the data
# define the output variable, y
y = cust.spend

# define the X
X = cust.drop('spend', axis=1)

# Look at shapes
print(y.shape)
print(X.shape)

# Time to split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                   test_size=0.2,
                                                   random_state=42)

# Look at shapes of X_train and X_test
print(X_train.shape, X_test.shape)


# Time to run a regression
reg = LinearRegression()
reg.fit(X_train, y_train)
print(f'Intercept:    {reg.intercept_}')
print(f'Coefficients: {reg.coef_}')

# Put the resulting coefficients in DataFrame
coefficients_df = pd.DataFrame(
    data = reg.coef_,
    index = X_train.columns,
    columns = ['Coefficient Value'])

print(coefficients_df)

# We can compute the training R-squared, MSE, and RMSE
trainR2 = r2_score(y_train, reg.predict(X_train))
trainMSE = mean_squared_error(y_train, reg.predict(X_train))
trainRMSE = np.sqrt(trainMSE)

print(f'Training R-squared is: {trainR2:.2%}')
print(f'          and MSE is:  {trainMSE:.2f}')
print(f'          and RMSE is: {trainRMSE:.2f}')


# Really interested in the test metrics
pred = reg.predict(X_test)
rSquare = r2_score(y_test, pred)
mse = mean_squared_error(y_test, pred)
rmse = np.sqrt(mse)

print(f'Test R-squared is: {rSquare:.2%}')
print(f'      and MSE is:  {mse:.2f}')
print(f'      and RMSE is: {rmse:.2f}')


# Use the statsmodel ols functionality to 
# easily get summary of regression
# It is easiest to rejoin X and y
data_full = X_train.copy()
data_full['spend'] = y_train

# Create the RHS of the all X variables
rhs = '+'.join(X_train.columns)

# Regress spend on all X variables
mlr_results = ols('spend ~ '+rhs, data=data_full).fit()
print(mlr_results.summary())







