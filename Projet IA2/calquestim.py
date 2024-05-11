#Estimation du nombre de calques possibles
import numpy as np

totalabs=3**9

estimés=totalabs

def nbase3(nb):
    Lnbbt=[]
    reste=0
    adiv=nb
    for i in range(0,9):
        reste=adiv%3
        adiv=(adiv-reste)/3
        Lnbbt.append(reste)
    return Lnbbt

def dematrix(plato):
    dematrixed=[]
    a=0
    while a<=2:
        b=0
        while b<=2:
            dematrixed.append(plato[a,b])
            b=b+1
        a=a+1
    return dematrixed

def rematrix(Lplato):
    untiers=Lplato[0:3]
    deuxtiers=Lplato[3:6]
    troistiers=Lplato[6:9]
    plato=np.array([untiers,deuxtiers,troistiers])
    return plato

def checkend(plato):
    fin=0
    for i in range(0,3):
        if plato[i,0]>0: #vérification colonnes
            test=plato[i,0]
            if plato[i,1]==plato[i,2]==test:
                fin=1
        if plato[0,i]>0: #vérification lignes
            test=plato[0,i]
            if plato[1,i]==plato[2,i]==test:
                fin=1
    if plato[0,0]==plato[1,1]==plato[2,2]: #les diagonales
        if plato[1,1]>0:
            fin=1
    if plato[2,0]==plato[1,1]==plato[0,2]:
        if plato[1,1]>0:
            fin=1
    if fin==0:
        Lplato=dematrix(plato)
        fullmap=0
        for i in range(0,9):
            if Lplato[i]==0:
                fullmap=1
        if fullmap==0:
            fin=-1
    return fin

def platourne(Lplato,rota):
    platour=[]
    if rota==0:
        platour=Lplato
    if rota==1:
        a=2
        for i in range(0,9):
            platour.append(Lplato[a])
            if a>5:
                a=a-7
            else:
                a=a+3
    if rota==2:
        a=8
        for i in range(0,9):
            platour.append(Lplato[a])
            a=a-1
    if rota==3:
        a=6
        for i in range(0,9):
            platour.append(Lplato[a])
            if a<3:
                a=a+7
            else:
                a=a-3
    if rota==4:
        platour=Lplato
    return platour

Listeabstout=[]

for a in range(0,totalabs):
    print(a)
    Lplato=nbase3(a)
    plato=rematrix(Lplato)
    if checkend(plato)!=0:
        estimés=estimés-1
        print("MAUVAIS")
    else:
        good=0
        for b in range(0,4):
            Lplato=platourne(Lplato,b)
            for c in range(0,len(Listeabstout)):
                if Lplato==Listeabstout[c]:
                    good=1
        if good==1:
            estimés=estimés-1
            print("MAUVAIS")
        else:
            print("GOOD")
            Listeabstout.append(Lplato)

print("le nombre de calques estimés est",estimés)




