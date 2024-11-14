# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 15:22:24 2023

@author: mddean
"""

# import primary packages
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Helps with formatting labels on charts
from matplotlib.ticker import FuncFormatter, PercentFormatter

# Reading in Global Super Store dataset
# Somewhat large so make take a little bit
gss = pd.read_excel('./data/GlobalSuperstore.xlsx')
gss.info()

# Interested in seeing sales across regsions
gss.groupby('Region')['Sales'].sum().sort_values()

# Now create a new DataFrame named 'grouped'
grouped = gss.groupby('Region')[['Sales','Quantity','Profit']].sum().sort_values(by='Sales')
grouped

# Try a basic horizontal bar chart
grouped.Sales.plot(kind='barh')

# Put grouped in descending order
desc_grouped = grouped.sort_values(by='Sales', ascending=False)
desc_grouped

# Add percent of sales, cumulative percent of sales, and ranking of sales
desc_grouped['pct'] = desc_grouped.Sales/desc_grouped.Sales.sum()*100
desc_grouped['cum_pct'] = desc_grouped.Sales.cumsum()/desc_grouped.Sales.sum()*100
desc_grouped['rank'] = desc_grouped.Sales.rank(ascending=False)
desc_grouped

### Very, very BAD idea
# Create a pie chart
plt.figure()
plt.pie(desc_grouped.Sales, labels=desc_grouped.index,
        autopct='%1.1f%%', startangle=90, counterclock=False)

###  Probably a BAD idea
# Create a stacked bar chart
plt.figure()
pd.DataFrame(desc_grouped.Sales).T.plot.bar(stacked=True)

### Good Stuff
# Create a bar chart
fig, ax = plt.subplots()
ax.barh(data=grouped, y=grouped.index, width='Sales')
for c in ax.containers:
    labels = [f'${(v.get_width())/1000000:.2f}M' for v in c]
    ax.bar_label(c, labels=labels, label_type='edge')

fig.suptitle(f'Total Sales Across All Regions ${grouped.Sales.sum()/1000000:.2f}M')
ax.set_xlabel('Sales')
ax.set_ylabel('Region')
ax.xaxis.set_major_formatter(
    FuncFormatter(lambda x, pos: '${:,.2f}'.format(x/1000000) + 'M'))

### Using seaborn instead
g = sns.catplot(data=gss,
            x='Sales',
            y='Region',
            kind='bar',
            estimator=sum,
            palette=['cornflowerblue'],
            errorbar=None,
            order=gss.groupby('Region')['Sales'].sum().sort_values(ascending=False).index)

ax = g.facet_axis(0, 0)
ax.set_title(f'Total Sales Across All Regions ${gss.Sales.sum()/1000000:.2f}M')
for c in ax.containers:
    labels = [f'${(v.get_width())/1000000:.2f}M' for v in c]
    ax.bar_label(c, labels=labels, label_type='edge')
    
ax.xaxis.set_major_formatter(
    FuncFormatter(lambda x, pos: '${:,.2f}'.format(x/1000000) + 'M'))

###
# Create a Pareto chart
fig, ax = plt.subplots()
ax.bar(desc_grouped.index, desc_grouped['Sales'], color='C0')
ax2 = ax.twinx()
ax2.plot(desc_grouped.index, desc_grouped['cum_pct'], color='C1', marker='D', ms=5)
ax2.yaxis.set_major_formatter(PercentFormatter())
ax2.set_ylim(0)

ax.yaxis.set_major_formatter(
    FuncFormatter(lambda y, pos: '${:,.2f}'.format(y/1000000) + 'M'))

ax.tick_params(axis='y', colors='C0')
ax2.tick_params(axis='y', colors='C1')

for tick in ax.get_xticklabels():
    tick.set_rotation(45)

fig.suptitle(f'Total Sales Across All Regions ${desc_grouped.Sales.sum()/1000000:.2f}M')
plt.show()
