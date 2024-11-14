# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 10:39:27 2023

@author: mddean
"""

# import packages
import pandas as pd
import seaborn as sns

# We'll use a DummyClassifier for fun
from sklearn.dummy import DummyClassifier

# We'll stick with logistic regression 
from sklearn.linear_model import LogisticRegression

# Need to split the data
from sklearn.model_selection import train_test_split

# Need to measure "goodness"
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import PrecisionRecallDisplay
from sklearn.metrics import RocCurveDisplay

## These are also useful, but not used in this example
# from sklearn.metrics import accuracy_score 
# from sklearn.metrics import recall_score
# from sklearn.metrics import average_precision_score
# from sklearn.metrics import f1_score, fbeta_score
# from sklearn.metrics import roc_auc_score, precision_recall_curve
# from sklearn.metrics import precision_recall_fscore_support

# Read in the data from .csv file
default = pd.read_csv('./data/default.csv')
default.shape

# Create a pivot table that shows the number of (non-)students broken
# broken out default or no-default
pd.pivot_table(data=default, values='balance', index='student',
              columns='default', aggfunc='count', margins=True)

# Create dummy variables
default_coded = pd.get_dummies(default, drop_first=True)
default_coded.sample(n=10)

# What is the overall default rate?
print(f'Overall default rate is {default_coded.default_Yes.mean():.2%}')

# Let's try something crazy ... let's fit an OLS model to the data
# Plot it to see what it looks like
#
# Plot balance on x-axis and default_Yes on the y-axis, add regression line
sns.regplot(x='balance', y='default_Yes',
            data=default_coded,
            ci=None)

# Output at top different than OLS
# Coefficients table useful for p-values and for predictions
# Let's plot the logistic regression model
# Turn OFF the confidence interval, otherwise it take time to run
sns.lmplot(x='balance', y='default_Yes',
           data=default_coded,logistic=True,
           ci=None)



# Make the X and y variables
# From some preliminary analysis, I know that income
#  was not statistically significant when running full model
#  so let's also drop that column
y = default_coded.default_Yes
X = default_coded.drop(columns=['default_Yes', 'income'])
X.head()

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# What is the default rates in both training and test??
print(f'Training default rate is {y_train.mean():.2%}')
print(f'Testing default rate is  {y_test.mean():.2%}')

# Split the data with stratification
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.3,
                                                    stratify=y,
                                                    random_state=42)

# What is the default rates in both training and test??
print(f'Training default rate is {y_train.mean():.2%}')
print(f'Testing default rate is  {y_test.mean():.2%}')


# Want a base to compare against
# Create a DummyClassifier with constant strategy
dummy = DummyClassifier(strategy='constant',
                        constant=0)
# Fit it to the training set
dummy.fit(X_train, y_train)

# Can 'score' the dummy classifier for test set
# This is the accuracy of the simple predictions
dummy_accuracy = dummy.score(X_test, y_test)
print('Using the majority class as the prediction', end='')
print(f'gave an accuracy of {dummy_accuracy:.2%}')

# Create a confusion matrix display
ConfusionMatrixDisplay.from_estimator(dummy,
                                      X_test,
                                      y_test,
                                      cmap='cividis')

# Create an ROC Curve display
RocCurveDisplay.from_estimator(dummy, X_test, y_test)

# Create a Precision Recall Display
PrecisionRecallDisplay.from_estimator(dummy, X_test, y_test)

# Create a LogisticRegression
log_reg = LogisticRegression()

# fit the logistic regression model
log_reg.fit(X_train, y_train)

# Print out the estimated intercept and coefficients
print(log_reg.intercept_)
print(log_reg.coef_)

# Print out the confusion matrix
print(confusion_matrix(y_test, log_reg.predict(X_test)))

# Let's make a plot of confusion matrix
ConfusionMatrixDisplay.from_estimator(log_reg,
                                      X_test,
                                      y_test,
                                      cmap='cividis')


# Print the classification_report
print(classification_report(y_test,
                            log_reg.predict(X_test),
                            target_names=['No','Yes']))

# Create an ROC Curve display
RocCurveDisplay.from_estimator(log_reg, X_test, y_test)


# Make a Precision Recall display
PrecisionRecallDisplay.from_estimator(log_reg, X_test, y_test)

# We can "unravel" the values in confusion matrix with .ravel()
true_neg, false_pos, false_neg, true_pos = \
    confusion_matrix(y_test, log_reg.predict(X_test)).ravel()

print(f'true_neg : {true_neg:>4}')
print(f'false_pos: {false_pos:>4}')
print(f'false_neg: {false_neg:>4}')
print(f'true_pos : {true_pos:>4}')

# Let's first look at the overall error rate and accuracy
# Overall error rate = total misclassifications / total chances (sample size)
print(f'Overall Error Rate: {(false_neg+false_pos)/len(y_test):>6.2%}')
print(f'Overall Accuracy  : {(true_neg+true_pos)/len(y_test):>6.2%}')

# Let's look at error rates
# Find the number of defaulter and non-defaulters
totDefaulters = y_test.sum()
totNonDefaulters = len(y_test) - totDefaulters
print(f'# of defaulters: {totDefaulters}')
print(f'# of non-defaulters: {totNonDefaulters}')

# How good are we with non-defaulters? We misclassified 16 non-defaulters
# Error rate = false positives / total non-defaulters
print(f'Error rate for non-defaulters: {false_pos/totNonDefaulters:>6.2%}')
# Accuracy for non-defaulters = true negatives / total non-defaulters
print(f'Accuracy for non-defaulters  : {true_neg/totNonDefaulters:>6.2%}')

# What about those who defaulted?
# Error rate for defaulters = false negatives / total defaulters
print(f'Error rate for defaulters: {false_neg/totDefaulters:>6.2%}')
# Accuracy for defaulters = true positives / total defaulters
print(f'Accuracy for defaulters  : {true_pos/totDefaulters:>6.2%}')





