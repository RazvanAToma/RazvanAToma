#Fasit på ekstraoppgave: Hvor mange kilo startet hen med?.
import numpy as np
import matplotlib.pyplot as plt
#Funksjon som gir hvor mange prosent som er igjen av stoffet etter t tid.
def p(t,h,m):
    return  m*0.5**(t/h)
 
#Be om verdier for t og h.
m = float(input("Hvor mange kilo av grunnstoffet starter du med? "))
t = np.linspace(0, float(input("Hvor lang tid skal gå? ")), 1000)
h = float(input("Hva er halveringstida? "))
 
#Lag graf.
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.grid(True)
 
x = t
y = p(t,h,m)
 
ax1.plot(x,y)
plt.show()