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

def Lot_Vol_Sim(y,t0,b,a,e,s):
    
    H = y[0]
    P = y[1]
    
    dH_dt = b * H - a * P * H
    dP_dt = e * a * P * H - s * P
    
    return [dH_dt,dP_dt]

#Trial One - Given Parameters
#b = 0.5; a = 0.02; e = 0.1; s = 0.2; H0 = 25; P0 = 5
times = range(0,100) #Passed as t0
y0=[25,5] #Passed as H and P, respectively
params = (0.5,0.02,0.1,0.2) #Passed as (b,a,e,s)
#Running the simulation using scipy integrate
sim = spint.odeint(func=Lot_Vol_Sim,y0=y0,t=times,args=params)
#Creating a dataframe
simdf=pd.DataFrame({"t":times,"H":sim[:,0],"P":sim[:,1]})
a=ggplot(simdf,aes(x="t",y="H"))+geom_line()+ylab("Population")+geom_line(simdf,aes(x="t",y="P"),color="red")+theme_classic()
print(a)

#Trial 2 - Doubling b, a, P; Halving e, s, H
#Should run without major problems
times = range(0,100)
y0 = [12,10] #Passed as H and P, respectively
params = (1,0.04,0.05,0.1) #Passed as (b,a,e,s)
sim2 = spint.odeint(func=Lot_Vol_Sim,y0=y0,t=times,args=params)
simdf2=pd.DataFrame({"t":times,"H":sim2[:,0],"P":sim2[:,1]})
b=ggplot(simdf2,aes(x="t",y="H"))+geom_line()+ylab("Population")+geom_line(simdf2,aes(x="t",y="P"),color="red")+theme_classic()
print(b)

#Trial 3 - 5x b, a, P; 0.2x e,s,H
#Should be observably different
times = range(0,100)
y0=[5,25]
params=(2.5,0.1,0.02,0.04)
sim3=spint.odeint(func=Lot_Vol_Sim,y0=y0,t=times,args=params)
simdf3=pd.DataFrame({"t":times,"H":sim3[:,0],"P":sim3[:,1]})
c=ggplot(simdf3,aes(x="t",y="H"))+geom_line()+ylab("Population")+geom_line(simdf3,aes(x="t",y="P"),color="red")+theme_classic()
print(c)