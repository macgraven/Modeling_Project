#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 10:52:35 2018

@author: ekerns
"""
#Load packages
import pandas
import scipy
import scipy.integrate as spint
from plotnine import *

#Custom function for Ros_Mac
def Ros_Mac_Sim(y,t0,b,a,w,d,e,s):
    H = y[0]
    P = y[1]

    dH_dt = b * H * (1 - a * H) - w * (H / (d + H)) * P
    
    dP_dt = e * w * (H / (d + H)) * P - s * P
    
    return [dH_dt,dP_dt]

#Simulation 1: standard parameters 
#Define parameters
params = (0.8,0.001,5,400,0.07,0.2) #(b,a,w,d,e,s)
times = range(0,100)

#b=prey birth rate 
#Simulate using odeint
y0 = [500,120] #Passed as H and P, respectively
sim = spint.odeint(func=Ros_Mac_Sim,y0=y0,t=times,args=params)

#Creating a DataFrame
simdf = pandas.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a = ggplot(simdf,aes(x="t",y="H"))+geom_line()+ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="red")+theme_classic()
print(a)

#Simulation 2: double b (prey birth rate) 
#See Simulation 1 for descritions of variables, etc. 
params = (0.16,0.001,5,400,0.07,0.2) #(b,a,w,d,e,s)
times = range(0,100)
y0=[500,120]
sim = spint.odeint(func=Ros_Mac_Sim,y0=y0,t=times,args=params)
simdf = pandas.DataFarme({"t":times,"H":sim[:,0],"P":sim[:,1]})
a = ggplot(simdf,aes(x="t",y="H"))+geom_line() + ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="red")+theme_classic()
print(a)

#Simulation 3: half b (prey birth rate)

#Simulation 4: 

#Simulation 5: 

#Simulation 6: 

#Simulation 7:

#Simulation 8: '
