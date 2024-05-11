#chercheur de diviseur
from math import sqrt
import numpy as np
from matplotlib import pyplot as plt
import sys



#zone mémoire
Lnbpremiers=[]

def enregistrement(Lnbpremiers):
    with open('stokage.txt', 'wb') as e:  #on stocke les listes definissant les IA
        np.save(e, np.array(Lnbpremiers))


def resetIA():
    Lnbpremiers=[]
    enregistrement(Lnbpremiers)


def chargerlistes():
    with open('stokage.txt', 'rb') as e:
        Lnbpremiers = np.load(e)
    return Lnbpremiers



#trouver les diviseurs
def prodiviseur(nb):
    Ldiviseurs=[]
    autrecotedivi=[]
    maxatest=int(sqrt(nb))
    for i in range(1,maxatest+1):
        if nb%i==0:
            Ldiviseurs.append(i)
            autrecotedivi.append()
