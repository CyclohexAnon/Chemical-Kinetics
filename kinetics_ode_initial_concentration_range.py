# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 13:34:29 2025

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
t_span = (0, 1000000)
conc_range = np.linspace(0, 3, 100)
initial_concentrations = lambda c: np.array([1, c, 0, 0, 0], dtype='float')

# Precompute stoichiometry terms
reactant_mask = stoic < 0
neg_stoic = -stoic * reactant_mask  # only reactants get powered

def kinetics(t, y):
    # y: concentrations at time t
    y_power = y ** neg_stoic  # shape: (reactions, species)
    rates = ratec * np.prod(y_power, axis=1)
    return rates @ stoic  # shape: (species,)

t_eval = np.linspace(*t_span, 2)

start = ti.time()
end_concs = np.zeros((len(conc_range), len(substances)))

for k in range(len(conc_range)):
    sol = solve_ivp(kinetics, t_span, initial_concentrations(conc_range[k]), t_eval=t_eval, method='LSODA')  # or 'RK45', 'BDF'
    end_concs[k] = sol.y[:,-1]

end = ti.time()
print(f"Completed in {end-start:.5f} s")

plt.plot(conc_range, end_concs, label=substances)
plt.xlabel("Equivalents of A")
plt.ylabel("Final concentration")
plt.legend()


