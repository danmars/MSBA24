# -*- coding: utf-8 -*-
'''
Created on Tue Jan 17 17:04:43 2023

@author: mddean
'''

# import primary packages
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Read in the iris dataset
iris = pd.read_excel('./data/iris.xlsx')
iris.info()

# See the correlation matrix
iris.corr()

# Create a scatter plot between strongest correlation
plt.scatter(iris.petal_width, iris.petal_length)


### Try a different dataset
# advertising outlets and sales
ads = pd.read_csv('./data/advertising.csv')
ads.info()

ads.describe()

# Create TV vs Sales
''' Format of the scatterplot method is as follows: ax.scatter(x-series, y-series) '''
fig, ax = plt.subplots()
''' 
ax.scatter() statement creates scatterplot
The 'alpha' parameter controls dot transparency: 1 = solid, <1 = various transparency levels, 0 = no mark
The c parameter designates color of the dots: 'b' stands for blue  
'''
ax.scatter(ads.tv, ads.sales, alpha=0.5, c = 'b')  
fig.suptitle('TV Advertising Effect on Sales')   # Graph title
ax.xaxis.set_label_text('TV Advertising Budget')  # x-axis caption
ax.yaxis.set_label_text('Sales')       # y-axis caption

# Social Media vs Sales
''' Format of the scatterplot method is as follows: ax.scatter(x-series, y-series) '''
fig, ax = plt.subplots()
''' 
ax.scatter() statement creates scatterplot
The 'alpha' parameter controls dot transparency: 1 = solid, <1 = various transparency levels, 0 = no mark
The c parameter designates color of the dots: 'red' stands for red
'''
ax.scatter(ads.socialMedia, ads.sales, alpha=0.5, c = 'red')  
fig.suptitle('Social Media Advertising Effect on Sales')   # Graph title
ax.xaxis.set_label_text('Social Media Advertising Budget')  # x-axis caption
ax.yaxis.set_label_text('Sales')       # y-axis caption

# Streaming Radio vs Sales
''' Format of the scatterplot method is as follows: ax.scatter(x-series, y-series) '''
fig, ax = plt.subplots()
''' 
ax.scatter() statement creates scatterplot
The 'alpha' parameter controls dot transparency: 1 = solid, <1 = various transparency levels, 0 = no mark
The c parameter designates color of the dots: 'b' stands for blue  
'''
ax.scatter(ads.streamingRadio, ads.sales, alpha=0.5, c = 'green')  
fig.suptitle('Streaming Radio Advertising Effect on Sales')   # Graph title
ax.xaxis.set_label_text('Streaming Radio Advertising Budget')  # x-axis caption
ax.yaxis.set_label_text('Sales')       # y-axis caption

## What about putting them all on the same plot?
plt.figure()
plt.scatter(ads.tv, ads.sales, color='b')
plt.scatter(ads.socialMedia, ads.sales, color='r')
plt.scatter(ads.streamingRadio, ads.sales, color='g')


# create 1 row by 3 columns subplots, each with a scatter
fig, ax = plt.subplots(1, 3, sharey=True, figsize=(12,5))

# first subplot is TV ad budget on x-axis
ax[0].scatter(ads['tv'], ads['sales'],
             facecolors='none', edgecolors='b')

# second subplot is Social Media on x-axis
ax[1].scatter(ads['socialMedia'], ads['sales'],
             facecolors='none', edgecolors='r')

# third subplot is Streaming Radio on x-axis
ax[2].scatter(ads['streamingRadio'], ads['sales'],
             facecolors='none', edgecolors='g')

# add y-axis label to just the first subplot
ax[0].set_ylabel('Sales ($K)')

# add x-axis labels to each plot to tell me which budget it is
ax[0].set_xlabel('TV')
ax[1].set_xlabel('Social Media')
ax[2].set_xlabel('Streaming Radio')

# Create 3 subplots that are scatter and contain OLS line
fig, ax = plt.subplots(1, 3, sharey=True, figsize=(12,5))

# Make each advertising budget (i.e., TV, Social Media, Streaming Radio)
# have its own row with the associated Sales output. Let's melt!
adsMelted = pd.melt(ads,
                    value_vars=['tv', 'socialMedia', 'streamingRadio'],
                    var_name='advertisingOutlet',
                    id_vars='sales',
                    value_name='budget')

# Look at the new shape
print(adsMelted.shape)
adsMelted.sample(10)
sns.regplot(ax=ax[0], x=ads.tv, y=ads.sales, ci=None, color='b')
sns.regplot(ax=ax[1], x=ads.socialMedia, y=ads.sales, ci=None, color='r')
sns.regplot(ax=ax[2], x=ads.streamingRadio, y=ads.sales, ci=None, color='g')

sns.lmplot(x='budget', y='sales', data=adsMelted, hue='advertisingOutlet', fit_reg=False)

# Let's use open circles
# We need to pass scatter plot keywords using argument scatter_kws
sns.lmplot(x='budget', y='sales', data=adsMelted, hue='advertisingOutlet', fit_reg=False,
          scatter_kws={'facecolor':'none'})

# Make the solid circles more transparent
sns.lmplot(x='budget', y='sales', data=adsMelted, hue='advertisingOutlet', fit_reg=False,
          scatter_kws={'alpha':0.5})


sns.lmplot(x='budget', y='sales', data=adsMelted, hue='advertisingOutlet', fit_reg=False,
          markers=['o', 'x', '+'])

# Heatmap for ads
# Create a heatmap of the correlation matrix
# annot=True will put the correlation coefficient in each square
# linewidths=0.5 puts a white line between the squares
# cmap='Blues' changes the color map to use 'Blues'
plt.figure()
sns.heatmap(ads.corr(), annot=True, linewidths=0.5, cmap='PuOr', vmin=-1.0, vmax=1.0)

### Back to iris dataset
plt.figure()
sns.heatmap(iris.corr(), annot=True, linewidth=0.5, cmap='PuOr',vmin=-1.0, vmax=1.0)

# try pairplot
sns.pairplot(iris)

# Break it out by species
sns.pairplot(iris, hue='species')