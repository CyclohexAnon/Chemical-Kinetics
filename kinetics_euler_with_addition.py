# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 10:53:25 2025

@author: CyclohexAnon
"""

import numpy as np
import matplotlib.pyplot as plt
import util

stoic, substances = util.parse_reactions("B + A = C\nC + A = D\nD + A = E")
ratec = np.array([3e-4, 2e-4, 1e-4], dtype='float') #rate constants for all reactions
conc = np.array([1,0,0,0,0],dtype='float') #concentrations for all substances (order of appearance)

addition_amount = np.array([0,2,0,0,0],dtype='float')
addition_time = 10000

veloc = np.copy(ratec)
time_total = 50000
dt = 10
steps = int(time_total/dt)

nothing = np.zeros(addition_amount.shape,dtype='float')

def addition(t):
    if t < addition_time:
        return addition_amount * dt/addition_time 
    else:
        return nothing

time = np.arange(0, time_total, dt)

concentrations = np.zeros((steps, len(conc)), dtype="float")

for t in range(steps):
    conc += addition(t*dt)
    
    for i in range(stoic.shape[0]):
        veloc[i] = ratec[i]
        for j in range(stoic.shape[1]):        
            if stoic[i,j] < 0:
                veloc[i] *= conc[j]**(-stoic[i,j])
                
    conc = conc + dt*np.dot(veloc, stoic)
    concentrations[t,:] = conc

for i in range(5):
    plt.plot(time, concentrations[:,i], label = substances[i])
plt.legend()

#plt.xlim([0, time_total])
#plt.ylim([0, 2])

print(concentrations[-1,:])