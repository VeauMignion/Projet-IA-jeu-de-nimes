import numpy as np
import random
#Idée du 06/04/24
#L'IA se défini par une liste calques: ces calques modélisent une situation que l'IA a affronté 
#(avec un système de coin indenté pour ne pas tenir compte des rotations) et s'accompagnent de probabilitées sur les coups que l'IA peut jouer 
#(qui s'adaptent en fonction des victoires et échecs de l'IA) quand l'IA affronte une situation qu'elle ne connaît pas, 
#elle cherche le calque le plus proche et joue selon ses probabilités (et elle crée un calque de la situation inconnue)
#créé le 13/04/24 par Paul HUMBERT
#pour plus d'infos voir documentation-IA-morpion.pdf



#modifications possibles
modulateur=5
evealéa=5

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
##fonctions de manipulation de la mémoire des IAS
def resetIASdeux(): #on remet à 0 les IAS:
    IA1ncalq=[] #colonne 1 de la matice, liste des numéros des calques
    IA1c1=[]  #colonnes 2 à 10 de la matrice, informations sur les cases que chaque calque doit reconnaitre 
    IA1c2=[]
    IA1c3=[]
    IA1c4=[]
    IA1c5=[]
    IA1c6=[]
    IA1c7=[]
    IA1c8=[]
    IA1c9=[]
    IA1cp1=[] #colonnes 11 à 19 de la matrices, probabilitées des coups à jouer en fonction des cases
    IA1cp2=[]
    IA1cp3=[]
    IA1cp4=[]
    IA1cp5=[]
    IA1cp6=[]
    IA1cp7=[]
    IA1cp8=[]
    IA1cp9=[]

    IA2ncalq=[] #colonne 1 de la matice, liste des numéros des calques
    IA2c1=[]  #colonnes 2 à 10 de la matrice, informations sur les cases que chaque calque doit reconnaitre 
    IA2c2=[]
    IA2c3=[]
    IA2c4=[]
    IA2c5=[]
    IA2c6=[]
    IA2c7=[]
    IA2c8=[]
    IA2c9=[]
    IA2cp1=[] #colonnes 11 à 19 de la matrices, probabilitées des coups à jouer en fonction des cases
    IA2cp2=[]
    IA2cp3=[]
    IA2cp4=[]
    IA2cp5=[]
    IA2cp6=[]
    IA2cp7=[]
    IA2cp8=[]
    IA2cp9=[]
    for i in range(0,2804):
        IA1ncalq.append(0)
        IA1c1.append(0)
        IA1c2.append(0)
        IA1c3.append(0)
        IA1c4.append(0)
        IA1c5.append(0)
        IA1c6.append(0)
        IA1c7.append(0)
        IA1c8.append(0)
        IA1c9.append(0)
        IA1cp1.append(0)
        IA1cp2.append(0)
        IA1cp3.append(0)
        IA1cp4.append(0)
        IA1cp5.append(0)
        IA1cp6.append(0)
        IA1cp7.append(0)
        IA1cp8.append(0)
        IA1cp9.append(0)

        IA2ncalq.append(0)
        IA2c1.append(0)
        IA2c2.append(0)
        IA2c3.append(0)
        IA2c4.append(0)
        IA2c5.append(0)
        IA2c6.append(0)
        IA2c7.append(0)
        IA2c8.append(0)
        IA2c9.append(0)
        IA2cp1.append(0)
        IA2cp2.append(0)
        IA2cp3.append(0)
        IA2cp4.append(0)
        IA2cp5.append(0)
        IA2cp6.append(0)
        IA2cp7.append(0)
        IA2cp8.append(0)
        IA2cp9.append(0)
    IA1=np.array([IA1ncalq,IA1c1,IA1c2,IA1c3,IA1c4,IA1c5,IA1c6,IA1c7,IA1c8,IA1c9,IA1cp1,IA1cp2,IA1cp3,IA1cp4,IA1cp5,IA1cp6,IA1cp7,IA1cp8,IA1cp9])
    IA2=np.array([IA2ncalq,IA2c1,IA2c2,IA2c3,IA2c4,IA2c5,IA2c6,IA2c7,IA2c8,IA2c9,IA2cp1,IA2cp2,IA2cp3,IA2cp4,IA2cp5,IA2cp6,IA2cp7,IA2cp8,IA2cp9])
    IA1[0,0]=1
    IA2[0,0]=1
    for i in range(10,19):
        IA1[i,0]=10
        IA2[i,0]=10
    return IA1,IA2

def resetIAS():
    IA1=np.zeros((19,2804))
    IA2=np.zeros((19,2804))
    IA1[0,0]=1
    IA2[0,0]=1
    for i in range(10,19):
        IA1[i,0]=10
        IA2[i,0]=10
    return IA1,IA2

def capass():
    enregistrementIA(IA1,IA2)

def enregistrementIA(IA1,IA2):
    with open('stokage.txt', 'wb') as e:  #on stocke les listes definissant les IA
        np.save(e, IA1)
        np.save(e, IA2)


def chargerlistes():
    with open('stokage.txt', 'rb') as e:     #on charge les listes des IA
        IA1 = np.load(e)
        IA2 = np.load(e)
    return IA1,IA2

def setupmem():
    IA1,IA2=resetIAS()
    enregistrementIA(IA1,IA2)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
##fonctions d'entraînement
def entrainement(suivi):
    plato=np.array([[0,0,0],[0,0,0],[0,0,0]]) #platon=np.array([[1,2,3],[4,5,6],[7,8,9]])
    fingame=0
    if random.randint(0,1)>=0.5:     #On choisit quelle IA commence
        IAjoue=1
    else:
        IAjoue=0
    IA1coupsjoués=[]
    IA2coupsjoués=[]
    while fingame==0:
        if suivi==1:
            print()
            print(plato)
        plato,coupjoué=jeuIA(plato,IAjoue,0)
        fingame=checkend(plato)
        if IAjoue==1:
            IAjoue=0
            IA1coupsjoués.append(coupjoué)
        else:
            IAjoue=1
            IA2coupsjoués.append(coupjoué)
    if fingame==-1:
        win=-1
    else:
        if IAjoue==1:
            win=0
        else:
            win=1
    if suivi==1:
        print(plato)
        print("win=",win)
        print("@@@@@@@@@@@")
    amélioration(win,IA1coupsjoués,IA2coupsjoués)


    
    


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




def jeuIA(plato,IAjoue,cjoueur): #adapter aux numéros joués par le joueur
    situation=dematrix(plato)
    if IAjoue==1:
        Lplato=dematrix(plato)
        bestcalq=meilleurcalq(plato,IAjoue)
        calqdecision=[]
        for i in range(10,19):
            calqdecision.append(IA1[i,bestcalq[0]])
        calqdecision=platourne(calqdecision,bestcalq[1])
        probtot=0
        for a in range(0,9):
            probtot=probtot+calqdecision[a]
        probtot=int(probtot)
        choix=random.randint(0,probtot)
        if choix==0:
            choix=1
        if choix==90:
            choix=89
        #print("nb random pris (IA1)",choix)
        #print("calque de l'IA1",IA1[:,bestcalq[0]])   #"bug: le float de certains calques les faits passer au dessus de 90, n'ayant donc  jamais de case proposée"
        casechoisie=-1
        if cjoueur==1:
            everandom=1
        else:
            everandom=random.randint(0,evealéa)
        if everandom==0:
            casetrouve=0
            while casetrouve==0:
                casetest=int(round(random.randint(0,8)))
                if Lplato[casetest]==0:
                    Lplato[casetest]=1
                    casetrouve=1
            casechoisie=casetest
        else:
            while choix>0:
                casechoisie=casechoisie+1
                choix=choix-calqdecision[casechoisie]
            if Lplato[casechoisie]==0:
                if cjoueur==1:
                    Lplato[casechoisie]=2
                else:
                    Lplato[casechoisie]=1
            else:
                casetrouve=0
                while casetrouve==0:
                    casetest=int(round(random.randint(0,8)))
                    if Lplato[casetest]==0:
                        Lplato[casetest]=1
                        casetrouve=1
                casechoisie=casetest
        plato=rematrix(Lplato)
    else:
        Lplato=dematrix(plato)
        bestcalq=meilleurcalq(plato,IAjoue)
        calqdecision=[]
        for i in range(10,19):
            calqdecision.append(IA2[i,bestcalq[0]])
        calqdecision=platourne(calqdecision,bestcalq[1])
        probtot=0
        for a in range(0,9):
            probtot=probtot+calqdecision[a]
        probtot=int(probtot)
        choix=random.randint(0,probtot)
        if choix==0:
            choix=1
        if choix==90:
            choix=89
        #print("nb random pris (IA2)",choix)
        #print("calque de l'IA2",IA2[:,bestcalq[0]])
        casechoisie=-1
        if cjoueur==1:
            everandom=1
        else:
            everandom=random.randint(0,evealéa)
        if everandom==0:
            casetrouve=0
            while casetrouve==0:
                casetest=int(round(random.randint(0,8)))
                if Lplato[casetest]==0:
                    Lplato[casetest]=2
                    casetrouve=1
            casechoisie=casetest
        else:
            while choix>0:
                casechoisie=casechoisie+1
                choix=choix-calqdecision[casechoisie]
            if Lplato[casechoisie]==0:
                Lplato[casechoisie]=2
            else:
                casetrouve=0
                while casetrouve==0:
                    casetest=int(round(random.randint(0,8)))
                    if Lplato[casetest]==0:
                        Lplato[casetest]=2
                        casetrouve=1
                casechoisie=casetest
        plato=rematrix(Lplato)
    infos=bestcalq
    casedansref=[]
    for i in range (0,9):
        if i==casechoisie:
            casedansref.append(1)
        else:
            casedansref.append(0)
    casedansref=platourne(casedansref,4-bestcalq[1])
    for i in range(0,9):
        if casedansref[i]==1:
            casejouée=i
    infos.append(casejouée)
    for i in range(0,9):
        infos.append(situation[i]) #à la fin, infos a 13éléments: n°calque, rota appliquée, score, n°case jouée puis 9 pour la situation
    #vérificationmanuelle()
    return plato, infos
        
        
def meilleurcalq(plato,IAjoue):
    if IAjoue==1:
        bestcalq=[]
        hscore=0   #le plus haut score obtenu
        situ=dematrix(plato)
        nteste=0
        while nteste+1==IA1[0,nteste]:
            rota=0
            calqtz=[]                   #liste du calque testé (sans rotation)
            for i in range(1,10):
                calqtz.append(IA1[i,nteste])
            while rota<4:
                calqt=platourne(calqtz,rota)
                score=0
                for i in range(0,9):
                    if situ[i]==calqt[i]:
                        score=score+10
                    else:
                        if situ[i]==2:
                            score=score+0
                        else:
                            if calqt[i]==0:
                                score=score+0
                            else:
                                score=score+4
                if score>hscore:
                    bestcalq=[nteste,rota,score]
                    hscore=score
                rota=rota+1
            nteste=nteste+1
    else:
        bestcalq=[]
        hscore=0   #le plus haut score obtenu
        situ=dematrix(plato)
        nteste=0
        while nteste+1==IA2[0,nteste]:
            rota=0
            calqtz=[]                   #liste du calque testé (sans rotation)
            for i in range(1,10):
                calqtz.append(IA2[i,nteste])
            while rota<4:
                calqt=platourne(calqtz,rota)
                score=0
                for i in range(0,9):
                    if situ[i]==calqt[i]:
                        score=score+10
                    else:
                        if situ[i]==2:
                            score=score+0
                        else:
                            if calqt[i]==0:
                                score=score+0
                            else:
                                score=score+4
                if score>hscore:
                    bestcalq=[nteste,rota,score]
                    hscore=score
                rota=rota+1
            nteste=nteste+1
    return bestcalq




def  amélioration(win,IA1coupsjoués,IA2coupsjoués): #"la matrice n'accepte que les nombres entiers, faut rework"
    #print("win by",win)
    #print("IA1coups",IA1coupsjoués)
    #print("IA1coups",IA2coupsjoués)
    mod=modulateur
    IA1coupsjoués=np.array(IA1coupsjoués)
    IA1nbcoups=np.size(IA1coupsjoués)/13
    b=0
    while b+1==IA1[0,b]:
        b=b+1
    ntotcalq=b
    if win==1:
        modif=mod
    else:
        if win==-1:
            modif=0
        else:
            modif=-mod
    for i in range(0,int(IA1nbcoups)):
        ncalq=IA1coupsjoués[i,0]
        if IA1coupsjoués[i,2]==90:
            caseslibres=0
            for c in range(4,13):
                if IA1coupsjoués[i,c]==0:
                    caseslibres=caseslibres+1
            for a in range(10,19):
                if a-10==IA1coupsjoués[i,3]:
                    IA1[a,ncalq]=IA1[a,ncalq]+modif
                else:
                    if IA1[a-9,ncalq]==0:
                        IA1[a,ncalq]=IA1[a,ncalq]-(modif/(caseslibres-1))            
        else:
            if IA1[0,ntotcalq]==0:
                IA1[0,ntotcalq]=ntotcalq+1
                caseslibres=0
                for c in range(4,13):
                    IA1[c-3,ntotcalq]=IA1coupsjoués[i,c]
                    if IA1coupsjoués[i,c]==0:
                        caseslibres=caseslibres+1
                for d in range(10,19):
                    if IA1[d-9,ntotcalq]==0:
                        IA1[d,ntotcalq]=90/caseslibres
                    else:
                        IA1[d,ntotcalq]=0
            else:
                print("ERROR def amélioration")
            ntotcalq=ntotcalq+1              
    #
    #
    #
    IA2coupsjoués=np.array(IA2coupsjoués)
    mod=modulateur
    IA2coupsjoués=np.array(IA2coupsjoués)
    IA2nbcoups=np.size(IA2coupsjoués)/13
    b=0
    while b+1==IA2[0,b]:
        b=b+1
    ntotcalq=b
    if win==0:
        modif=mod
    else:
        if win==-1:
            modif=0
        else:
            modif=-mod
    for i in range(0,int(IA2nbcoups)):
        ncalq=IA2coupsjoués[i,0]
        if IA2coupsjoués[i,2]==90:
            caseslibres=0
            for c in range(4,13):
                if IA2coupsjoués[i,c]==0:
                    caseslibres=caseslibres+1
            for a in range(10,19):
                if a-10==IA2coupsjoués[i,3]:
                    IA2[a,ncalq]=IA2[a,ncalq]+modif
                else:
                    if IA2[a-9,ncalq]==0:
                        IA2[a,ncalq]=IA2[a,ncalq]-(modif/(caseslibres-1))            
        else:
            if IA2[0,ntotcalq]==0:
                IA2[0,ntotcalq]=ntotcalq+1
                caseslibres=0
                for c in range(4,13):
                    IA2[c-3,ntotcalq]=IA2coupsjoués[i,c]
                    if IA2coupsjoués[i,c]==0:
                        caseslibres=caseslibres+1
                for d in range(10,19):
                    if IA2[d-9,ntotcalq]==0:
                        IA2[d,ntotcalq]=90/caseslibres
                    else:
                        IA2[d,ntotcalq]=0
            else:
                print("ERROR def amélioration")
            ntotcalq=ntotcalq+1
    réparerreurs()



def réparerreurs():
    e=0
    while IA1[0,e]==e+1:
        caseslib=0
        Lcaseslib=[]
        for c in range(10,19):
            if IA1[c-9,e]==0:
                caseslib=caseslib+1
                Lcaseslib.append(c)
        for a in range(0,len(Lcaseslib)):
            if IA1[Lcaseslib[a],e]<0:
                surmoins=0-IA1[Lcaseslib[a],e]
                IA1[Lcaseslib[a],e]=IA1[Lcaseslib[a],e]+surmoins
                diviseur=len(Lcaseslib)
                for b in range(0,len(Lcaseslib)):
                    if IA1[Lcaseslib[b],e]<=0:
                        diviseur=diviseur-1
                for d in range(0,len(Lcaseslib)):
                    if IA1[Lcaseslib[d],e]>0:
                        IA1[Lcaseslib[d],e]=IA1[Lcaseslib[d],e]-(surmoins/diviseur)
        fada=0
        for i in range(10,19):
            fada=fada+IA1[i,e]
        if fada!=90:
            diviseur=len(Lcaseslib)
            fada=fada-90
            for b in range(0,len(Lcaseslib)):
                if IA1[Lcaseslib[b],e]<=0:
                    diviseur=diviseur-1
            for d in range(0,len(Lcaseslib)):
                if IA1[Lcaseslib[d],e]>0:
                    IA1[Lcaseslib[d],e]=IA1[Lcaseslib[d],e]-(fada/diviseur)
        e=e+1
    #
    #
    #
    e=0
    while IA2[0,e]==e+1:
        caseslib=0
        Lcaseslib=[]
        for c in range(10,19):
            if IA2[c-9,e]==0:
                caseslib=caseslib+1
                Lcaseslib.append(c)
        for a in range(0,len(Lcaseslib)):
            if IA2[Lcaseslib[a],e]<0:
                surmoins=0-IA2[Lcaseslib[a],e]
                IA2[Lcaseslib[a],e]=IA2[Lcaseslib[a],e]+surmoins
                diviseur=len(Lcaseslib)
                for b in range(0,len(Lcaseslib)):
                    if IA2[Lcaseslib[b],e]<=0:
                        diviseur=diviseur-1
                for d in range(0,len(Lcaseslib)):
                    if IA2[Lcaseslib[d],e]>0:
                        IA2[Lcaseslib[d],e]=IA2[Lcaseslib[d],e]-(surmoins/diviseur)
        fada=0
        for i in range(10,19):
            fada=fada+IA2[i,e]
        if fada!=90:
            fada=fada-90
            diviseur=len(Lcaseslib)
            for b in range(0,len(Lcaseslib)):
                if IA2[Lcaseslib[b],e]<=0:
                    diviseur=diviseur-1
            for d in range(0,len(Lcaseslib)):
                if IA2[Lcaseslib[d],e]>0:
                    IA2[Lcaseslib[d],e]=IA2[Lcaseslib[d],e]-(fada/diviseur)
        e=e+1

                        

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
##fonctions de manipulations du plato/calque
def dematrix(plato):#Transforme une matrice 3*3 en liste 9 termes
    dematrixed=[]
    a=0
    while a<=2:
        b=0
        while b<=2:
            dematrixed.append(plato[a,b])
            b=b+1
        a=a+1
    return dematrixed

def rematrix(Lplato):#Transforme liste 9 termes en une matrice 3*3
    untiers=Lplato[0:3]
    deuxtiers=Lplato[3:6]
    troistiers=Lplato[6:9]
    plato=np.array([untiers,deuxtiers,troistiers])
    return plato

def platourne(Lplato,rota):#fait tourner une liste représentant une matrice 3*3 selon rota * 90 deg
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



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
##fonction d'interaction avec l'utilisateur (match,transmission d'infos)
def matchcontrejoueur(nIA):
    plato=np.array([[0,0,0],[0,0,0],[0,0,0]]) #platon=np.array([[1,2,3],[4,5,6],[7,8,9]])
    fingame=0
    if random.randint(0,1)>=0.5:     #On choisit quelle IA commence
        joueurjoue=1
    else:
        joueurjoue=0
    IA1coupsjoués=[]
    IA2coupsjoués=[]
    while fingame==0:
        print(plato)
        if joueurjoue==0:
            joueurjoue=1
            print("l'ia joue")
            plato,coupjoué=jeuIA(plato,nIA,1)
            if nIA==1:
                IA1coupsjoués.append(coupjoué)
            else:
                IA2coupsjoués.append(coupjoué)
        else:
            print("à vous de jouer")
            joueurjoue=0
            Lplato=dematrix(plato)
            casetrouvée=0
            while casetrouvée==0:
                casejouée=int(input("quelle case voulez-vous jouer?(1/2/.../9)"))-1
                if Lplato[casejouée]==0:
                    casetrouvée=1
            Lplato[casejouée]=1
            plato=rematrix(Lplato)
        fingame=checkend(plato)
    if fingame==-1:
        win=-1
        print("égalité")
    else:
        if joueurjoue==0:
            print(plato)
            print("vous avez gagné!")
            win=-2
        else:
            print(plato)
            print("j'ai gagné(par le biais de mon IA mais ça compte)")
            win=nIA
    print("@@@@@@@@@@@")
    amélioration(win,IA1coupsjoués,IA2coupsjoués)


def vérificationmanuelle():#affiche tout les calques des deux IAs
    print("IA1")
    e=0
    LtotIA1=[]
    while e+1==IA1[0,e]:
        totIA1=0
        for i in range(10,19):
            totIA1=totIA1+IA1[i,e]
        LtotIA1.append(totIA1)
        print(IA1[:,e],"total",totIA1)
        e=e+1
    print("IA2")
    e=0
    LtotIA2=[]
    while e+1==IA2[0,e]:
        totIA2=0
        for i in range(10,19):
            totIA2=totIA2+IA2[i,e]
        LtotIA2.append(totIA2)
        print(IA2[:,e],"total",totIA2)
        e=e+1



"""""
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
MAIN
"""""
aa=input("besoin de setup (oui/non)?")
if aa=="oui":
    IA1,IA2=resetIAS()
    enregistrementIA(IA1,IA2)
IA1,IA2=chargerlistes()



def main(IA1,IA2):
    ad = input("match ou gestion?")
    if ad=="gestion":
        ae = input("memoire ,infos ou entrainement?")
        if ae=="memoire":
            af=input("charger, stocker ou reset?")
            if af=="charger":
                IA1,IA2=chargerlistes()
            if af=="stocker":
                enregistrementIA(IA1,IA2)
            if af=="reset":
                IA1,IA2=resetIAS()
        if ae=="infos":
            ag=input("quelleIA (1/2)?")
            if ag=="1":
                vérificationmanuelle()
            if ag=="2":
                vérificationmanuelle()
        if ae=="entrainement":
            ah=input("combien d'entrainements?(avec infos)")
            if ah=="avec infos":
                ai=int(input("combien d'entrainements?"))
                for i in range(0,ai):
                    entrainement(1)
                    print(i)
                    #vérificationmanuelle()
            else:
                ai=int(ah)
                for i in range(0,ai):
                    entrainement(0)
                    print(i)
    if ad=="match":
        matchcontrejoueur(2)
    quit=input("quitter?(oui/non)")
    if quit=="non":
        main(IA1,IA2)
        
main(IA1,IA2)