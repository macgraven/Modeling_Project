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
import numpy 

#Custom function for Ros_Mac
def Ros_Mac_Sim(y,t0,b,a,w,d,e,s):
    H = y[0]
    P = y[1]
    #H = prey (herbivore), P = predator

    dH_dt = b * H * (1 - a * H) - w * (H / (d + H)) * P
    
    dP_dt = e * w * (H / (d + H)) * P - s * P
    
    return [dH_dt,dP_dt]

#Simulation 1: standard parameters 
#Define parameters
params = (0.8,0.001,5,400,0.07,0.2) #(b,a,w,d,e,s)
times = numpy.arange(0,100,0.1)
#b = prey birth rate 
#a = alpha = intra-specfic competition coefficient = carrying capacity 
#w = maximum predator attack rate 
#d = handling time of predator per prey = how much time predator spends on single prey (catch, digest, etc.)
#e = conversion efficiency of prey to predators 
#s = predator death rate 

#Simulate using odeint
y0 = [500,120] #Passed as H and P, respectively
sim = spint.odeint(func=Ros_Mac_Sim,y0=y0,t=times,args=params)

#Creating a DataFrame
simdf = pandas.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a = ggplot(simdf,aes(x="t",y="H"))+geom_line(color="black",size=1.5)+ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="blue",size=1.5)+theme_classic()
print(a)


#Simulation 2: double b (prey birth rate) 
#See Simulation 1 for descritions of variables, etc. 
params = (1.6,0.001,5,400,0.07,0.2) #(b,a,w,d,e,s)
times = numpy.arange(0,100,0.1)
y0=[500,120]
sim = spint.odeint(func=Ros_Mac_Sim,y0=y0,t=times,args=params)
simdf = pandas.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a = ggplot(simdf,aes(x="t",y="H"))+geom_line(color="black",size=1.5) + ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="blue",size=1.5)+theme_classic()
print(a)

#Simulation 3: halve b (prey birth rate)
params = (0.4,0.001,5,400,0.07,0.2) #(b,a,w,d,e,s)
times = numpy.arange(0,100,0.1)
y0=[500,120]
sim = spint.odeint(func=Ros_Mac_Sim,y0=y0,t=times,args=params)
simdf = pandas.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a = ggplot(simdf,aes(x="t",y="H"))+geom_line(color="black",size=1.5) + ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="blue",size=1.5)+theme_classic()
print(a)

#Simulation 4: triple a (competition coefficient)
params = (0.8,0.002,5,400,0.07,0.2) #(b,a,w,d,e,s)
times = numpy.arange(0,100,0.1)
y0=[500,120]
sim = spint.odeint(func=Ros_Mac_Sim,y0=y0,t=times,args=params)
simdf = pandas.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a = ggplot(simdf,aes(x="t",y="H"))+geom_line(color="black",size=1.5) + ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="blue",size=1.5)+theme_classic()
print(a)

#Simulation 5: halve a (competition coefficient)
params = (0.8,0.0005,5,400,0.07,0.2) #(b,a,w,d,e,s)
times = numpy.arange(0,100,0.1)
y0=[500,120]
sim = spint.odeint(func=Ros_Mac_Sim,y0=y0,t=times,args=params)
simdf = pandas.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a = ggplot(simdf,aes(x="t",y="H"))+geom_line(color="black",size=1.5) + ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="blue",size=1.5)+theme_classic()
print(a)

#Simulation 6: double w (maximum predator attack rate)
params = (0.8,0.001,10,400,0.07,0.2) #(b,a,w,d,e,s)
times = numpy.arange(0,100,0.1)
y0=[500,120]
sim = spint.odeint(func=Ros_Mac_Sim,y0=y0,t=times,args=params)
simdf = pandas.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a = ggplot(simdf,aes(x="t",y="H"))+geom_line(color="black",size=1.5) + ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="blue",size=1.5)+theme_classic()
print(a)

#Simulation 8: double d (handling time predator per prey)
params = (0.8,0.001,10,800,0.07,0.2) #(b,a,w,d,e,s)
times = numpy.arange(0,100,0.1)
y0=[500,120]
sim = spint.odeint(func=Ros_Mac_Sim,y0=y0,t=times,args=params)
simdf = pandas.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a = ggplot(simdf,aes(x="t",y="H"))+geom_line(color="black",size=1.5)+ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="blue",size=1.5)+theme_classic()
print(a)

#Simulation 9: halve d (handling time predator per prey)
params = (0.8,0.001,10,200,0.07,0.2) #(b,a,w,d,e,s)
times = numpy.arange(0,100,0.1)
y0=[500,120]
sim = spint.odeint(func=Ros_Mac_Sim,y0=y0,t=times,args=params)
simdf = pandas.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a = ggplot(simdf,aes(x="t",y="H"))+geom_line(color="black",size=1.5)+ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="blue",size=1.5)+theme_classic()
print(a)

#Simulation 10: double e (conversion efficiency)
params = (0.8,0.001,10,400,0.14,0.2) #(b,a,w,d,e,s)
times = numpy.arange(0,100,0.1)
y0 = [500,120]
sim = spint.odeint(func=Ros_Mac_Sim,y0=y0,t=times,args=params)
simdf = pandas.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a = ggplot(simdf,aes(x="t",y="H"))+geom_line(color="black",size=1.5)+ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="blue",size=1.5)+theme_classic()
print(a)


#Simulation 11: halve e (conversion efficiency)
params = (0.8,0.001,10,400,0.035,0.2) #(b,a,w,d,e,s)
times = numpy.arange(0,100,0.1)
y0 = [500,120]
sim = spint.odeint(func=Ros_Mac_Sim,y0=y0,t=times,args=params)
simdf = pandas.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a = ggplot(simdf,aes(x="t",y="H"))+geom_line(color="black",size=1.5)+ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="blue",size=1.5)+theme_classic()
print(a)

#Simulation 12: triple s (predator death rate)
params = (0.8,0.001,5,400,0.07,0.6) #(b,a,w,d,e,s)
times = numpy.arange(0,100,0.1)
y0 = [500,120]
sim = spint.odeint(func=Ros_Mac_Sim,y0=y0,t=times,args=params)
simdf = pandas.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a = ggplot(simdf,aes(x="t",y="H"))+geom_line(color="black",size=1.5)+ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="blue",size=1.5)+theme_classic()
print(a)

#Simulation 13: halve s (predator death rate)
params = (0.8,0.001,5,400,0.07,0.1) #(b,a,w,d,e,s)
times = numpy.arange(0,100,0.1)
y0 = [500,120]
sim = spint.odeint(func=Ros_Mac_Sim,y0=y0,t=times,args=params)
simdf = pandas.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a = ggplot(simdf,aes(x="t",y="H"))+geom_line(color="black",size=1.5)+ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="blue",size=1.5)+theme_classic()
print(a)


#Paradox of Enrichment 
#Simulation 14:
params = (0.8,0.00125,5,400,0.07,0.2) #(b,a,w,d,e,s) | Carrying Capacity of 800
times = numpy.arange(0,100,0.1)
y0 = [500,120]
sim = spint.odeint(func=Ros_Mac_Sim,y0=y0,t=times,args=params)
simdf = pandas.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a1 = ggplot(simdf,aes(x="t",y="H"))+geom_line(color="black",size=1.5)+ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="blue",size=1.5)+theme_classic()
print(a1)

#Simulation 15: 
params = (0.8,0.001,5,400,0.07,0.2) #(b,a,w,d,e,s) | Carrying Capacity of 1000
times = numpy.arange(0,100,0.1)
y0 = [500,120]
sim = spint.odeint(func=Ros_Mac_Sim,y0=y0,t=times,args=params)
simdf = pandas.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a2 = ggplot(simdf,aes(x="t",y="H"))+geom_line(color="black",size=1.5)+ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="blue",size=1.5)+theme_classic()
print(a2)

#Simulation 16:
params = (0.8,0.00067,5,400,0.07,0.2) #(b,a,w,d,e,s) | Carrying Capacity of 1500
times = numpy.arange(0,100,0.1)
y0 = [500,120]
sim = spint.odeint(func=Ros_Mac_Sim,y0=y0,t=times,args=params)
simdf = pandas.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a3 = ggplot(simdf,aes(x="t",y="H"))+geom_line(color="black",size=1.5)+ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="blue",size=1.5)+theme_classic()
print(a3)

#Simulation 17: 
params = (0.8,0.0005,5,400,0.07,0.2) #(b,a,w,d,e,s) | Carrying Capacity of 2000
times = numpy.arange(0,100,0.1)
y0 = [500,120]
sim = spint.odeint(func=Ros_Mac_Sim,y0=y0,t=times,args=params)
simdf = pandas.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a4 = ggplot(simdf,aes(x="t",y="H"))+geom_line(color="black",size=1.5)+ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="blue",size=1.5)+theme_classic()
print(a4)