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
    #H = prey (herbivore), P = predator

    dH_dt = b * H * (1 - a * H) - w * (H / (d + H)) * P
    
    dP_dt = e * w * (H / (d + H)) * P - s * P
    
    return [dH_dt,dP_dt]

#Simulation 1: standard parameters 
#Define parameters
params = (0.8,0.001,5,400,0.07,0.2) #(b,a,w,d,e,s)
times = range(0,100)
#b = prey birth rate 
#a = alpha = intra-specfici competition coefficient = carrying capacity 
#w = maximum predator attack rate 
#d = handling time of predator per prey = how much time predator spends on single prey (catch, digest, etc.)
#e = conversion efficiency of prey to predators 
#s = predator death rate 

#Simulate using odeint
y0 = [500,120] #Passed as H and P, respectively
sim = spint.odeint(func=Ros_Mac_Sim,y0=y0,t=times,args=params)

#Creating a DataFrame
simdf = pandas.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a = ggplot(simdf,aes(x="t",y="H"))+geom_line(color="black",size=1.5)+ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="red",size=1.5)+theme_classic()
print(a)


#Simulation 2: double b (prey birth rate) 
#See Simulation 1 for descritions of variables, etc. 
params = (1.6,0.001,5,400,0.07,0.2) #(b,a,w,d,e,s)
times = range(0,100)
y0=[500,120]
sim = spint.odeint(func=Ros_Mac_Sim,y0=y0,t=times,args=params)
simdf = pandas.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a = ggplot(simdf,aes(x="t",y="H"))+geom_line(color="black",size=1.5) + ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="green",size=1.5)+theme_classic()
print(a)

#Simulation 3: halve b (prey birth rate)
params = (0.4,0.001,5,400,0.07,0.2) #(b,a,w,d,e,s)
times = range(0,100)
y0=[500,120]
sim = spint.odeint(func=Ros_Mac_Sim,y0=y0,t=times,args=params)
simdf = pandas.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a = ggplot(simdf,aes(x="t",y="H"))+geom_line(color="black",size=1.5) + ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="green",size=1.5)+theme_classic()
print(a)

#Simulation 4: triple a (predator attack rate)
params = (0.8,0.002,5,400,0.07,0.2) #(b,a,w,d,e,s)
times = range(0,100)
y0=[500,120]
sim = spint.odeint(func=Ros_Mac_Sim,y0=y0,t=times,args=params)
simdf = pandas.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a = ggplot(simdf,aes(x="t",y="H"))+geom_line(color="black",size=1.5) + ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="blue",size=1.5)+theme_classic()
print(a)

#Simulation 5: halve a (predator attack rate)
params = (0.8,0.0005,5,400,0.07,0.2) #(b,a,w,d,e,s)
times = range(0,100)
y0=[500,120]
sim = spint.odeint(func=Ros_Mac_Sim,y0=y0,t=times,args=params)
simdf = pandas.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a = ggplot(simdf,aes(x="t",y="H"))+geom_line(color="black",size=1.5) + ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="blue",size=1.5)+theme_classic()
print(a)

#Simulation 6: double w
params = (0.8,0.001,10,400,0.07,0.2) #(b,a,w,d,e,s)
times = range(0,100)
y0=[500,120]
sim = spint.odeint(func=Ros_Mac_Sim,y0=y0,t=times,args=params)
simdf = pandas.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a = ggplot(simdf,aes(x="t",y="H"))+geom_line(color="black",size=1.5) + ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="pink",size=1.5)+theme_classic()
print(a)

#Simulation 7: halve w
params = (0.8,0.001,2.5,400,0.07,0.2) #(b,a,w,d,e,s)
times = range(0,100)
y0 = [500,120]
sim = spint.odeint(func=Ros_Mac_Sim,y0=y0,t=times,args=params)
simdf = pandas.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a = ggplot(simdf,aes(x="t",y="H"))+geom_line(color="black",size=1.5)+ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="pink",size=1.5)+theme_classic()
print(a)

#Simulation 8: triple d
params = (0.8,0.001,10,800,0.07,0.2) #(b,a,w,d,e,s)
times = range(0,100)
y0=[500,120]
sim = spint.odeint(func=Ros_Mac_Sim,y0=y0,t=times,args=params)
simdf = pandas.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a = ggplot(simdf,aes(x="t",y="H"))+geom_line(color="black",size=1.5)+ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="orange",size=1.5)+theme_classic()
print(a)

#Simulation 9: halve d
params = (0.8,0.001,10,200,0.07,0.2) #(b,a,w,d,e,s)
times = range(0,100)
y0=[500,120]
sim = spint.odeint(func=Ros_Mac_Sim,y0=y0,t=times,args=params)
simdf = pandas.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a = ggplot(simdf,aes(x="t",y="H"))+geom_line(color="black")+ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="orange",size=1.5)+theme_classic()
print(a)

#Simulation 10: double e
params = (0.8,0.001,10,400,0.14,0.2) #(b,a,w,d,e,s)
times = range(0,100)
y0 = [500,120]
sim = spint.odeint(func=Ros_Mac_Sim,y0=y0,t=times,args=params)
simdf = pandas.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a = ggplot(simdf,aes(x="t",y="H"))+geom_line(color="black",size=1.5)+ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="purple",size=1.5)+theme_classic()
print(a)


#Simulation 11: halve e
params = (0.8,0.001,10,400,0.035,0.2) #(b,a,w,d,e,s)
times = range(0,100)
y0 = [500,120]
sim = spint.odeint(func=Ros_Mac_Sim,y0=y0,t=times,args=params)
simdf = pandas.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a = ggplot(simdf,aes(x="t",y="H"))+geom_line(color="black",size=1.5)+ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="purple",size=1.5)+theme_classic()
print(a)

#Simulation 12: triple s
params = (0.8,0.001,5,400,0.07,0.6) #(b,a,w,d,e,s)
times=range(0,100)
y0 = [500,120]
sim = spint.odeint(func=Ros_Mac_Sim,y0=y0,t=times,args=params)
simdf = pandas.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a = ggplot(simdf,aes(x="t",y="H"))+geom_line(color="black",size=1.5)+ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="magenta",size=1.5)+theme_classic()
print(a)

#Simulation 13: halve s 
params = (0.8,0.001,5,400,0.07,0.1) #(b,a,w,d,e,s)\
times=range(0,100)
y0 = [500,120]
sim = spint.odeint(func=Ros_Mac_Sim,y0=y0,t=times,args=params)
simdf = pandas.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a = ggplot(simdf,aes(x="t",y="H"))+geom_line(color="black",size=1.5)+ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="magenta",size=1.5)+theme_classic()
print(a)


#Paradox of Enrichment 