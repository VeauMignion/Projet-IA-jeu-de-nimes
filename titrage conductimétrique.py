# Créé par HUMBERT, le 30/09/2023 en Python 3.7
import numpy  as np
from matplotlib import pyplot as plt
from math import exp, expm1, sqrt

##Le but de ce programme va être de décrire par l'intervalle d'un graphique l'evolution de la condutance d'une solution en cours de titrage
##Le logiciel de base devra être capable de fonctionner pour des réactions type: (aA + sS) +> (bB + iI) --> sS + iI + pP + fF ou A et S sont les ions de
##la solution titrante, et B et I les ions de la solution titrée

#Information nécéssaires sur les ions
nameionA="H3O+"            #nom des différents ions (à écrire dans la formule)
nameionS="Cl-"
nameionB="HO-"
nameionI="Na+"
nameionP="H2O"
nameionF=""


a=1                         #nombre stœchiométrique qui leur est associé
s=1
b=1
i=1
p=2
f=0

condA=35.0*1e-3             #leur conductivité molaire ionique en S.m^2.mol^-1
condS=7.63*1e-3
condB=19.8*1e-3
condI=5.01*1e-3
condP=0
condF=0

#informations nécéssaires sur les solutions
VBI=20                       #volume de solution B + I en mL
VmaxAS=20                    #volume maximal de solution A + S en mL

CBI=0.05                     #concentration de la solution B + I en mol.L^-1
CAS=0.10

#mode de calcul (0 pour le pas par pas et 1 pour le logique)
ModeC=0
pas=1                        #pas du titrage en mL

##Premier affichage sur la réaction
print()
print("*****************************")
print("Equation de réaction:")
print(a,nameionA,"+",s,nameionS,"+",b,nameionB,"+",i,nameionI," ==> ",s,nameionS,"+",i,nameionI,"+",p,nameionP,"+",f,nameionF)
print("*****************************")
print()

#déductions et conversions
VBIL=VBI*1e-3                 #VBI en L
nI=i*CBI*VBIL                   #quantité de matière de l'ion I(mol)(qui ne varie pas car il est dans la solution titrée et spectateur)
niA=0                         #quantité de matière initales des ions de la solution titrante (égale à 0)
niS=0
niP=0                         #quantité de matière initiale des produits (égal à 0)
niF=0
niB=b*CBI*VBIL                #quantité de matière initiale de l'ion B(mol)

#definition de variables utiles
Vverse=0                     #volume versé de solution A + S en mL
Vtot=VBI+Vverse                      #volume total de solution dans le becher en mL
Vtotm3=Vtot*1e-6             #volume total de solution dans le becher en m^3
sig=0                          #Conductivité de la solution en S.m^-1
sigmS=sig*1e3                  #Conductivité de la solution en mS.m^-1
sigV=[]
evoVolverse=[]
evonA=[]
evonS=[]
evonB=[]
evonI=[]
evonP=[]
evonF=[]
nA=0                         #quantité de matière des ions de la solution titrante (égale à 0)
nS=0
nP=0                         #quantité de matière des produits (égal à 0)
nF=0
nB=b*CBI*VBIL                #quantité de matière de l'ion B(mol)
najouteA=0
Veexp=0
Veparfait=0
Avmax=0                      #avancement à l'équivalance (avancement max)(mol)
n=-1
derivsig=0                   #dérivée de la conductance
evoderivsig=[]
sigd=0
sige=0
sigf=0

#pas par pas
if ModeC == 0:
    while Vverse <= VmaxAS:
        n=n+1
        sig=((nA/Vtotm3)*condA+(nB/Vtotm3)*condB+(nS/Vtotm3)*condS+(nI/Vtotm3)*condI+(nP/Vtotm3)*condP+(nF/Vtotm3)*condF)       #calcul de la conductivité
        sigmS=sig*1e3                                                                                                          #actuelle et stockage de
        sigV.append(sigmS)
        if n>0 :
            derivsig=(sigV[n]-sigV[n-1])/pas
        evoderivsig.append(derivsig)                                                                                                   #la donnée
        evoVolverse.append(Vverse)
        evonA.append(nA)
        evonS.append(nS)
        evonB.append(nB)
        evonI.append(nI)
        evonP.append(nP)
        evonF.append(nF)
        print(sigmS,"/",Vverse)
        Vverse=Vverse+pas                                                                                                       ##calcul des nouvelles
        Vtot=VBI+Vverse                                                                                                         ##valeurs des volumes
        Vtotm3=Vtot*1e-6                                                                                                        ##et quantitées de
        nS=s*CAS*Vverse*1e-3                                                                                                    ##matière
        najouteA=a*CAS*pas*1e-3
        nB=nB-(najouteA/a)*b
        if nB > 0:
            nB=nB
            nA=0
            nP=nP+p*(najouteA/a)
            nF=nF+f*(najouteA/a)
        else:
            if 0-nB == (najouteA/a)*b:
                nA=nA+najouteA
                nB=0
                nP=nP
                nF=nF
            else:
                nA=0-nB
                nP=nP+p*((najouteA/a)*b+nB)
                nF=nF+f*((najouteA/a)*b+nB)
                nB=0
                Veexp=Vverse

    #résultats du pas par pas
    print()
    print()
    print("l'équivalance ce situe entre",Veexp-1,"mL et",Veexp,"mL")

    #graphiques
    #créer les 2 figures
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 10))

    #Tracer le graphique courbe des tirs(1)
    ax1.set_title('évolution des quantitées de matière')
    ax1.set_xlabel('Volume versé(mL)')
    ax1.set_ylabel('Quantitées de matière(mol)')
    ax1.set_xlim(0,VmaxAS+0.5)
    ax1.set_ylim(0,1.1*max(max(evonA), max(evonP), max(evonB), max(evonS), max(evonI)))
    ax1.plot(evoVolverse,evonA,'r', label="quantité de l'ion " + nameionA)
    ax1.plot(evoVolverse, evonP, 'b', label="quantité de l'ion " + nameionP)
    ax1.plot(evoVolverse, evonB, 'green', label="quantité de l'ion " + nameionB)
    ax1.plot(evoVolverse, evonI, 'black', label="quantité de l'ion " + nameionI)
    ax1.plot(evoVolverse, evonS, 'pink', label="quantité de l'ion " + nameionS)
    ax1.legend(loc='upper left')
    ax1.grid()

    #Graphique conductimetrie
    ax2.set_title('évolution de la conductance')
    ax2.set_xlabel('Volume versé(mL)')
    ax2.set_ylabel('Conductance (mS)')
    ax2.set_xlim(0,VmaxAS+0.5)
    ax2.set_ylim(1.1*min(min(evoderivsig),0),1.1*max(sigV))
    ax2.plot(evoVolverse,evoderivsig,'g', label="dérivée")
    ax2.plot(evoVolverse,sigV,'r', label="conductance")
    ax2.legend(loc='upper left')
    ax2.grid()


    plt.tight_layout()
    plt.show()

#Mode parfait
if ModeC == 0:
    sigd=((nA/Vtotm3)*condA+(nB/Vtotm3)*condB+(nS/Vtotm3)*condS+(nI/Vtotm3)*condI+(nP/Vtotm3)*condP+(nF/Vtotm3)*condF)
    Veparfait=(CBI*VBI*a)/b*CAS
    Ave
    nAe=0
    nSe=CAS*Veparfait*1e-3
    nBe=0
    nPe=0



























