# Créé par HUMBERT, le 28/05/2023 en Python 3.7
#importations nécéssaires
import random


#setup des valeurs
nbBatons = 21               #nombre de bâtons du jeu
nbcalcul = 90            #nombres totaux aléatoires pour chaque choix
nbB = nbBatons
lose = 0
randomtire = 0
nbentrainements = 0       #nombre de matchs joué par les IA
vicIA1 = 0
vicIA2 = 0
z = 0
w = 0
f = 5          #facteur de modification des Ia


#reset des IA
if 0==1:
    IA1tt = []
    IA1tu = []
    IA2tt = []
    IA2tu = []
    for i in range (0,nbBatons):
        IA1tt.append = (60)          #si nb random supérieur à cette position, alors l'AI1 tire 3 bâtons
        IA1tu.append = (30)          #si nb random inférieur à cette position, alors l'AI1 tire 1 bâton
        IA2tt.append = (60)          #si nb random supérieur à cette position, alors l'AI2 tire 3 bâtons
        IA2tu.append = (30)          #si nb random inférieur à cette position, alors l'AI2 tire 1 bâton


#jeu
def jeu ():
    nbB = nbBatons
    coupjouesIA1 = []                    #à quels nombres de batons l'IA1 à fait ses coups
    coupjouesIA2 = []                    #à quels nombres de batons l'IA2 à fait ses coups
    numcoupjouesIA1 = []                 #combien de bâtons l'IA1 à retiré à chaqun de ses coups
    numcoupjouesIA2 = []                 #combien de bâtons l'IA2 à retiré à chaqun de ses coups
    if random.random() >= 0.5:
        while lose == 0:
            if nbB <= 0:
                if lose == 0:
                    lose = 1
                return (1,0)
            else:
                randomtire = random.randint(0,90)
                if randomtire >= IA1tt[nbB]:
                    numcoupjouesIA1.append(nbB)
                    coupjouesIA1.append(3)
                    nbB = nbB-3
                if randomtire <= IA1tu[nbB]:
                    numcoupjouesIA1.append(nbB)
                    coupjouesIA1.append(1)
                    nbB = nbB-1
                else:
                    numcoupjouesIA1.append(nbB)
                    coupjouesIA1.append(2)
                    nbB = nbB-2
            if nbB <= 0:
                if lose == 0:
                    lose = 1
                return (0,1)
            else:
                randomtire = random.randint(0,90)
                if randomtire >= IA2tt[nbB]:
                    numcoupjouesIA2.append(nbB)
                    coupjouesIA2.append(3)
                    nbB = nbB-3
                if randomtire <= IA1tu[nbB]:
                    numcoupjouesIA2.append(nbB)
                    coupjouesIA2.append(1)
                    nbB = nbB-1
                else:
                    numcoupjouesIA2.append(nbB)
                    coupjouesIA2.append(2)
                    nbB = nbB-2
    else:
        while lose == 0:
            if nbB <= 0:
                if lose == 0:
                    lose = 1
                return (1,0)
            else:
                randomtire = random.randint(0,90)
                if randomtire >= IA1tt[nbB]:
                    numcoupjouesIA1.append(nbB)
                    coupjouesIA1.append(3)
                    nbB = nbB-3
                if randomtire <= IA1tu[nbB]:
                    numcoupjouesIA1.append(nbB)
                    coupjouesIA1.append(1)
                    nbB = nbB-1
                else:
                    numcoupjouesIA1.append(nbB)
                    coupjouesIA1.append(2)
                    nbB = nbB-2
            if nbB <= 0:
                if lose == 0:
                    lose = 1
                return (0,1)
            else:
                randomtire = random.randint(0,90)
                if randomtire >= IA2tt[nbB]:
                    numcoupjouesIA2.append(nbB)
                    coupjouesIA2.append(3)
                    nbB = nbB-3
                if randomtire <= IA1tu[nbB]:
                    numcoupjouesIA2.append(nbB)
                    coupjouesIA2.append(1)
                    nbB = nbB-1
                else:
                    numcoupjouesIA2.append(nbB)
                    coupjouesIA2.append(2)
                    nbB = nbB-2




#jeu en boucle et entrainement des IA l'une contre l'autre
for i in range (0,nbentrainements):
    vicIA1,vicIA2 = jeu()
    if vicIA1==1:
        z = 0
        while z <= len(numcoupjouesIA1):
            if coupjouesIA1(z) == 1:
                if IA1tu[numcoupjouesIA1(z)] <= IA1tt[numcoupjouesIA1(z)]-5:
                    if IA1tt[numcoupjouesIA1(z)]+5 <= 90:
                        IA1tu[numcoupjouesIA1(z)] = IA1tu[numcoupjouesIA1(z)]+10
                        IA1tt[numcoupjouesIA1(z)] = IA1tt[numcoupjouesIA1(z)]+5
                    else:
                        IA1tt[numcoupjouesIA1(z)] = 90
                else:
                    IA1tu[numcoupjouesIA1(z)] = IA1tt[numcoupjouesIA1(z)]-5
            if coupjouesIA1(z) == 2:
                if IA1tu[numcoupjouesIA1(z)] >= 5:
                    if IA1tt[numcoupjouesIA1(z)]+5 <= 90:
                        IA1tu[numcoupjouesIA1(z)] = IA1tu[numcoupjouesIA1(z)]-5
                        IA1tt[numcoupjouesIA1(z)] = IA1tt[numcoupjouesIA1(z)]+5
                    else:
                        IA1tt[numcoupjouesIA1(z)] = 90
                else:
                    IA1tu[numcoupjouesIA1(z)] = 0
            if coupjouesIA1(z) == 3:
                if IA1tu[numcoupjouesIA1(z)] <= IA1tt[numcoupjouesIA1(z)]-5:
                    if IA1tu[numcoupjouesIA1(z)]-5 <= 0:
                        IA1tu[numcoupjouesIA1(z)] = IA1tu[numcoupjouesIA1(z)]-5
                        IA1tt[numcoupjouesIA1(z)] = IA1tt[numcoupjouesIA1(z)]-10
                    else:
                        IA1tt[numcoupjouesIA1(z)] = 85
                else:
                    IA1tu[numcoupjouesIA1(z)] = IA1tt[numcoupjouesIA1(z)]