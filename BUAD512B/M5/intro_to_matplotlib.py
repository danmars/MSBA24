# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 13:46:57 2023

@author: mddean
"""

import matplotlib.pyplot as plt
import pandas as pd

#%% Initial plot
# Create 2 lists: one for x and one for y
x = [0,82.0442626658045,164.140532825633,249.101916493353,
     332.182520454561,416.254670963008,495.330844802651,
     575.152803567278,653.205144040749,738.002602107511,
     818.027625347191,898.118246791891,980.079475188722,
     1061.14169245002,1139.27372549306,1222.46124841828,
     1300.35875796241,1375.56916894815,1450.58381247379,
     1528.61926864683,1605.58397275636,1690.73526419816,
     1765.8607155748,1844.76374052086,1927.68455634244,
     2007.86892722346,2086.83606915306,2166.71913598734,
     2251.80135023691,2335.70816516882,2420.79263834332, 
     2499.86354911873,2577.05890165442,2654.19208140119,
     2730.09283946298,2809.07577275313,2894.08624312766, 
     2969.05670691318,3049.93958564477,3129.75861740531,
     3206.68277248806,3283.60346903165,3364.58552562287, 
     3449.40362446521,3525.4406380069,3608.13685182861,
     3690.05929028829,3773.14656467608,3850.22786804579, 
     3930.30737684189,4015.46434790825,4093.50879464788,
     4172.64841837878,4252.66450124259,4335.57956650011,
     4420.52164467734,4495.52991250898,4575.39742270308,
     4650.49642074232,4730.52574677055,4805.68851119975, 
     4880.60019974235,4960.70865715944,5043.67168991259,
     5118.73724644963,5203.54753389807,5283.38430140739, 
     5359.51383129058,5438.3504224767,5519.19106748314]
y = [69,70.5331166725557,71.5580608629997,71.7925736363559,
     71.3468902075964,70.8280365103217,70.6414982437025, 
     70.4451053764375,70.3795952412711,69.7645648576213,
     69.5426154537094,69.3004779067882,68.9026747371149,
     68.599154906399,68.519069857217,68.3772433121902,
     69.1486631584102,68.7548264957532,68.3609585242701,
     68.5575021969504,68.5786288310157,70.1801398605569,
     69.7914710297875,70.1491959166127,71.3308639026079,
     71.9361568322099,71.7841530239482,71.5632100706621,
     70.9532872882161,70.4120650812618,69.7956890967353,
     69.6193830861858,69.6154149236862,69.6130427165012,
     69.7102463368457,69.5264209638887,68.9050613087613,
     69.1051712486311,68.8193037564598,68.6066819000086,
     68.6092749335593,68.6204785117934,68.3360360051156,
     68.5812312774717,68.3713770000006,69.5440095449469,
     70.5260768620176,72.0285425812187,72.0349254824144,
     71.8158332177273,71.1892654017154,71.1169346409977,
     70.8948191898231,70.6895661675202,70.2298913978404,
     69.6255849641529,69.7340391269025,69.5070018796742,
     69.6617353391113,69.4627544694931,69.630774569752,
     69.8026157834872,69.5269217792645,69.0549816241028,
     69.1984712324886,68.3562401007611,68.1422906748129,
     68.2062726166005,68.0498033914326,68.6018257745021]

# Call plt.subplots()
# Returns both a figure and an axes
fig,ax = plt.subplots()

# See what returned
print('The variable fig is of type',type(fig))
print('The variable ax is of type',type(ax))

# plot on the axes object
ax.plot(x, y)

# Add titles, make it cleaner, etc.

# show the plot
plt.show()



#%%
mlb = pd.read_excel('./data/mlb_outfielders_2022.xlsx')
mlb.info()

# Create a scatter plot between on_base_percentage and on_base_plus_slugging
plt.scatter('on_base_percentage', 'on_base_plus_slugging', data=mlb)

# plt.show()

# plt.savefig('mlb_test.png')

# Create scatter between strike_outs and batting_avg


# Create scatter between strike_outs and home_runs
# Use the color green, make the marks semi-transparent
# and edge color of black
fig, ax = plt.subplots()
ax.scatter('strike_outs', 'home_runs', data=mlb,
            color='g', alpha=0.5, edgecolor='k')



## Look at apple trading data
apple = pd.read_csv('./data/aapl_2022.csv', 
                    thousands = ',',
                    parse_dates = ['Date'])
apple = apple.rename(str.lower, axis='columns')
apple.set_index('date', inplace=True)
apple.info()

# Create a line plot of the closing price
fig, ax = plt.subplots()
ax.plot(apple.close)

# Create histogram of the closing price
fig, ax = plt.subplots()
ax.hist(apple.close)

# Create a histogram of closing price with 25 bins


# Create a boxplot of closing price
fig, ax = plt.subplots()
ax.boxplot(apple.close)

# Create a boxplot of volume


### Back to MLB Data
# Create a horizontal bar chart sorted by home runs
# First, sort the DataFrame and save in new variable
sort_by_hr = mlb.sort_values('home_runs')
# Now plot
fig, ax = plt.subplots()
ax.barh(sort_by_hr.player, sort_by_hr.home_runs)

### Read in states data we saw back in M3
states = pd.read_csv('./data/states.csv')
states.info()

# Get top 6 states by population
top_6 = states.sort_values('Population', ascending=False).head(6)
top_6

# Create a bar plot
fig, ax = plt.subplots() 
ax.bar('State', 'Population', data=top_6)


# Try a horizontal bar chart
fig, ax = plt.subplots()
ax.barh('State', 'Population', data=top_6)

# What happened?
# Fix it so that biggest population is on top


# Create a new column called 'pop_in_millions'

# Want a horizontal bar chart with CA on top
# Import two classes from matplotlib.ticker to help format x-axis 
from matplotlib.ticker import FormatStrFormatter, MultipleLocator

# Plot, add title, add labels for axes, format x-axis
