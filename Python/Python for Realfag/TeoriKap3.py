import numpy as np


# 3.12 Arrayer

# 3.12.2 Hvordan konvertere lister til arrayer og motsatt

# 3.12.2.1 Konvertering fra liste til array

L = [0.1, 2.3, 4.5, 6.7]
print(L)

A = np.array(L)
print(A)

# 3.12.2.2 Konvertering fra array til liste
L = list(A)
print(L)


# 3.12.3 Lage arrayer med spesiell utforming

# 3.12.3.1 Arrayer med like elemntverdier

A = np.array([])
print(A)

# Array av bare 0-ere
A = np.zeros([3])
print(A)

# Array av bare 1-ere
A = np.ones([3])
print(A)


# Array av bare k-ere
A = np.zeros([3]) + 5.2
print(A)



# 3.12.3.2 Array med fast inkrement mellom elementene
t_start = 0.0
t_stopp = 1.0
Ts = 0.1
n = int((t_stopp - t_start) / Ts) + 1 # int() gir heltall avrundet mot 0.
t = np.linspace(t_start, t_stopp, n)
print(t)

# np.arange() i stedet for np.linspace()?
