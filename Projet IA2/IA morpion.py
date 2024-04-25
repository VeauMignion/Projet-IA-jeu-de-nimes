import numpy as np
#Idée du 06/04/24
#L'IA se défini par une liste calques: ces calques modélisent une situation que l'IA a affronté 
#(avec un système de coin indenté pour ne pas tenir compte des rotations) et s'accompagnent de probabilitées sur les coups que l'IA peut jouer 
#(qui s'adaptent en fonction des victoires et échecs de l'IA) quand l'IA affronte une situation qu'elle ne connaît pas, 
#elle cherche le calque le plus proche et joue selon ses probabilités (et elle crée un calque de la situation inconnue)
#créé le 13/04/24 par Paul HUMBERT
#pour plus d'infos voir documentation-IA-morpion.pdf


#on remet à 0 les IAS:
def resetIAS():
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
    for i in range(0,5000):
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
        
