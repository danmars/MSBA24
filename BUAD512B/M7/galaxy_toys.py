# -*- coding: utf-8 -*-
'''
Created on Mon Jan 23 14:57:07 2023

@author: mddean
'''

import pandas as pd
import pulp as pl

model = pl.LpProblem(name='ToyProduction', 
                     sense=pl.LpMaximize)

# Create 2 variables space_rays and phasers
x1 = pl.LpVariable('space_rays', 0, None)
x2 = pl.LpVariable('phasers', 0, None) 


# Create maximize objective function
model += 8 * x1 + 5* x2 

# Create four constraints
model += 2 * x1 + 1 * x2  <= 1200, 'Plastic(lbs)'
model += 3 * x1 + 4 * x2  <= 2400, 'Labor(minutes)'
model += 1 * x1 + 1 * x2  <= 800, 'OverallProduction'
model += 1 * x1 - 1 * x2  <= 450, 'ProductionMix'

# The problem is solved using PuLP's choice of Solver
model.solve()

print(f'Model Status:{pl.LpStatus[model.status]}')
print(f'Objective = {pl.value(model.objective)}')

# Optimal solution
for v in model.variables():
    print(v.name, '=', v.varValue)
  
    

##
# Sensitivity Analysis
##

# use list and dictionary comprehension to get
# shadow price and slack for each constraint  
o = [{'name':name,'shadow price':c.pi,'slack': c.slack} 
     for name, c in model.constraints.items()]

# Make it DataFrame and print it out
print(pd.DataFrame(o))


# Find the reduced cost for each variable
for v in model.variables():
    print(v.name, '=', v.varValue, 
          '\tReduced Cost =', v.dj)
    
    
    
##
# Change objective function to $2 for space rays
##
model.objective = 2 * x1 + 5* x2

model.solve()

print()
print(f'Objective = {pl.value(model.objective)}')
print('\nReduced Costs are:\n')
# Find the reduced cost for each variable
for v in model.variables():
    print(v.name, '=', v.varValue, 
          '\tReduced Cost =', v.dj)
    

## Force making a lot of space rays
model += 1 * x1 >= 1, 'ForceSpaceRayProd' 
model.solve()

print()
print(f'Objective = {pl.value(model.objective)}')
print('\nReduced Costs are:\n')
# Find the reduced cost for each variable
for v in model.variables():
    print(v.name, '=', v.varValue, 
          '\tReduced Cost =', v.dj)
    

#############    
##
# Multiple optimal solutions
##

# delete the forced space ray production constraint
print(model.constraints)
del model.constraints['ForceSpaceRayProd']
print(model.constraints)

# Change obj fn to 3.75x1 + 5x2
model.objective = 3.75 * x1 + 5 * x2
model.solve()

print()
print(f'Objective = {pl.value(model.objective)}')
print('\nReduced Costs are:\n')
# Find the reduced cost for each variable
for v in model.variables():
    print(v.name, '=', v.varValue, 
          '\tReduced Cost =', v.dj)
    
# Try to find other optimal soln
# add constraint of 3.75x1 + 5x2 = 3000
model += 3.75 * x1 + 5 * x2 == 3000, 'objFn'

# change obj fn to max x1
model.objective = 1 * x1
model.solve()

print()
print(f'Objective = {pl.value(model.objective)}')
print('\nReduced Costs are:\n')
# Find the reduced cost for each variable
for v in model.variables():
    print(v.name, '=', v.varValue, 
          '\tReduced Cost =', v.dj)



    
