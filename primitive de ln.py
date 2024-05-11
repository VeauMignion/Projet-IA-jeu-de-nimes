import numpy  as np
from matplotlib import pyplot as plt
from math import exp, expm1, sqrt,log

pas=0.0001
xi=0.00001
yi=0
xmax=100

x=xi
y=yi
lny=0
LY=[]
LNY=[]
LX=[]
    
LY.append(y)
LX.append(x)
LNY.append(lny)
while x<xmax:
    lny=log(x)
    y=y+log(x)*pas
    x=x+pas
    LY.append(y)
    LX.append(x)
    LNY.append(lny)



fig, (ax1) = plt.subplots(1, 1, figsize=(10, 10))

#ax1.axis([xi,x,-2,2])
ax1.plot(LX,LY,'b')
ax1.plot(LX,LNY,'g')
ax1.legend(['primitive estimée','logarithime népérien'])
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('graphique proche de la primitive')
ax1.grid()

plt.show()