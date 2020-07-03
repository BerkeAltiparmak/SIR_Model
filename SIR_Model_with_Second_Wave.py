#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 2020

@author: Berke6 on Github

This program creates an SIR_Model to show how the world might face a second wave 
using the principles stated in Berke Altiparmak's video 
with the title "Numbers of COVID-19: SIR Model"
"""

import numpy as np
import matplotlib.pyplot as plt

S0 = 999 #Initial susceptibles
I0 = 1 #Initial infected(s)
N = S0 + I0 #Total population

day = 0 #Number of days since the first case

S = S0 #Susceptibles
I = I0 #Infected
R = 0 #Removed

beta = 0.944/N #Transmission Rate
gamma = 0.154 #Rate of removal

S_array = [] #Array that will include number of susceptibles each day
I_array = [] #Array that will include number of infected each day
R_array = [] #Array that will include number of removed each day
day_array = [] #Array that will include number of days since the first case

S_array.append(S)
I_array.append(I)
R_array.append(R)
day_array.append(day)

def nextS():
    global S 
    S = S - beta*I*S #Calculates the number of susceptibles in the next day
def nextI():
    global I 
    I = I + beta*I*S - gamma*I #Calculates the number of infected in the next day
def nextR():
    global R 
    R = R + gamma*I #Calculates the number of removed in the next day

while I >= 1:
    nextS()
    nextI()
    nextR()
    day = day + 1
    
    #Creates an effect of 'second wave'
    if(I>=N/10):
        beta = 0.944/N/3
    elif(I<=N/25):
        beta = 0.944/N*5
    
    
    #Adds the calculated values to the arrays:
    S_array.append(S)
    I_array.append(I)
    R_array.append(R)
    day_array.append(day)
    

#If you want to see the animation, type the three quotation marks here

#Converts the arrays into numpy arrays
S_array = np.array(S_array)
I_array = np.array(I_array)
R_array = np.array(R_array)
day_array = np.array(day_array)

#Makes background color
fig, ax = plt.subplots(nrows=1, ncols=1)
fig.patch.set_facecolor('grey')
ax.patch.set_facecolor('black')

# Plots data with days on the x-axis and the three categories on the y-axis:
plt.plot(day_array, S_array, color='g', label='Susceptibles')
plt.plot(day_array, I_array, color='r', label='Infected')
plt.plot(day_array, R_array, color='b', label='Removed')

#Labels:
plt.xlabel('Days Since First Infected Case')
plt.ylabel('Number of People')

plt.legend(loc = 'upper right') #Creates a legend
plt.show()

