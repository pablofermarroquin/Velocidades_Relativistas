import matplotlib.pyplot as plt
from numpy import arange, meshgrid, sqrt
import random
import matplotlib.patches as mpatches
c=1 #3*10**8 

#largo=25
v=0.6*c
largo=float(input("Ingrese largo de barra: "))
#v=float(input("Ingrese múltiplo de c para velocidad: "))

delta = 0.025
x, y = meshgrid(arange(-largo*3, 5, delta),arange(0, largo, delta))
chars = '0123456789ABCDEF'
patches=[]
j=0
random.seed(0)
col=['#'+''.join(random.sample(chars,6)) for i in range(11)]      #para distintos colores
for i in range(0,11,1):
  t=-1
  plt.contour(x, y,x/v+sqrt(x**2+y**2)/c-t, [0],  colors=col[j])
  patches.append(mpatches.Patch(color=col[j], label='v='+str(round(v,2))+"c"))
  j+=1
  v+=0.03*c

plt.title("Barra vertical con movimiento en x\n(variando v de 0.6c a 0.9c)")
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.legend(handles=patches)
plt.show()