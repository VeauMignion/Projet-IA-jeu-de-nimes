#Crée par paul HUMBERT, le 28/03/24, Refonte d'un projet commencé le 28/05/2023 qui n'avait pas aboutit:
#Programme d'IA qui jouent au jeu de nîmes
#imports
import random
import numpy as np
from matplotlib import pyplot as plt
import sys


#paramêtres du jeu de Nîmes
nbBi=21
nbB=nbBi

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
    while a<nbBi:
        IA1_t1.append(30)
        IA1_t2.append(30)
        IA1_t3.append(30)
        IA2_t1.append(30)
        IA2_t2.append(30)
        IA2_t3.append(30)
        a=a+1
    return IA1_t1,IA1_t2,IA1_t3,IA2_t1,IA2_t2,IA2_t3

def defIAparfaite():
    IAp_t1=[]
    IAp_t2=[]
    IAp_t3=[]
    a=0
    while a<nbBi:
        if a%4==0:
            IAp_t1.append(30)
            IAp_t2.append(30)
            IAp_t3.append(30)
        if a%4==1:
            IAp_t1.append(90)
            IAp_t2.append(0)
            IAp_t3.append(0)
        if a%4==2:
            IAp_t1.append(0)
            IAp_t2.append(90)
            IAp_t3.append(0)
        if a%4==3:
            IAp_t1.append(0)
            IAp_t2.append(0)
            IAp_t3.append(90)
        a=a+1
    return IAp_t1,IAp_t2,IAp_t3

IAp_t1,IAp_t2,IAp_t3=defIAparfaite()

def enregistrementIA(IA1_t1,IA1_t2,IA1_t3,IA2_t1,IA2_t2,IA2_t3):
    with open('stokage.txt', 'wb') as e:  #on stocke les listes definissant les IA
        np.save(e, np.array(IA1_t1))
        np.save(e, np.array(IA1_t2))
        np.save(e, np.array(IA1_t3))
        np.save(e, np.array(IA2_t1))
        np.save(e, np.array(IA2_t2))
        np.save(e, np.array(IA2_t3))


#Rechargement des données
with open('stokage.txt', 'rb') as e:     #on charge les listes des IA
    IA1_t1 = np.load(e)
    IA1_t2 = np.load(e)
    IA1_t3 = np.load(e)
    IA2_t1 = np.load(e)
    IA2_t2 = np.load(e)
    IA2_t3 = np.load(e)

def chargerlistes():
    with open('stokage.txt', 'rb') as e:     #on charge les listes des IA
        IA1_t1 = np.load(e)
        IA1_t2 = np.load(e)
        IA1_t3 = np.load(e)
        IA2_t1 = np.load(e)
        IA2_t2 = np.load(e)
        IA2_t3 = np.load(e)

def entrainement(d):     #fonction que l'on va faire en boucle pour entrainer les IA
    nbB=nbBi
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
    if d==1:
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


def jeucontreIA(b):
    nbB=nbBi
    if random.randint(0,1)>=0.5:
        playing=1
        print("Joueur commence")
    else:
        playing=0
        print("IA commence")
    while nbB>0:
        joue=0
        if playing==1:
            print("votre tour")
            print(nbB)
            nbBenleve=int(input("nombre de batons que vous voulez enlever(1,2ou3)"))
            if nbBenleve>3:
                nbBenleve=1
            if nbBenleve<1:
                nbBenleve=1
            playing=0
            nbB=nbB-nbBenleve
            joue=1
        if playing==0:
            if joue==0:
                print("tour IA")
                print(nbB)
                nbBenleve=IA_joue_batons(b,nbB)
                playing=1
                nbB=nbB-nbBenleve
        print()
    if playing==1:
        print("vous avez gagné")
    if playing==0:
        print("l'IA à gagné")

def affichagejeu(nbB):
    print("pas encore fait")


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
    a=0
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


def affichageperf(a):                            #affiche les choix des IA sous forme d"histogramme
    choixmoy,to21=choixmoyen(1)
    if a==1:
        fig, (ax1) = plt.subplots(1, 1, figsize=(10, 10))
    else:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 10))
    ax1.hist(donéespourhist(choixmoy),range = (1, nbBi), bins = nbBi)
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
        while a<len(IA2_t1):
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

def affichagemat(b):
    if b==1:
        a=0
        choixmoy,to21=choixmoyen(b)
        print("#############")
        while a<len(IA1_t1):
            somme=IA1_t1[a]+IA1_t2[a]+IA1_t3[a]
            print(a,"   ",somme,"   ",IA1_t1[a],"   ",IA1_t2[a],"   ",IA1_t3[a],"   ",choixmoy[a])
            a=a+1
    if b==2:
        a=0
        choixmoy,to21=choixmoyen(b)
        print("#############")
        while a<len(IA2_t1):
            somme=IA2_t1[a]+IA2_t2[a]+IA2_t3[a]
            print(a,"   ",somme,"   ",IA2_t1[a],"   ",IA2_t2[a],"   ",IA2_t3[a],"   ",choixmoy[a])
            a=a+1

def proxperfect(b):
    dmax=0
    if b==1:
        a=0
        sommedist=0
        while a<len(IA1_t1):
            if a%4==0:
                distu=0
            else:
                distu=abs(IA1_t1[a]-IAp_t1[a])+abs(IA1_t2[a]-IAp_t2[a])+abs(IA1_t3[a]-IAp_t3[a])
                dmax=dmax+180
            sommedist=sommedist+distu
            a=a+1
    else:
        a=0
        sommedist=0
        while a<len(IA2_t1):
            if a%4==0:
                distu=0
            else:
                distu=abs(IA2_t1[a]-IAp_t1[a])+abs(IA2_t2[a]-IAp_t2[a])+abs(IA2_t3[a]-IAp_t3[a])
                dmax=dmax+180
            sommedist=sommedist+distu
            a=a+1
    accurate=100-(sommedist/dmax)*100
    return accurate

#############################################################################################################
#############################################################################################################
print()

def main():
    ad = input("admin ou invite?")
    if ad=="admin":
        print("admin zone")
        mode=input("memoire, entrainement ou infos?")
        if mode=="memoire":
            mem=input("delete, enregistrer ou charger?")
            if mem=="delete":
                IA1_t1,IA1_t2,IA1_t3,IA2_t1,IA2_t2,IA2_t3=resetIA()
                enregistrementIA(IA1_t1,IA1_t2,IA1_t3,IA2_t1,IA2_t2,IA2_t3)
                print("mémoire reset")
            if mem=="enregistrer":
                enregistrementIA(IA1_t1,IA1_t2,IA1_t3,IA2_t1,IA2_t2,IA2_t3)
            if mem=="charger":
                chargerlistes()
        if mode=="entrainement":
            rep=input("nombre d'entrainements?(ou 'avec infos')")
            if rep=="avec infos":
                nbentrainements=int(input("nombre d'entrainements?"))
                a=0
                lisprox=[]
                lisentrai=[]
                while a<nbentrainements:
                    entrainement(1)
                    lisprox.append(proxperfect(1))
                    lisentrai.append(a)
                    a=a+1
                fig, (ax1) = plt.subplots(1, 1, figsize=(10, 10))
                ax1.plot(lisentrai,lisprox,'r')
                ax1.legend(["niveau de l'IA"])
                ax1.set_xlabel("nombre d'entrainement faits")
                ax1.set_ylabel("proximité de la perfection (%)")
                ax1.set_title("Evolution de la performance de l'IA1")
                ax1.grid()
                plt.show()
            else:
                nbentrainements=int(rep)
                a=0
                while a<nbentrainements:
                    entrainement(0)
                    a=a+1
        if mode=="infos":
            print("matrice de l'IA1,    pourcentage de perfection:",proxperfect(1))
            affichagemat(1)
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("matrice de l'IA2,    pourcentage de perfection:",proxperfect(2))
            affichagemat(2)
            affichageperf(1)       
    if ad=="invite":
        print("invité zone")
        vs=int(input("jouer contre quel adversaire?(1ou2)"))
        if vs==0:
            jeucontreIA(vs)
        if vs==1:
            jeucontreIA(vs)
        if vs==2:
            jeucontreIA(vs)
    c=input("taper 0 pour quitter, 1 pour rester")
    if c=="1":
        main()

main()