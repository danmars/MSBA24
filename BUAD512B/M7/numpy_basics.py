# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 08:44:43 2023

@author: mddean
"""

# import numpy with alias np
import numpy as np

##
# Creating Arrays
##

# From a Python list
n = [1, 3, 5, 7, 9]

odds = np.array(n)

print(odds)
print(f'the variable odds has type {type(odds)}')
print(f'odds has dimensions of {odds.ndim}')
print(f'odds has shape of {odds.shape}')

# Fill array with constant value
all_zeros = np.zeros(4)
print(f'all_zeros = {all_zeros}')
 
all_ones = np.ones(4)
print(f'all_ones = {all_ones}')

all_42 = np.full(4, 42)
print(f'all_42 = {all_42}')

# Fill array from a range
zero_to_4 = np.arange(0, 5)
print(f'zero_to_4 = {zero_to_4}')

zero_to_4_b = np.linspace(0, 4, 5)
print(f'zero_to_4_b = {zero_to_4_b}')

# linspace should be used when increment is not 1
# default number of samples is 50
print(np.linspace(0, 4))

# Multidimensional 
# 2 by 3 matrix
print(np.zeros((2,3)))

# the identity matrix
print(np.identity(4))

# Can use eye also
print(np.eye(4))

# If you want ones offset
print(np.eye(4, k=1))

# Diagonal with other values
print(np.diag(np.arange(0,10,2)))


##
# Index and Slicing
##

# One-dimensional
print(f'odds[0] = {odds[0]}')
print(f'odds[-1] = {odds[-1]}')
print(f'odds[:] = {odds[:]}')
print(f'odds[0:5:2 = {odds[0:5:2]}')

# Multidimensional 
A = np.arange(1,17).reshape(4,4)
print(A)

# Second column
print(f'A[:, 1] = {A[:, 1]}')

# Second row
print(f'A[1, :] = {A[1, :]}')

# Every second element starting from 0, 0
print(f'A[::2, ::2] = {A[::2, ::2]}')

# Every first and third element starting from 1, 0
print(f'A[1::2, 0::3] = {A[1::2, 0::3]}')

# Let's look at visual summary of indexing
# methods for NumPy arrays


##
# Vectorized Functions and Broadcasting
##
# Create a 3 by 3 matrix
B = np.array([[11,12,13],
              [21,22,23],
              [31,32,33]])

print(B)

# Create a single row of 3 columns
single_row = np.array([1,2,3])
print(single_row)

# Add B and the single_row
# single_row will be **broadcasted**
print(f'B + single_row =\n {B+single_row}')

# Create a single column of 3 rows
single_column = np.array([[1],[2],[3]])
print(single_column)

# Add B and the single_column
# single_column will be **broadcasted**
print(f'B + single_column =\n {B+single_column}')

# Let's look at the visual summary of those two actions


##
# Elementwise and Aggregate Functions
##

# There are lots of mathematical functions
# See https://numpy.org/doc/stable/reference/routines.math.html

# Look at B again
print(B)
# Take square root of all elements
print(np.sqrt(B))
# Take the natural log 
print(np.log(B))
# Try floor of natural log
print(np.floor(np.log(B)))


# Aggregate functions
# Create a new matrix C
# with easier numbers
C = np.arange(1,10).reshape(3,3)
print(C)

# Sum all elements of matrix
print(f'np.sum(C) = {np.sum(C)}')

# Average all elements of matrix
print(f'np.mean(C) = {np.mean(C)}')

# sum over the columns with axis=0
print(f'np.sum(C, axis=0) = {np.sum(C, axis=0)}')
# average over the columns with axis=0
print(f'np.mean(C, axis=0) = {np.mean(C, axis=0)}')

# sum over the rows with axis=1
print(f'np.sum(C, axis=1) = {np.sum(C, axis=1)}')
# average over the rows with axis=1
print(f'np.average(C, axis=1) = {np.average(C, axis=1)}')

# Let's look at the visual summary of aggregation
# for columns vs. rows

##
# Matrix and Vector Operations
##
# Matrix manipulations underlie almost all
# numerical calculations in most data science,
# business analytics, or statistical learning
# models and methods. A basic understanding of
# linear algebra can help you fully understand
# the underlying math of the methods you use.
#
# If you don't remember linear algebar, there
# are lots of free (and reasonably good) 
# resources on the web (e.g., Khan Academy)

# Matrix multiplication can be done with np.matmul()
# mulitply C by itself
C2 = np.matmul(C, C)
print(C2)
C3 = np.matmul(C2, C)
print(C3)

# Create a 4 by 1 matrix
D = np.array([[2],[4],[6],[8]])
print(D)

# CANNOT do matrix multiplication
# Num columns in C must match num rows in D
print(np.matmul(C, D))

# Drop last element from D and try again
D = np.delete(D, -1, 0)
print(D)

print(np.matmul(C, D))



# Solve the 2 equations in 2 unknowns
# 2x1 + 3x2 = 4
# 5x1 + 4x2 = 3
# Want to plot the two lines 
import matplotlib.pyplot as plt
x1 = np.linspace(-4, 2)
x2 = np.linspace(-2, 6)

fig, ax = plt.subplots()
ax.plot(x1, -2/3*x1 + 4/3)
ax.plot(x1, -5/4*x1 + 3/4, c='orange')

# Solve Ax = b
my_A = np.array([[2,3], [5,4]])
my_b = np.array([4,3])

import numpy.linalg as la

x = la.solve(my_A, my_b)
print(f'solution is the point {x}')

# Find the rank of the matrix
print(f'rank of my_A is {la.matrix_rank(my_A)}')
# Find the condition number
print(f'condition number of my_A is {la.cond(my_A)}')
# Find the determinant
print(f'determinant of my_A is {la.det(my_A):.2f}')
# Get eigenvalues and eigenvectors
e_vals, e_vecs = la.eig(my_A)
print(f'eigenvalues are {e_vals}')
print(f'eigenvectors are {e_vecs}')

# Plot again with the solution as a point
fig, ax = plt.subplots()
ax.plot(x1, -2/3*x1 + 4/3)
ax.plot(x1, -5/4*x1 + 3/4, c='orange')
ax.scatter(x[0], x[1], color='green')
ax.text(-1.5, 1.5, '(-1,2)')
