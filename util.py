# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 10:40:12 2025

@author: CyclohexAnon
"""

import numpy as np

def parse_reactions(text):
    substances = []
    for i in text.split("\n"):
        for j in i.replace(" = ", " + ").split(" + "):
            if " " in j:
                k = j.split(" ")
                if k[1] not in substances:
                    substances += [k[1]]
            else:
                if j not in substances:
                    substances += [j]
    
    rec = len(text.split("\n"))
    stoic = np.zeros((rec, len(substances)), dtype="float")
    
    for i in range(rec):
        a = text.split("\n")[i].split(" = ")
        #a[0] = educts, a[1] = products
        
        for j in a[0].split(" + "):
            if " " in j:
                k = j.split(" ")           
                z = substances.index(k[1])
                stoic[i, z] = -int(k[0])
            else:
                z = substances.index(j)
                stoic[i, z] = -1
        for j in a[1].split(" + "):
            if " " in j:
                k = j.split(" ")           
                z = substances.index(k[1])
                stoic[i, z] = int(k[0])
            else:
                z = substances.index(j)
                stoic[i, z] = 1
    return(stoic, substances)