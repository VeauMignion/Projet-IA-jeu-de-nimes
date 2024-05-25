#chercheur de diviseur
from math import sqrt
import numpy as np
from matplotlib import pyplot as plt
import sys



#zone mémoire
Lnbpremiers=[]
Lnbpremiers.append(1)

def charger():
    with open('stokage.txt', 'rb') as e:
        premiersarr = np.load(e)
    Lnbpremiers=[]
    for i in range(0,len(premiersarr)):
        Lnbpremiers.append(premiersarr[i])
    return Lnbpremiers

def enregistrement(Lnbpremiers):
    with open('stokage.txt', 'wb') as e:
        np.save(e, np.array(Lnbpremiers))

def reset():
    Lnbpremiers=[]
    Lnbpremiers.append(1)
    enregistrement(Lnbpremiers)

#trouver les diviseurs
def prodiviseur(nb):
    Ldiviseurs=[]
    autrecotedivi=[]
    maxatest=int(sqrt(nb))
    i=1
    while i<=maxatest:
        nbtesté=i
        if nb%nbtesté==0:
            Ldiviseurs.append(nbtesté)
            if nb/nbtesté!=nbtesté:
                autrecotedivi.append(int(nb/nbtesté))
        i=i+1
    for a in range(1,len(autrecotedivi)+1):
        Ldiviseurs.append(autrecotedivi[len(autrecotedivi)-a])
    return len(Ldiviseurs),Ldiviseurs


#trouver des nombres premiers
def cherchpremiers(nbatest):
    nbptesté=Lnbpremiers[len(Lnbpremiers)-1]+1
    début=nbptesté
    for nbptesté in range(début,début+nbatest):
        nbdivi,balec=prodiviseur(nbptesté)
        if nbdivi==2:
            Lnbpremiers.append(nbptesté)
    return Lnbpremiers

#décomposer en nombres premiers
def décomposeur(nb):
    ind=1
    decomposition=[]
    while nb>1:
        if nb%Lnbpremiers[ind]==0:
            decomposition.append(Lnbpremiers[ind])
            nb=int(nb/Lnbpremiers[ind])
        else:
            ind=ind+1
    return decomposition


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
er=input("besoin de setup(oui/non)")
if er=="oui":
    reset()
Lnbpremiers=charger()




def main(Lnbpremiers):
    aa=input("[afficher] la liste, [tester] un nombre, gérer la [memoire]?")
    if aa=="afficher":
        print(Lnbpremiers)
    if aa=="tester":
        ab=int(input("chercher les diviseurs de quel nombre "))
        a,b=prodiviseur(ab)
        c=décomposeur(ab)
        print("nombre de diviseurs",a)
        print("liste des diviseurs",b)
        print("décomposition en nombres premiers",c)
    if aa=="memoire":
        ac=input("charger,reset ou augmenter?")
        if ac=="charger":
            charger()
        if ac=="reset":
            reset()
        if ac=="augmenter":
            ad=int(input("essayer combien de nombres?"))
            Lnbpremiers=cherchpremiers(ad)
            enregistrement(Lnbpremiers)
    ae=input("continuer(oui/non)?")
    if ae=="oui":
        main(Lnbpremiers)

main(Lnbpremiers)