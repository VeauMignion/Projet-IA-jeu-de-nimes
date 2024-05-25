#modélisation de lancés de dés

import random
import numpy as np
from matplotlib import pyplot as plt
from math import exp, expm1, sqrt, acos, log

P=acos(-1)

#données des lancés
#nombre des faces
faces=8
#nombre de dés lancés
lancés=20
testot=10000

#partie probas théoriques:
#pour 1 dé
esp=(faces+1)/2
var=(faces*faces-1)/12

#pour la somme
esptot=esp*lancés
vartot=var*lancés
ecartot=sqrt(vartot)

#caratéristiques:
maxdés=faces*lancés
mindés=lancés

Llancés=[]
for i in range(0,testot):
    lancé=0
    for a in range(0,lancés):
        lancé=lancé+random.randint(1,faces)
    Llancés.append(lancé)

#tracé de la gaussienne
def gauss(x):
    y=exp(-1*(((x-esptot)**2)/(2*vartot)))*testot/(ecartot*sqrt(2*P))
    return y

pas=0.1
x=mindés
Lx=[]
Lgauss=[]
while x<=maxdés:
    Lx.append(x)
    Lgauss.append(gauss(x))
    x=x+pas




fig, (ax1) = plt.subplots(1, 1, figsize=(10, 10))
ax1.hist(Llancés, range = (mindés, maxdés), bins = (maxdés-mindés+1))
ax1.plot(Lx, Lgauss, "r")
ax1.legend(["modélisation","Lancés aléatoires"])
ax1.set_xlabel("score obtenu")
ax1.set_ylabel("nombre de lancés donnant cette valeur")
ax1.set_title("modélisation gaussienne des lancés de dés")
ax1.grid()
plt.show()
