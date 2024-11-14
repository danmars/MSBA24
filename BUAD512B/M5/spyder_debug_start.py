# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 11:07:15 2023

@author: mddean
"""

def what_to_wear(temp):
if temp <= 32:
choice = 'Wear winter coat'
elif temp <= 60:
choice = 'Wear light jacket'
elif temp <= 80:
choice = 'Wear pants and T-shirt'
else:
choice = 'Wear shorts and T-shirt'

temperature = input('Please enter today's temperature: ')
                    
outfit = what_to_wear(temperature)
print(outfit)