# Créé par HUMBERT, le 25/05/2023 en Python
import numpy  as np
from matplotlib import pyplot as plt
from math import exp, expm1, sqrt

#Définition des valeurs
vikmh = 30        #vitesse initiale(km/h)
al = 10           #angle de tir(degrés)
hi = 0.1            #hauteur initiale de tir(m)
m = 0.0027             #masse de la boule tirée(kg)
r = 0.02            #rayon de la boule(m)
da = 1.263       #densité de l'air(kg.m^-3)
Cx = 0.47        #coefficient de trainée de l'objet tiré(sans unité)
g = 9.81             #intensité de la pesenteur(N.kg^-1)
t = 0             #temps écoulé depuis le tir(s)
ventkmh = 0           #vitesse du vent(axe Ox)(km/h)
pas = 0.001       #pas du calcul(temps)(s)

#Calcul des autres grandeurs
vent = ventkmh/3.6 #vitesse du vent(axe Ox)(m/s)
vi = vikmh/3.6   #vitesse initiale(m/s)
S = np.pi*r*r    #section frontale de l'objet tiré
fv = 0.5*da*S*Cx #trainée divisée par la vitesse par rapport à l'air au carré(N.m^-2.s^2)
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

#corrections approximatives
##1.01*(fv * ((Voy) ** 2) * (m ** -1) * dt) <= (P*(m**-1)*dt)


#vérification des données


#Création des listes
temps = []        #liste des moments des mesures
posxt = []        #position x de l'objet au cours du temps
posyt = []        #position y de l'objet au cours du temps
Emt = []          #énergie mécanique au cours de temps
Ect = []          #énergie cinétique au cours de temps
Ept = []          #énergie potentielle au cours de temps
tracking_Voy = []

#Définition des fonctions


#calcul pas à pas
#   enregistrement des position de départ
posxt.append(posx)
posyt.append(posy)
temps.append(t)
Ect.append(Ec)
Ept.append(Ep)
Emt.append(Em)
#   premier calcul
posx = posx+(Vox*dt)
posy = posy+(Voy*dt)
posxt.append(posx)
posyt.append(posy)
t = t+dt
temps.append(t)
Ec = 0.5*m*((Vox**2)+(Voy**2))
Ep = posy*m*g
Em = Ec+Ep
Ect.append(Ec)
Ept.append(Ep)
Emt.append(Em)
if Vox < vent :
    Vox = Vox+(fv*((Vox-vent)**2)*(m**-1)*dt)
if Vox > vent :
    Vox = Vox-(fv*((Vox-vent)**2)*(m**-1)*dt)
Voy = Voy-(fv*((Voy)**2)*(m**-1)*dt)
Voy = Voy-(P*(m**-1)*dt)
#calcule le trajet jusqu'a ce que le boule touche le sol
while posy > 0 :
    posx = posx+(Vox*dt)
    posy = posy+(Voy*dt)
    posxt.append(posx)
    posyt.append(posy)
    t = t+dt
    temps.append(t)
    Ec = 0.5*m*((Vox**2)+(Voy**2))
    Ep = posy*m*g
    Em = Ec+Ep
    Ect.append(Ec)
    Ept.append(Ep)
    Emt.append(Em)
    if Vox < vent :
        Vox = Vox+(fv*((Vox-vent)**2)*(m**-1)*dt)
    if Vox > vent :
        Vox = Vox-(fv*((Vox-vent)**2)*(m**-1)*dt)
    if Voy > 0:
        Voy = Voy - ((fv * ((Voy) ** 2) * (m ** -1)+g) * dt)
    if Voy < 0:
        Voy = Voy + ((fv * ((Voy) ** 2) * (m ** -1)-g) * dt)
        if a == 0:
            a = 1
            hA = posy
            dA = posx
            tA = t
dB = posx
tB = t


#informations
print("==============")
print("sommet de la parabole")
print(f"temps = {tA}")
print(f"distance = {dA}")
print(f"hauteur = {hA}")
print()
print("==============")
print("fin de la parabole")
print(f"temps = {tB}");
print(f"distance = {dB}")
print(f"hauteur = {posy}")
print()
print("==============")
print(f"vitesses finales")
print("verticale = ",Voy," m.s-1")
print("horizontale = ",Vox," m.s-1")
print("absolue = ",sqrt((Voy*Voy)+(Vox*Vox))," m.s-1")

#calcul des limites du cadre nécéssaires
#toujours 20% de rab par rapport à la plus grande valeur pour une meilleure lisibilité
#les maximum des abscisses et des ordonnées doivent être identiques
if dB > hA :
    xmax1 = 1.2*dB
    ymax1=xmax1
else:
    ymax1 = 1.2*hA
    xmax1=ymax1
ymax2 = 1.2*EMmax
xmax2 = xmax1



#calcul global

#créer les 2 figures
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 10))


#Tracer le graphique courbe des tirs(1)
ax1.set_title('représentation des tirs')
ax1.set_xlabel('longueur(m)')
ax1.set_ylabel('hauteur(m)')
ax1.set_xlim(0,xmax1)
ax1.set_ylim(0,ymax1)
ax1.plot(posxt,posyt,'r')
ax1.legend(['courbe du projectile'])
ax1.grid()

#Tracer le graphique courbe des énergies(2)
ax2.set_title('représentation des energies')
ax2.set_xlabel('distance parcourue(m)')
ax2.set_ylabel('quantité d énergie(J)')
ax2.set_xlim(0,xmax2)
ax2.set_ylim(0,ymax2)
ax2.plot(posxt,Ect,'y')
ax2.plot(posxt,Ept,'g')
ax2.plot(posxt,Emt,'b')
ax2.legend(['énergie cinétique','energie potentielle','énergie mécanique'])
ax2.grid()



#afficher les deux figures ensemble
plt.tight_layout()  # Pour éviter que les titres et les axes se chevauchent
plt.show()

#informations:

