import matplotlib.pyplot as plt
from numpy import arange, meshgrid, sqrt
import random
import matplotlib.patches as mpatches
c=1 #3*10**8 

#radio=10
#v=0.7*c
radio=float(input("Ingrese radio de círculo: "))
v=float(input("Ingrese múltiplo de c para velocidad: "))

delta = 0.025
x, y = meshgrid(arange(-5*v*radio, radio/2, delta),arange(-radio, radio, delta))
chars = '0123456789ABCDEF'
patches=[]
j=0
random.seed(0)
col=['#'+''.join(random.sample(chars,6)) for i in range(11)]      #para distintos colores
for t in range(-5,6):
  lam=1/sqrt(1-(v/c)**2)
  plt.contour(x, y,x/v+sqrt(x**2+y**2)/c+sqrt(radio**2-y**2)/(lam*c)-t, [0], colors=col[j])
  plt.contour(x, y,x/v+sqrt(x**2+y**2)/c-sqrt(radio**2-y**2)/(lam*c)-t, [0], colors=col[j])
  patches.append(mpatches.Patch(color=col[j], label='t='+str(t)))
  j+=1

plt.title("Círculo con movimiento en x\n(variando t de -5 a 5)")
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.legend(handles=patches)
plt.show()