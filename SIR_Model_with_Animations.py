#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 2020

@author: Berke6 on Github

This program creates an SIR_Model with animations using the principles stated in Berke Altiparmak's
video with the title "Numbers of COVID-19: SIR Model"
"""

import numpy as np
import matplotlib
matplotlib.use("Agg") #Use this if you want the graph to be plotted with animation
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

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

#Creates a background color
fig = plt.figure()
ax = plt.subplot(1, 1, 1)
fig.patch.set_facecolor('xkcd:light brown')
ax.patch.set_facecolor('xkcd:dark brown')

#Increase this if you want to skip some data, but I see no reason to do that...
data_skip = 1

#Creates the graph
def init_func():
    ax.clear()
    plt.xlabel('Days Since First Infected Case')
    plt.ylabel('Number of People')
    #plt.xlim((0, 60)) #If you want to have an x limit
    #plt.ylim((0, N)) #If you want to have a y limit

#Plotting data by data
def update_plot(i):
    ax.plot(day_array[i:i+data_skip], S_array[i:i+data_skip], color='k', label='Susceptible')
    ax.scatter(day_array[i], S_array[i], marker='o', color='g', label='Susceptible')
    ax.plot(day_array[i:i+data_skip], I_array[i:i+data_skip], color='k', label='Infected')
    ax.scatter(day_array[i], I_array[i], marker='o', color='r', label='Infected')
    ax.plot(day_array[i:i+data_skip], R_array[i:i+data_skip], color='k', label='Removed')
    ax.scatter(day_array[i], R_array[i], marker='o', color='b', label='Removed')



#Setting up the formatting of the movie files so that the animation can be saved
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)

#Creates the animation (increase interval for faster graphing)
anim = FuncAnimation(fig,
                     update_plot,
                     frames=np.arange(0, len(day_array), data_skip),
                     init_func=init_func,
                     interval=20)

#Saves the graph on your computer
anim.save('testGraph.mp4', writer=writer)


    
    

    
    
