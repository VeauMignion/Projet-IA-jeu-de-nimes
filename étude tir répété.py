# Créé par HUMBERT, le 25/05/2023 en Python
import numpy  as np
from matplotlib import pyplot as plt
from math import exp, expm1, sqrt,log

#Définition des valeurs
vikmh = 50       #vitesse initiale(km/h)
al = 30         #angle de tir(degrés)
hi = 1            #hauteur initiale de tir(m)
m = 0.1             #masse de la boule tirée(kg)
r = 0.02            #rayon de la boule(m)
da = 1.263       #densité de l'air(kg.m^-3)
Cx = 0.47        #coefficient de trainée de l'objet tiré(sans unité)
g = 9.81             #intensité de la pesenteur(N.kg^-1)
t = 0             #temps écoulé depuis le tir(s)
ventkmh = 0           #vitesse du vent(axe Ox)(km/h)
pas = 0.0001       #pas du calcul(temps)(s)

#Calcul des autres grandeurs
vent = ventkmh/3.6 #vitesse du vent(axe Ox)(m/s)
vi = vikmh/3.6   #vitesse initiale(m/s)
S = np.pi*r*r    #section frontale de l'objet tiré
fv = 0.5*da*S*Cx #trainée divisée par la vitesse par rapport à l'air au carré(N.m^-2.s^2)
j=fv/m           #accélération divisée par la vitesse par rapport à l'air au carré(m^-1)
P = m*g          #poids de l'objet(N)
posx = 0         #position x de départ de l'objet
posy = hi        #position y de départ de l'objet
k = 360/(2*np.pi)#pour changer les degrés en radiants
alr = al/k       #angle de tir en radiants
Vox = vi*np.cos(alr)#vitesse de l'objet dans l'axe Ox
Voy = vi*np.sin(alr)#vitesse de l'objet dans l'axe Oy
dt = pas         #autre nom pour le pas (temps)(s)
Ec = 0.5*m*((Vox**2)+(Voy**2))            #énergie cinétique(J)
Ep = posy*m*g           #énergie potentielle(J)
Em = Ec+Ep              #énergie mécanique(J)
EMmax = Em              #énergie mécanique max (J) (pour les limites du graphique
hA = 0                  #informations sur le point A (sommet de la parabole)
dA = 0
tA = 0
dB = 0                  #informations sur le point B (fin de la courbe)
tB = 0
a = 0                   #si sommet déja enrigistré, a=1

#constantes à garder
Voxd=Vox

#opérations répétées
vitessemax=1000
nbtestvoulus=30
testn=0
#listes
Voyliste=[]
Voysqliste=[]
lntsliste=[]
tsliste=[]
tsestimliste=[]
while testn<nbtestvoulus:
    #nouvelles valeurs(mise à 0)
    testn=testn+1
    print("test",testn)
    Voy=(testn*vitessemax)/nbtestvoulus
    Voyliste.append(Voy)
    Voysqliste.append(1.37-exp(-Voy/30))
    t=0
    Vox=Voxd
    a=0
    tA=0
    #Création des listes

    ts_estim=1.37-exp(-Voy/30)
    tsestimliste.append(ts_estim)
    #Définition des fonctions


    #calcul pas à pas
    #   enregistrement des position de départ
    #   premier calcul
    posx = posx+(Vox*dt)
    posy = posy+(Voy*dt)
    t = t+dt
    if Vox < vent :
        Vox = Vox+(fv*((Vox-vent)**2)*(m**-1)*dt)
    if Vox > vent :
        Vox = Vox-(fv*((Vox-vent)**2)*(m**-1)*dt)
    Voyold=Voy
    Voy = Voy-(fv*((Voy)**2)*(m**-1)*dt)
    Voy = Voy-(P*(m**-1)*dt)
    #calcule le trajet jusqu'a ce que le boule touche le sol
    while tA == 0 :
        posx = posx+(Vox*dt)
        posy = posy+(Voy*dt)
        t = t+dt
        Voyold=Voy
        if Vox < vent :
            Vox = Vox+(fv*((Vox-vent)**2)*(m**-1)*dt)
        if Vox > vent :
            Vox = Vox-(fv*((Vox-vent)**2)*(m**-1)*dt)
        if Voy < 0:
            Voy = Voy + ((fv * ((Voy) ** 2) * (m ** -1)-g) * dt)
            if a == 0:
                a = 1
                hA = posy
                dA = posx
                tA = t
        if Voy > 0:
            Voy = Voy - ((fv * ((Voy) ** 2) * (m ** -1)+g) * dt)
    dB = posx
    tB = t
    tsliste.append(tA)
    lntsliste.append(log(tA))

#calcul des lim du graphe
if tA>ts_estim:
    ymax1=1.2*tA
else:
    ymax1=1.2*ts_estim

if lntsliste[len(lntsliste)-1] > lntsliste[0]:
    ymax3=lntsliste[len(lntsliste)-1]
else:
    ymax3=lntsliste[0]

#2 sousgraphiques:
fig, ((ax1, ax2),(ax3,ax4)) = plt.subplots(2, 2, figsize=(10, 10))

ax1.set_title('ts en fonction Voy initiale')
ax1.set_xlabel('Voy(m.s-1)')
ax1.set_ylabel('ts(s)')
ax1.set_xlim(0,vitessemax)
ax1.set_ylim(0,ymax1)
ax1.plot(Voyliste,tsliste,'r')
ax1.plot(Voyliste,tsestimliste,'b')
ax1.grid()

ax2.set_title('ts en fonction de sqrt de Voy initiale')
ax2.set_xlabel('sqrt Voy(m.s-1)')
ax2.set_ylabel('ts(s)')
ax2.set_xlim(0,1.2*Voysqliste[len(Voysqliste)-1])
ax2.set_ylim(0,ymax1)
ax2.plot(Voysqliste,tsliste,'g')
ax2.grid()

ax3.set_title('ln de ts en fonction de Voy initiale')
ax3.set_xlabel('Voy(m.s-1)')
ax3.set_ylabel('ln ts(s)')
ax3.set_xlim(0,vitessemax)
ax2.set_ylim(0,1.2*ymax3)
ax3.plot(Voyliste,lntsliste,'grey')
ax3.grid()

#informations:
print("@@@@@@@@@@@@@@")
print("oui")
plt.tight_layout()
plt.show()