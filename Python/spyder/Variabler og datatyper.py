# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 19:42:51 2023

@author: Razvan
"""

# Function - Funksjon

import numpy as np

x = 2.0

y = np.sqrt(x)

print(y)


# Method - Metode

L = [0, 1]
L.append(5)



# Tuples - Tupler

T = (1.0, "a")

T1 = (1.0, "a")
T2 = (2.0, "b")

T = T1 + T2

print(T)


(tall1, tekst1) = (1.0, "a")

print(tall1) ; print(tekst1)



# Dictionary

D = {}

D["Lag"] = "Odd"
D["Poeng"] = 100

print(D)