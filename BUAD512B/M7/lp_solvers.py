# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 19:12:48 2023

@author: mddean
"""

import pulp as pl

solver_list = pl.listSolvers(onlyAvailable=True)
print(solver_list)