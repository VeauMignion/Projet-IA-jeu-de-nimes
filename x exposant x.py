#crée par HUMBERT le 27/02
#x^x

import numpy  as np
from matplotlib import pyplot as plt
from math import exp, expm1, sqrt,log

def f(x):
    if x>0:
        a=x**x
    else:
        if x==0:
            a=1
        else:
            a=x**x
    print(x)
    print(a)
    print()
    listreely.append(a.real)
    listimy.append(a.imag)
    return abs(a)

pas=0.01
xi=-10
xfin=0
listys=[]
listxs=[]
listreely=[]
listimy=[]
arr=round(1-log(pas))
print(arr)

x=xi
while  x<=xfin:
    listys.append(f(x))
    listxs.append(x)
    x=x+pas
    x=round(x,arr)

print("@@@@@@@@@@@@@@@@@@@")
print((-0.2)**(-0.2))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 10))

ax1.axis([xi,x,-2,2])
ax1.plot(listxs,listys,'b')
ax1.plot(listxs,listreely,'g')
ax1.plot(listxs,listimy,'pink')
ax1.legend(['valeur absolue de x^x','valeur réelle de x^x','valeur imaginaire de x^x'])
ax1.set_xlabel('x')
ax1.set_ylabel('x^x')
ax1.set_title('graphique y=x^x')
ax1.grid()



ax2.axis([-1.5,1.5,-1.5,1.5])
ax2.plot(listreely,listimy,'black')
ax2.legend(['ensemble graphique des nombres complexes'])
ax2.set_xlabel('partie réelle')
ax2.set_ylabel('partie imaginaire')
ax2.set_title('ensemble graphique des nombres complexes')
ax2.grid()

plt.show()


