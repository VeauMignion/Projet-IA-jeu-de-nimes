#meilleur option monopoly

import random
import numpy as np
from matplotlib import pyplot as plt

plateau=np.array([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]])
Lplato=[]
X=[]
for i in range(0,40):
    Lplato.append(0)
    X.append(i)

for a in range(0,10000):
    position=0
    while position<40:
        reste=position%10
        ligne=int((position-reste)/10)
        plateau[ligne,reste]=plateau[ligne,reste]+1
        Lplato[position]=Lplato[position]+1
        position=position+random.randint(1,6)+random.randint(1,6)
print(plateau)

fig, (ax1) = plt.subplots(1, 1, figsize=(10, 10))

ax1.plot(X,Lplato,'b')
ax1.legend(['probas de tomber sur la case'])
ax1.set_xlabel('x')
ax1.set_ylabel('nombre de passage')
ax1.set_title('la meilleurs stratégie au monopoly')
ax1.grid()

plt.show()
