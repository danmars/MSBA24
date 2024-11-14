# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 16:56:16 2023

@author: mddean
"""

# import primary packages
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Read in the grades dataset
grades = pd.read_excel('./data/grades.xlsx')
grades.info()

# Try .hist() from the DataFrame
grades.hist()

# Change number of bins
plt.figure()
grades.hist(bins=15)

# Set the bin edges
plt.figure()
grades.hist(bins=[10,20,30,40,50,60,70,80,90,100],
            grid=False)

# Try seaborn
sns.displot(data=grades, kind='hist')

# Custom bin edges and setting title
sns.displot(data=grades, 
            bins=[10,20,30,40,50,60,70,80,90,100],
            kind='hist').set(title='Grade Distribution')

# Add a rug plot
sns.displot(data=grades, 
            bins=[10,20,30,40,50,60,70,80,90,100],
            kind='hist',
            rug=True).set(title='Grade Distribution')

# Try kernel density estimation
sns.displot(data=grades, kind='kde',
            rug=True).set(title='Grade Distribution')

# Add kde on top of histogram
sns.displot(data=grades, x='Grade',
           bins=[10,20,30,40,50,60,70,80,90,100],
           kde=True,).set(title='Grade Distribution')

# Using matplotlib, we can use 'step' to mimic a frequency polygon
plt.figure()
plt.hist(grades.Grade, bins=[10,20,30,40,50,60,70,80,90,100],
        histtype='step')

# Break the distribution up by gender
plt.figure()
sns.displot(data=grades, x='Grade', hue='Gender',
            bins=[10,20,30,40,50,60,70,80,90,100],
            kind='hist')

# This is when frequency polygon is better
plt.figure()
plt.hist([grades[grades['Gender']=='F'].Grade,
          grades[grades['Gender']=='M'].Grade],
         histtype='step',
         bins=[10,20,30,40,50,60,70,80,90,100])

plt.legend(['M','F'])

# Boxplots
plt.figure()
grades.boxplot(grid=False, figsize=(2,5))

# Break out by gender
plt.figure()
grades.boxplot(column='Grade', by='Gender', grid=False, figsize=(5,5))

# Try seaborn for boxplots
plt.figure()
sns.boxplot(data=grades)

# Break out by group
plt.figure()
sns.boxplot(data=grades, x='Gender', y='Grade', order=['F', 'M'])

# Another look
plt.figure()
sns.boxplot(data=grades, x='Grade', y='Gender',
           notch=True, flierprops={'marker':'x'})
