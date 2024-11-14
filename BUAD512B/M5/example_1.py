# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

# Read in the Apple trading data
apple = pd.read_csv('./data/aapl_2022.csv',
                    thousands=',',
                    parse_dates=['Date'])
apple.info()

