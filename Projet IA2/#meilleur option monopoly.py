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

for a in range(0,1000):
    position=0
    while position<40:
        reste=position%10
        ligne=int((position-reste)/10)
        plateau[ligne,reste]=plateau[ligne,reste]+1
        position=position+random.randint(1,6)+random.randint(1,6)
print(plateau)

plt.xlabel('D en (cm)')
plt.ylabel('y en (cm) ')
plt.plot(X,Lplato,"r")
plt.grid
plt.show