#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 10:52:17 2018

@author: Mac
"""

import pandas as pd
import scipy
import scipy.integrate as spint
from plotnine import *
import numpy as np

#H - Herbivore Birth Rate
#P - Predator Attack Rate
#b - Prey Birth Rate
#a - Predator Death Rate
#e - Conversion efficiency of prey to predators
#s - Predator Death Rate

def Lot_Vol_Sim(y,t0,b,a,e,s):
    
    H = y[0]
    P = y[1]
    
    dH_dt = b * H - a * P * H
    dP_dt = e * a * P * H - s * P
    
    return [dH_dt,dP_dt]

#Trial 1 - Given Parameters
#b = 0.5; a = 0.02; e = 0.1; s = 0.2; H0 = 25; P0 = 5
times = np.arange(0,100,0.1) #Passed as t0
y0=[25,5] #Passed as H and P, respectively
params = (0.5,0.02,0.1,0.2) #Passed as (b,a,e,s)
#Running the simulation using scipy integrate
sim = spint.odeint(func=Lot_Vol_Sim,y0=y0,t=times,args=params)
#Creating a dataframe
simdf=pd.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
max_df=(max(simdf.H))
print(max_df)
a=ggplot(simdf,aes(x="t",y="H"))+geom_line()+ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="red")+theme_classic()
print(a)
print("Original Parameters")


#Trial 2 - Doubling P
times = np.arange(0,100,0.1)
y0 = [25,10] #Passed as H and P, respectively
params = (0.5,0.02,0.1,0.2) #Passed as (b,a,e,s)
sim2 = spint.odeint(func=Lot_Vol_Sim,y0=y0,t=times,args=params)
simdf2=pd.DataFrame({"t":times,"H":sim2[:,0],"P":sim2[:,1]})
b=ggplot(simdf2,aes(x="t",y="H"))+geom_line()+ylab("Population")+geom_line(simdf2,aes(x="t",y="P"),color="red")+theme_classic()
print(b)
print("P Doubled")

#Trial 3 - .5x P
times = np.arange(0,100,0.1)
y0=[25,2.5]
params=(0.5,0.02,0.1,0.2)
sim3=spint.odeint(func=Lot_Vol_Sim,y0=y0,t=times,args=params)
simdf3=pd.DataFrame({"t":times,"H":sim3[:,0],"P":sim3[:,1]})
c=ggplot(simdf3,aes(x="t",y="H"))+geom_line()+ylab("Population")+geom_line(simdf3,aes(x="t",y="P"),color="red")+theme_classic()
print(c)
print("P Halved")


#Trial 4 - Doubling H
times = np.arange(0,100,0.1)
y0 = [50,5] #Passed as H and P, respectively
params = (0.5,0.02,0.1,0.2) #Passed as (b,a,e,s)
sim2 = spint.odeint(func=Lot_Vol_Sim,y0=y0,t=times,args=params)
simdf2=pd.DataFrame({"t":times,"H":sim2[:,0],"P":sim2[:,1]})
d=ggplot(simdf2,aes(x="t",y="H"))+geom_line()+ylab("Population")+geom_line(simdf2,aes(x="t",y="P"),color="red")+theme_classic()
print(d)
print("H Doubled")

#Trial 5 - Halving H
times = np.arange(0,100,0.1)
y0=[12.5,5] #Passed as H and P, respectively
params = (0.5,0.02,0.1,0.2) #Passed as (b,a,e,s)
#Running the simulation using scipy integrate
sim = spint.odeint(func=Lot_Vol_Sim,y0=y0,t=times,args=params)
#Creating a dataframe
simdf=pd.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a=ggplot(simdf,aes(x="t",y="H"))+geom_line()+ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="red")+theme_classic()
print(a)
print("H Halved")

#Trial 6 - b * 2
times = np.arange(0,100,0.1)
y0 = [25,5] #Passed as H and P, respectively
params = (1,0.02,0.1,0.2) #Passed as (b,a,e,s)
sim2 = spint.odeint(func=Lot_Vol_Sim,y0=y0,t=times,args=params)
simdf2=pd.DataFrame({"t":times,"H":sim2[:,0],"P":sim2[:,1]})
e=ggplot(simdf2,aes(x="t",y="H"))+geom_line()+ylab("Population")+geom_line(simdf2,aes(x="t",y="P"),color="red")+theme_classic()
print(e)
print("b Doubled")

#Trial 7 - b * .5
times = np.arange(0,100,0.1)
y0=[25,5] #Passed as H and P, respectively
params = (0.25,0.02,0.1,0.2) #Passed as (b,a,e,s)
#Running the simulation using scipy integrate
sim = spint.odeint(func=Lot_Vol_Sim,y0=y0,t=times,args=params)
#Creating a dataframe
simdf=pd.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a=ggplot(simdf,aes(x="t",y="H"))+geom_line()+ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="red")+theme_classic()
print(a)
print("b Halved")

#Trial 8 - a * 2
times = np.arange(0,100,0.1)
y0=[25,5] #Passed as H and P, respectively
params = (0.5,0.04,0.1,0.2) #Passed as (b,a,e,s)
#Running the simulation using scipy integrate
sim = spint.odeint(func=Lot_Vol_Sim,y0=y0,t=times,args=params)
#Creating a dataframe
simdf=pd.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a=ggplot(simdf,aes(x="t",y="H"))+geom_line()+ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="red")+theme_classic()
print(a)
print("a Doubled")

#Trial 9 - a * .5
times = np.arange(0,100,0.1)
y0=[25,5] #Passed as H and P, respectively
params = (0.5,0.01,0.1,0.2) #Passed as (b,a,e,s)
#Running the simulation using scipy integrate
sim = spint.odeint(func=Lot_Vol_Sim,y0=y0,t=times,args=params)
#Creating a dataframe
simdf=pd.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a=ggplot(simdf,aes(x="t",y="H"))+geom_line()+ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="red")+theme_classic()
print(a)
print("a Halved")

#Trial 10 - e * 2
times = np.arange(0,100,0.1)
y0=[25,5] #Passed as H and P, respectively
params = (0.5,0.02,0.2,0.2) #Passed as (b,a,e,s)
#Running the simulation using scipy integrate
sim = spint.odeint(func=Lot_Vol_Sim,y0=y0,t=times,args=params)
#Creating a dataframe
simdf=pd.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a=ggplot(simdf,aes(x="t",y="H"))+geom_line()+ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="red")+theme_classic()
print(a)
print("e Doubled")

#Trail 11 - e * .5
times = np.arange(0,100,0.1)
y0=[25,5] #Passed as H and P, respectively
params = (0.5,0.02,0.05,0.2) #Passed as (b,a,e,s)
#Running the simulation using scipy integrate
sim = spint.odeint(func=Lot_Vol_Sim,y0=y0,t=times,args=params)
#Creating a dataframe
simdf=pd.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a=ggplot(simdf,aes(x="t",y="H"))+geom_line()+ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="red")+theme_classic()
print(a)
print("e Halved")

#Trial 12 - s * 2
times = np.arange(0,100,0.1)
y0=[25,5] #Passed as H and P, respectively
params = (0.5,0.02,0.1,0.4) #Passed as (b,a,e,s)
#Running the simulation using scipy integrate
sim = spint.odeint(func=Lot_Vol_Sim,y0=y0,t=times,args=params)
#Creating a dataframe
simdf=pd.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a=ggplot(simdf,aes(x="t",y="H"))+geom_line()+ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="red")+theme_classic()
print(a)
print("s Doubled")

#Trial 13 - s * .5
times = np.arange(0,100,0.1)
y0=[25,5] #Passed as H and P, respectively
params = (0.5,0.02,0.1,0.1) #Passed as (b,a,e,s)
#Running the simulation using scipy integrate
sim = spint.odeint(func=Lot_Vol_Sim,y0=y0,t=times,args=params)
#Creating a dataframe
simdf=pd.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a=ggplot(simdf,aes(x="t",y="H"))+geom_line()+ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="red")+theme_classic()
print(a)
print("s Halved")