import matplotlib.pyplot as plt
from numpy import arange, meshgrid, sqrt
import random
import matplotlib.patches as mpatches
c=1 #3*10**8 

#radio=10
v=0.6*c
radio=float(input("Ingrese radio de círculo: "))

delta = 0.025
x, y = meshgrid(arange(-radio*5, radio/2, delta),arange(-radio, radio, delta))
chars = '0123456789ABCDEF'
patches=[]
j=0
random.seed(0)
col=['#'+''.join(random.sample(chars,6)) for i in range(11)]      #para distintos colores
for i in range(0,11,1):
  t=-1
  lam=1/sqrt(1-(v/c)**2)
  plt.contour(x, y,x/v+sqrt(x**2+y**2)/c+sqrt(radio**2-y**2)/(lam*c)-t, [0], colors=col[10-j])
  plt.contour(x, y,x/v+sqrt(x**2+y**2)/c-sqrt(radio**2-y**2)/(lam*c)-t, [0], colors=col[10-j])
  patches.append(mpatches.Patch(color=col[j], label='v='+str(round(v,2))+"c"))
  j+=1
  v+=0.03*c

plt.title("Círculo con movimiento en x\n(variando v de 0.6c a 0.9c)")
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.legend(handles=patches)
plt.show()