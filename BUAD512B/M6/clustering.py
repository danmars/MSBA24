# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 12:34:11 2023

@author: mddean
"""

### Clustering Example
# imports
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

# Read in data
cust = pd.read_csv('./data/customer_sample.csv')
cust.info()

# Drop the two categorical
cust.drop(columns=['Profession','Graduated_College'], inplace=True)
cust.info()

# Want to use Age and Income to make clusters
# Scatter of age and income
sns.relplot(data=cust,
           x='Age',
           y='Income')

# Let's try 3 clusters
kmeans_model = KMeans(n_clusters=3)
clusters = kmeans_model.fit_predict(cust[['Age','Income']])
print(clusters)

# Add clusters to cust DataFrame
cust['3_clusters'] = clusters

# Plot with the different clusters as color
sns.relplot(data=cust,
           x='Age',
           y='Income',
           hue='3_clusters',
           palette=['k','tab:blue', 'tab:orange'])

# Try to find the "correct" number of clusters
# One approach is called the "elbow method"
# Try different values for k
# Look for when the drop in "inertia" falls off less
# Inertia is the sum of squared distances of samples 
# to their closest cluster center
# Create a new list to hold the sum of squared distances
ssd = []
# Try k=2 up to k=8
for k in range(2, 9):
    kmeans_model = KMeans(n_clusters=k)
    kmeans_model.fit(cust[['Age','Income']])
    ssd.append(kmeans_model.inertia_)
plt.figure(figsize=(6, 4), dpi=100)
plt.plot(range(2, 9), ssd, color="green", marker="o")
plt.xlabel("Number of clusters (K)")
plt.ylabel("SSD for K")
plt.show()

# This makes it look like 4 clusters
# Let's try 4 clusters
kmeans_model = KMeans(n_clusters=4)
clusters_4 = kmeans_model.fit_predict(cust[['Age','Income']])
print(clusters_4)

# Add to DataFrame
cust['4_clusters'] = clusters_4

# Plot the four clusters 
sns.relplot(data=cust,
           x='Age',
           y='Income',
           hue='4_clusters',
           palette=['k','tab:blue','tab:orange','tab:green'])

## Need to scale the data
## Age and Income have different ranges
## Income is driving the clusters

# scale data with MinMaxScaler
m_scaler = MinMaxScaler().fit(cust)
m_scaled_cust = pd.DataFrame(m_scaler.transform(cust),
                             columns=cust.columns)
print(m_scaled_cust)

# Do the number of clusters change with scaled data?
ssd2 = []
for k in range(2, 9):
    kmeans_model = KMeans(n_clusters=k)
    kmeans_model.fit(m_scaled_cust[['Age','Income']])
    ssd2.append(kmeans_model.inertia_)
plt.figure(figsize=(6, 4), dpi=100)
plt.plot(range(2, 9), ssd2, color="green", marker="o")
plt.xlabel("Number of clusters (K)")
plt.ylabel("SSD for K")
plt.show()

kmeans_model = KMeans(n_clusters=4)
four_clusters = kmeans_model.fit_predict(
    m_scaled_cust[['Age','Income']])
print(four_clusters)

# Add to DataFrame
cust['4_clusters_scaled'] = four_clusters

# Plot
sns.relplot(data=cust,
           x='Age',
           y='Income',
           hue='4_clusters_scaled',
           palette=['k','tab:blue','tab:orange','tab:green'])



