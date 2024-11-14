# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 15:48:15 2023

@author: mddean
"""

# Import packages
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Read in the mlb dataset
mlb = pd.read_excel('./data/mlb_outfielders_2022.xlsx')
mlb.info()

# Create a scatter plot with high-level relplot() function
sns.relplot(data=mlb,
           x='strike_outs', y='home_runs',
           hue='player')

# That was not pretty, try again
sns.relplot(data=mlb,
           x='strike_outs', y='home_runs',
           hue='position', style='position')

# Setting the default theme of 'darkgrid'
# This affects ALL matplotlib objects aftewards
sns.set_theme()

sns.relplot(data=mlb,
           x='strike_outs', y='home_runs',
           hue='position')

# Try 'white'
sns.set_style('white')

sns.relplot(data=mlb,
           x='strike_outs', y='home_runs',
           hue='position')

# Try 'whitegrid'
sns.set_style('whitegrid')

sns.relplot(data=mlb,
           x='strike_outs', y='home_runs',
           hue='position')

# Try 'white'
sns.set_style('white')

sns.relplot(data=mlb,
           x='strike_outs', y='home_runs',
           hue='position')

# Try 'ticks'
sns.set_style('ticks')

sns.relplot(data=mlb,
           x='strike_outs', y='home_runs',
           hue='position')


# How many of each position do we have in dataset?
# Need to create a new figure object
# otherwise will draw on previous figure
plt.figure()
sns.countplot(data=mlb,
             x='position')

# Make it horizontal instead
# Need to create a new figure object
# otherwise will draw on previous figure
plt.figure()
sns.countplot(data=mlb,
             y='position')


## High-level approach is to use .catplot()
sns.catplot(data=mlb,
            x='position',
            kind='count')

# Make it horizontal
sns.catplot(data=mlb,
            y='position',
            kind='count')


### .catplot() is flexible
# 
# Categorial scatterplots
# Strip plot - adds jitter by default
sns.catplot(data=mlb,
            x='position',
            y='home_runs',
            kind='strip')


# Turn off jitter
sns.catplot(data=mlb,
            x='position',
            y='home_runs',
            kind='strip',
            jitter=False)

# Swarm plot - works well for relatively small datasets
sns.catplot(data=mlb,
            x='position',
            y='home_runs',
            kind='swarm')

## Comparing distributions
# boxplots
sns.catplot(data=mlb,
            x='position',
            y='home_runs',
            kind='box')


# boxen -- better suited for large datasets
sns.catplot(data=mlb,
            x='position',
            y='home_runs',
            kind='boxen')

# violin plots - uses kde to provide richer description
sns.catplot(data=mlb,
            x='position',
            y='home_runs',
            kind='violin')

## Estimating central tendency
# bar plots
sns.catplot(data=mlb,
            x='position',
            y='home_runs',
            kind='bar')

# point plots
sns.catplot(data=mlb,
            x='position',
            y='home_runs',
            kind='point')

### Get apple trading data
apple = pd.read_csv('./data/aapl_2022.csv', 
                    thousands = ',',
                    parse_dates = ['Date'])
apple = apple.rename(str.lower, axis='columns')
apple.set_index('date', inplace=True)
apple.info()

# Create a line plot for closing price
sns.relplot(data=apple,
            x=apple.index,
            y='close',
            kind='line')

# Look at 'boxen' for larger dataset
sns.catplot(data=apple,
           y='volume',
           kind='boxen')