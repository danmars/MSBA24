# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 15:40:06 2023

@author: mddean
"""

# import primary packages
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Read in the NYC Ride dataset
data = pd.read_excel('./data/NYCRideData_2022.xlsx',
                    parse_dates=['Date'])
data.info()

# Look at head
data.head()

# Try ploting trips per day as a line plot
data['Trips Per Day'].plot()

# Try creating a line plot of the Yellow taxi cabs' trips per day
plt.figure()
plt.plot(data[data['License Class'] == 'Yellow']['Trips Per Day'])

# When plotting with pandas, it often wants a wide format
# Create a new DataFrame named 'trips_per_day'
trips_per_day = data.pivot(index='Date', 
                           columns='License Class', 
                           values='Trips Per Day')
trips_per_day

# Drop 3 of the FHV columns
trips_per_day.drop(columns=['FHV - Black Car', 'FHV - Livery', 'FHV - Lux Limo'],
                  inplace=True)

# Rename the high volume to 'Ride Hail'
trips_per_day.rename(columns={'FHV - High Volume': 'Ride Hail'}, inplace=True)
trips_per_day

###
# Plot the three main ride services in NYC 
trips_per_day.plot(color=['k','g','y'], title='Trips per Day')

###
# Try using seaborn instead
sns.relplot(data=trips_per_day, 
            kind='line',
            palette=['k','g','y']).set(title='Trips per Day')

###
# Let's do the same thing with unique vehicles
unique_veh = data.pivot(index='Date', 
                        columns='License Class', 
                        values='Unique Vehicles')

unique_veh.drop(columns=['FHV - Black Car', 'FHV - Livery', 'FHV - Lux Limo'],
                inplace=True)
unique_veh.rename(columns={'FHV - High Volume': 'Ride Hail'}, inplace=True)
unique_veh

###
# Plot the unique vehicles
sns.relplot(data=unique_veh, 
            kind='line', 
            palette=['k','g','y']).set(title='Unique Vehicles per Day')

###
# What if we wanted to look at trips per day aggegated by year?
annual_trips = trips_per_day.groupby(pd.Grouper(freq='Y')).sum()
annual_trips

sns.relplot(data=annual_trips, 
            kind='line', 
            palette=['k','g','y']).set(title='Trips per Day Aggregated by Year')

###
# Want to try to create a highlight table
# Years for the rows, months for the columns
# Step 1. Add year and month to the data DataFrame
data['year'] = pd.DatetimeIndex(data.Date).year
data['month'] = pd.DatetimeIndex(data.Date).month

# Step 2. Pull out only yellow cabs
yellow = data[data['License Class'] == 'Yellow']

# Step 3. Create the table as a DataFrame
year_and_month = yellow.pivot(index='year', 
                              columns='month', 
                              values='Trips Per Day')
year_and_month


### These only really work in an Jupyter notebook because of HTML
### Step 4. Gradient is EASY!
# year_and_month.style.background_gradient()

# # Step 5. Try stle of bar
# year_and_month.style.bar()


# Step 6. Make a user-defined function for stepped color
#         and use it
#
# def color_all_cells(cell_value):
#     highlight_low = 'background-color: SkyBlue;'
#     highlight_medium = 'background-color: LightSteelBlue;'
#     highlight_big = 'background-color: SteelBlue;'
#     default = ''
    
#     if type(cell_value) in [float, int]:
#         if cell_value <= 253045:
#             return highlight_low
#         elif cell_value <= 468819.5:
#             return highlight_medium
#         else:
#             return highlight_big
    
#     else:
#         return default
    
# year_and_month.style.applymap(color_all_cells)