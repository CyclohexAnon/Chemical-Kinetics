# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 13:25:36 2025

@author: CyclohexAnon
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import time as ti
import util

# User input
stoic, substances = util.parse_reactions("B + A = C\nC + A = D\nD + A = E")
ratec = np.array([3e-4, 2e-4, 1e-4], dtype='float')  # rate constants
initial_concentrations = np.array([1, 2.0, 0, 0, 0], dtype='float')  # initial concentrations
t_span = (0, 50000)
t_eval = np.linspace(*t_span, 1000)  # save 1000 points for plotting

# Precompute stoichiometry terms
reactant_mask = stoic < 0
neg_stoic = -stoic * reactant_mask  # only reactants get powered

def kinetics(t, y):
    # y: concentrations at time t
    y_power = y ** neg_stoic  # shape: (reactions, species)
    rates = ratec * np.prod(y_power, axis=1)
    return rates @ stoic  # shape: (species,)

start = ti.time()
sol = solve_ivp(kinetics, t_span, initial_concentrations, t_eval=t_eval, method='LSODA')  # or 'RK45', 'BDF'
end = ti.time()
print(f"Completed in {end-start:.5f} s")
print("-"*20)
print("Final concentrations:")
for i in range(sol.y.shape[0]):
    print(f"{substances[i]}: {sol.y[i,-1]:.10f}")
    
for i in range(sol.y.shape[0]):
    plt.plot(sol.t, sol.y[i], label=substances[i])
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.legend()
plt.show()
