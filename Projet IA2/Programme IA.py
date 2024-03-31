#Crée par paul HUMBERT, le 28/03/24, Refonte d'un projet commencé le 28/05/2023 qui n'avait pas aboutit:
#Programme d'IA qui jouent au jeu de nîmes
#imports
import random
import numpy as np
from matplotlib import pyplot as plt


#paramêtres du jeu de Nîmes
nbB=21

#facteur des IAs:
y=0 #capacité des IA a tester de nouvelles choses, si =0, l'IA pourra abandonner totalement une possibilité
f=1 #vitesse à laquelle une IA change après une victoire ou une défaite

#Les IAs se résument à 3 suites de chiffres de 21 termes chaqunes qui correspondent à, pour chaque nombre
#de bâtons restant, la probabilité que l'IA en enlève 1, 2 ou 3

def resetIA():        #on reset les listes des IA (dangereux)
    IA1_t1=[]
    IA1_t2=[]
    IA1_t3=[]
    IA2_t1=[]
    IA2_t2=[]
    IA2_t3=[]
    a=0
    while a<nbB:
        IA1_t1.append(30)
        IA1_t2.append(30)
        IA1_t3.append(30)
        IA2_t1.append(30)
        IA2_t2.append(30)
        IA2_t3.append(30)
        a=a+1
    return IA1_t1,IA1_t2,IA1_t3,IA2_t1,IA2_t2,IA2_t3

def enregistrementIA(IA1_t1,IA1_t2,IA1_t3,IA2_t1,IA2_t2,IA2_t3):
    with open('stokage.txt', 'wb') as e:  #on stocke les listes definissant les IA
        np.save(e, np.array(IA1_t1))
        np.save(e, np.array(IA1_t2))
        np.save(e, np.array(IA1_t3))
        np.save(e, np.array(IA2_t1))
        np.save(e, np.array(IA2_t2))
        np.save(e, np.array(IA2_t3))

IA1_t1,IA1_t2,IA1_t3,IA2_t1,IA2_t2,IA2_t3=resetIA()
enregistrementIA(IA1_t1,IA1_t2,IA1_t3,IA2_t1,IA2_t2,IA2_t3)

#Rechargement des données
with open('stokage.txt', 'rb') as e:     #on charge les listes des IA
    IA1_t1 = np.load(e)
    IA1_t2 = np.load(e)
    IA1_t3 = np.load(e)
    IA2_t1 = np.load(e)
    IA2_t2 = np.load(e)
    IA2_t3 = np.load(e)

def entrainement():     #fonction que l'on va faire en boucle pour entrainer les IA
    nbB=21
    LPcoupsIA1=[]    #listes dans lequelles on va enregistrer les coups joués avec un P=position du coup,  
    LcoupsIA1=[]     #sans=nombre de batons enlevés
    LPcoupsIA2=[]
    LcoupsIA2=[]
    if random.randint(0,1)>=0.5:     #On choisit quelle IA commence
        IAplay=1
    else:
        IAplay=0
    while nbB>0:
        nbBf=nbB-1
        nbBenleve=IA_joue_batons(IAplay,nbB)
        if IAplay==1:                             #on note les coups joués dans les listes
            LPcoupsIA1.append(nbBf)
            LcoupsIA1.append(nbBenleve)
            IAplay=0
        else:
            LPcoupsIA2.append(nbBf)
            LcoupsIA2.append(nbBenleve)
            IAplay=1
        nbB=nbB-nbBenleve
    win=IAplay                                        #IA qui a gagné
    rapportentrainement(win,LPcoupsIA1,LcoupsIA1,LPcoupsIA2,LcoupsIA2)
    apprentissage(LPcoupsIA1,LcoupsIA1,LPcoupsIA2,LcoupsIA2,win)


def rapportentrainement(win,LPcoupsIA1,LcoupsIA1,LPcoupsIA2,LcoupsIA2):
    print(win)
    print()
    print("coups de l'IA1")
    print(LPcoupsIA1,"     ",LcoupsIA1)
    print("coups de l'IA2")
    print(LPcoupsIA2,"     ",LcoupsIA2)
    print()
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print()
    print()




def IA_joue_batons(IAplay,nbB):     #chaque IA effectue son coup
    nbBf=nbB-1
    if IAplay==1:
        totprobas=IA1_t1[nbBf]+IA1_t2[nbBf]+IA1_t3[nbBf]
        nbchoisi=random.randint(0,totprobas)
        if nbchoisi<=IA1_t1[nbBf]:
            nbBenleve=1
        else:
            if nbchoisi<=IA1_t1[nbBf]+IA1_t2[nbBf]:
                nbBenleve=2
            else:
                nbBenleve=3
    else:
        totprobas=IA2_t1[nbBf]+IA2_t2[nbBf]+IA2_t3[nbBf]
        nbchoisi=random.randint(0,totprobas)
        if nbchoisi<=IA2_t1[nbBf]:
            nbBenleve=1
        else:
            if nbchoisi<=IA2_t1[nbBf]+IA2_t2[nbBf]:
                nbBenleve=2
            else:
                nbBenleve=3
    return nbBenleve

def apprentissage(LPcoupsIA1,LcoupsIA1,LPcoupsIA2,LcoupsIA2,win):
    a=0
    fm=f
    if win==0:
        fm=(-1)*f                         #on ajuste le modifier pour qu'il pénalise l'IA si elle a perdu
    while a<len(LPcoupsIA1):
        if LcoupsIA1[a]==1:
            IA1_t1[LPcoupsIA1[a]]=IA1_t1[LPcoupsIA1[a]]+2*fm
            IA1_t2[LPcoupsIA1[a]]=IA1_t2[LPcoupsIA1[a]]-fm
            IA1_t3[LPcoupsIA1[a]]=IA1_t3[LPcoupsIA1[a]]-fm
        if LcoupsIA1[a]==2:
            IA1_t1[LPcoupsIA1[a]]=IA1_t1[LPcoupsIA1[a]]-fm
            IA1_t2[LPcoupsIA1[a]]=IA1_t2[LPcoupsIA1[a]]+2*fm
            IA1_t3[LPcoupsIA1[a]]=IA1_t3[LPcoupsIA1[a]]-fm
        if LcoupsIA1[a]==3:
            IA1_t1[LPcoupsIA1[a]]=IA1_t1[LPcoupsIA1[a]]-fm
            IA1_t2[LPcoupsIA1[a]]=IA1_t2[LPcoupsIA1[a]]-fm
            IA1_t3[LPcoupsIA1[a]]=IA1_t3[LPcoupsIA1[a]]+2*fm
        checkvariables(LPcoupsIA1[a])
        a=a+1
    fm=f
    if win==1:
        fm=(-1)*f                         #on ajuste le modifier pour qu'il pénalise l'IA si elle a perdu
    while a<len(LPcoupsIA2):
        if LcoupsIA2[a]==1:
            IA2_t1[LPcoupsIA2[a]]=IA2_t1[LPcoupsIA2[a]]+2*fm
            IA2_t2[LPcoupsIA2[a]]=IA2_t2[LPcoupsIA2[a]]-fm
            IA2_t3[LPcoupsIA2[a]]=IA2_t3[LPcoupsIA2[a]]-fm
        if LcoupsIA2[a]==2:
            IA2_t1[LPcoupsIA2[a]]=IA2_t1[LPcoupsIA2[a]]-fm
            IA2_t2[LPcoupsIA2[a]]=IA2_t2[LPcoupsIA2[a]]+2*fm
            IA2_t3[LPcoupsIA2[a]]=IA2_t3[LPcoupsIA2[a]]-fm
        if LcoupsIA2[a]==3:
            IA2_t1[LPcoupsIA2[a]]=IA2_t1[LPcoupsIA2[a]]-fm
            IA2_t2[LPcoupsIA2[a]]=IA2_t2[LPcoupsIA2[a]]-fm
            IA2_t3[LPcoupsIA2[a]]=IA2_t3[LPcoupsIA2[a]]+2*fm
        checkvariables(LPcoupsIA2[a])
        a=a+1


def checkvariables(n):  #n correspond au numéro des termes dont on doit vérifier le cohérence
    n=0
    while n<len(IA1_t1):
        if IA1_t1[n]<y:
            diff=y-IA1_t1[n]
            IA1_t1[n]=y
            if IA1_t2[n]>IA1_t3[n]:
                IA1_t2[n]=IA1_t2[n]-diff
            else:
                IA1_t3[n]=IA1_t3[n]-diff
        if IA1_t2[n]<y:
            diff=y-IA1_t2[n]
            IA1_t2[n]=y
            if IA1_t1[n]>IA1_t3[n]:
                IA1_t1[n]=IA1_t1[n]-diff
            else:
                IA1_t3[n]=IA1_t3[n]-diff
        if IA1_t3[n]<y:
            diff=y-IA1_t3[n]
            IA1_t3[n]=y
            if IA1_t2[n]>IA1_t1[n]:
                IA1_t2[n]=IA1_t2[n]-diff
            else:
                IA1_t1[n]=IA1_t1[n]-diff

        if IA2_t1[n]<y:
            diff=y-IA2_t1[n]
            IA2_t1[n]=y
            if IA2_t2[n]>IA2_t3[n]:
                IA2_t2[n]=IA2_t2[n]-diff
            else:
                IA2_t3[n]=IA2_t3[n]-diff
        if IA2_t2[n]<y:
            diff=y-IA2_t2[n]
            IA2_t2[n]=y
            if IA2_t1[n]>IA2_t3[n]:
                IA2_t1[n]=IA2_t1[n]-diff
            else:
                IA2_t3[n]=IA2_t3[n]-diff
        if IA2_t3[n]<y:
            diff=y-IA2_t3[n]
            IA2_t3[n]=y
            if IA2_t2[n]>IA2_t1[n]:
                IA2_t2[n]=IA2_t2[n]-diff
            else:
                IA2_t1[n]=IA2_t1[n]-diff
        n=n+1


def affichageperf():                            #affiche les choix des IA sous forme d"histogramme
    choixmoy,to21=choixmoyen(1)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 10))
    ax1.hist(donéespourhist(choixmoy),range = (1, 21), bins = 21)
    ax1.legend(["choix moyen de l'IA1"])
    ax1.set_xlabel("nombre de bâtons")
    ax1.set_ylabel("bâtons enlevés")
    ax1.set_title("Performance de l'IA1")
    ax1.grid()
    plt.show()

def choixmoyen(nbIA):
    choixmoy=[]
    to21=[]
    a=0
    if nbIA==1:
        while a<len(IA1_t1):
            choixmoy.append((1*IA1_t1[a]+2*IA1_t2[a]+3*IA1_t3[a])/(IA1_t1[a]+IA1_t2[a]+IA1_t3[a]))
            a=a+1
            to21.append(a)
    else:
        while a<len(IA1_t1):
            choixmoy.append((1*IA2_t1[a]+2*IA2_t2[a]+3*IA2_t3[a])/(IA2_t1[a]+IA2_t2[a]+IA2_t3[a]))
            a=a+1
            to21.append(a)
    return choixmoy,to21

def donéespourhist(choixmoy):
    Lchoixhist=[]
    a=0
    while a<len(choixmoy):
        b=0
        while b<10*choixmoy[a]:
            Lchoixhist.append(a+1)
            b=b+1
        a=a+1
    return Lchoixhist

def affichagemat():
    a=0
    choixmoy,to21=choixmoyen(1)
    print("#############")
    while a<len(IA1_t1):
        somme=IA1_t1[a]+IA1_t2[a]+IA1_t3[a]
        print(a,"   ",somme,"   ",IA1_t1[a],"   ",IA1_t2[a],"   ",IA1_t3[a],"   ",choixmoy[a])
        a=a+1

#############################################################################################################
#############################################################################################################
resetIA()
nbentrainement=1000
a=0
while a<nbentrainement:
    entrainement()
    a=a+1

affichagemat()

affichageperf()
