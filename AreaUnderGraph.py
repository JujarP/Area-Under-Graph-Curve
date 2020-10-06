# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 10:48:39 2020

@author: Jujar
"""

"""""""""
Python script for finding the area under the curve
"""""""""

import numpy as np                               #Import numpy
import pandas as pd                              #Import pandas
import matplotlib.pyplot as plt                  #Import plotting library
from scipy.integrate import trapz, simps         #Import integration library
                                                 #trapz = trapezium rule
                                                 #simps = simpsons rule

data = pd.read_table("SampleData2.txt",sep="\s+") #Import the data
x = data["x"].values                             #Assign x
y = data["y"].values                             #Assign y

#print(x)                                         #Sanity check
#print(y)                                         #Sanity check

plt.plot(x,y)

print("area under graph", trapz(y, x))
print("area under graph", simps(y, x))