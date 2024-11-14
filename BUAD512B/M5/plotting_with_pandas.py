# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 11:35:02 2023

@author: mddean
"""

# %% imports
import pandas as pd

# %% get data
apple = pd.read_csv('./data/aapl_2022.csv', 
                    thousands = ',',
                    parse_dates = ['Date'])

apple.info()
#%% failed plot
# This will fail
apple.plot()

#%% modify DataFrame

apple = apple.rename(str.lower, axis='columns')
apple.set_index('date', inplace=True)
apple.info()

#%% plot everything
apple.plot()

#%% plot close

# Just calling .plot()

# Create histogram

# Change number of bins

# Create boxplot

# Look at boxplot for volume
