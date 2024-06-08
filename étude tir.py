# Créé par HUMBERT, le 25/05/2023 en Python
import numpy  as np
from matplotlib import pyplot as plt
from math import exp, expm1, sqrt, atan, tan, log, cos

#Définition des valeurs
vikmh =487*3.6       #vitesse initiale(km/h)
al = 30        #angle de tir(degrés)
hi = 20            #hauteur initiale de tir(m)
m = 14.5            #masse de la boule tirée(kg)
r = 0.154            #rayon de la boule(m)
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
Vy=Voy
Vx=Vox


#//étude V2: le mode parfait
#fonctions utilisées
#vitesses:
def vitx(t):
    V=Vox/(abs(Vox)*j*t+1)
    return V
def vity(t):
    if Voy>0:
        if t<-(atan(-sqrt(j/g)*Voy)/sqrt(j*g)):
            V=-sqrt(g/j)*tan(sqrt(g*j)*t+atan(-sqrt(j/g)*Voy))
        else:
            V=sqrt(g/j)*(exp(2*sqrt(j*g)*t)-1)/(-exp(2*sqrt(j*g)*t)-1)
    else:
        V=sqrt(g/j)*(exp(2*sqrt(j*g)*t)*(-sqrt(j/g)*Voy+1)-sqrt(j/g)*Voy-1)/(-exp(2*sqrt(j*g)*t)*(-sqrt(j/g)*Voy+1)-sqrt(j/g)*Voy-1)
    return V

#Positions:
def pox(t):
    P=abs(Vox)/(j*Vox)*log(abs(Vox)*j*t+1)
    return P

def poy(t):
    if Voy>0:
        if t<-(atan(-sqrt(j/g)*Voy)/sqrt(j*g)):
            P=1/j*log(cos(sqrt(j*g)*t+atan(-sqrt(j/g)*Voy))/cos(atan(-sqrt(j/g)*Voy)))+hi
        else:
            P=log(abs(-exp(2*sqrt(j*g)*(t+atan(-sqrt(j/g)*Voy)/sqrt(j*g)))-1))/(-j)+sqrt(g/j)*(t+atan(-sqrt(j/g)*Voy)/sqrt(j*g))+log(2/cos(atan(-sqrt(j/g)*Voy)))/j+hi
    else:
        P=log(abs(-exp(2*sqrt(j*g)*t)*(-sqrt(j/g)*Voy+1)-sqrt(j/g)*Voy-1))/-j+sqrt(g/j)*t+log(2)/j+hi
    return P

##constantes précises
#au sommet
ts=-(atan(-sqrt(j/g)*Voy)/sqrt(j*g)) #temps au sommet
xs=pox(ts) #distance
ys=poy(ts) #hauteur

#à la fin
tf=1/sqrt(j*g)*log((exp(j*hi)+sqrt(exp(2*j*hi)-(cos(atan(-sqrt(j/g)*Voy)))**2))/(cos(atan(-sqrt(j/g)*Voy))))-(atan(-sqrt(j/g)*Voy)/sqrt(j*g))
xf=pox(tf)
yf=0

#vitesses finales
vfx=vitx(tf)
vfy=vity(tf)
vf=sqrt(vfx**2+vfy**2)

#production de la trace:
T=0
Lpx=[]
Lpy=[]
compteur=0
while T<tf:
    Lpx.append(pox(T))
    Lpy.append(poy(T))
    if compteur>1000:
        print(pox(T))
        print(poy(T))
        compteur=0
    compteur=compteur+1
    T=T+pas



#corrections approximatives
##1.01*(fv * ((Vy) ** 2) * (m ** -1) * dt) <= (P*(m**-1)*dt)


#vérification des données


#Création des listes
temps = []        #liste des moments des mesures
posxt = []        #position x de l'objet au cours du temps
posyt = []        #position y de l'objet au cours du temps
Emt = []          #énergie mécanique au cours de temps
Ect = []          #énergie cinétique au cours de temps
Ept = []          #énergie potentielle au cours de temps

#tests modélisations
tracking_Vy = [] 
tracking_ay = []
tracking_ayp=[]


#calcul pas à pas
#   enregistrement des position de départ
t=0
posxt.append(posx)
posyt.append(posy)
temps.append(t)
Ect.append(Ec)
Ept.append(Ep)
Emt.append(Em)
tracking_ay.append(0)
tracking_Vy.append(0)
ayp=0
tracking_ayp.append(ayp)
#   premier calcul
posx = posx+(Vx*dt)
posy = posy+(Vy*dt)
posxt.append(posx)
posyt.append(posy)
t = t+dt
temps.append(t)
tracking_Vy.append(Vy)
Ec = 0.5*m*((Vx**2)+(Vy**2))
Ep = posy*m*g
Em = Ec+Ep
Ect.append(Ec)
Ept.append(Ep)
Emt.append(Em)
if Vx < vent :
    Vx = Vx+(fv*((Vx-vent)**2)*(m**-1)*dt)
if Vx > vent :
    Vx = Vx-(fv*((Vx-vent)**2)*(m**-1)*dt)
Vyold=Vy
Vy = Vy-(fv*((Vy)**2)*(m**-1)*dt)
Vy = Vy-(P*(m**-1)*dt)
ay=(Vy-Vyold)/dt
tracking_ay.append(ay)
ayp=0
tracking_ayp.append(ayp)
#calcule le trajet jusqu'a ce que le boule touche le sol
while posy > 0 :
    posx = posx+(Vx*dt)
    posy = posy+(Vy*dt)
    posxt.append(posx)
    posyt.append(posy)
    tracking_Vy.append(Vy)
    t = t+dt
    temps.append(t)
    Ec = 0.5*m*((Vx**2)+(Vy**2))
    Ep = posy*m*g
    Em = Ec+Ep
    Ect.append(Ec)
    Ept.append(Ep)
    Emt.append(Em)
    Vyold=Vy
    ayold=ay
    if Vx < vent :
        Vx = Vx+(fv*((Vx-vent)**2)*(m**-1)*dt)
    if Vx > vent :
        Vx = Vx-(fv*((Vx-vent)**2)*(m**-1)*dt)
    if Vy < 0:
        Vy = Vy + ((fv * ((Vy) ** 2) * (m ** -1)-g) * dt)
        if a == 0:
            a = 1
            hA = posy
            dA = posx
            tA = t
    if Vy > 0:
        Vy = Vy - ((fv * ((Vy) ** 2) * (m ** -1)+g) * dt)
    ay=(Vy-Vyold)/dt
    tracking_ay.append(ay)
    ayp=(ay-ayold)/dt
    tracking_ayp.append(ayp)
dB = posx
tB = t


#informations
print("==============")
print("sommet de la parabole")
print(f"temps = {tA}")
print(f"temps(mode2) = {ts}")
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
print("verticale = ",Vy," m.s-1")
print("horizontale = ",Vx," m.s-1")
print("absolue = ",sqrt((Vy*Vy)+(Vx*Vx))," m.s-1")

#calcul des limites du cadre nécéssaires
#toujours 20% de rab par rapport à la plus grande valeur pour une meilleure lisibilité
#les maximum des abscisses et des ordonnées doivent être identiques
if hA<hi:
    hA=hi

if dB > hA :
    xmax1 = 1.2*dB
    ymax1=xmax1
else:
    ymax1 = 1.2*hA
    xmax1=1.2*dB
ymax2 = 1.2*EMmax
xmax2 = 1.2*dB

if tracking_ay[2]<tracking_Vy[2]:
    ymim3=1.2*tracking_ay[2]
    ymax3=1.2*tracking_Vy[2]
else:
    ymim3=1.2*tracking_Vy[2]
    ymax3=1.2*tracking_ay[2]
xmax3=1.2*t

if tracking_ay[3]<tracking_ayp[3]:
    if tracking_ayp[len(tracking_ayp)-1]<tracking_ayp[3]:
        ymax4=1.2*tracking_ayp[3]
        if tracking_ay[3]<tracking_ayp[len(tracking_ayp)-1]:
            ymin4=1.2*tracking_ay[3]
        else:
            ymin4=1.2*tracking_ayp[len(tracking_ayp)-1]
    else:
        ymax4=1.2*tracking_ayp[len(tracking_ayp)-1] 
        ymin4=1.2*tracking_ay[3]
else:
    if tracking_ay[3]>tracking_ayp[len(tracking_ayp)-1]:
        ymax4=tracking_ay[3]
        if tracking_ayp[3]<tracking_ayp[len(tracking_ayp)-1]:
            ymin4=tracking_ayp[3]
        else:
            ymin4=tracking_ayp[len(tracking_ayp)-1]
    else:
        ymax4=1.2*tracking_ayp[len(tracking_ayp)-1] 
        ymin4=1.2*tracking_ayp[3]

if ymax3**2<1:
    ymax3=1
    
if ymax4**2<1:
    ymax4=1

ymax4=max(tracking_ayp)


#calcul global

#créer les 2 figures
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(8, 8))


#Tracer le graphique courbe des tirs(1)
ax1.set_title('représentation des tirs')
ax1.set_xlabel('longueur(m)')
ax1.set_ylabel('hauteur(m)')
ax1.set_xlim(0,xmax1)
ax1.set_ylim(0,ymax1)
ax1.plot(posxt,posyt,'r')
ax1.plot(Lpx,Lpy,'b')
ax1.legend(['courbe du projectile','modélisation parfaite'])
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

#tracer le graphique des vitesses et accélérations(3)
ax3.set_title('représentation des vitesses et accélérations en y')
ax3.set_xlabel('temps(s)')
ax3.set_ylabel('vitesse(m*s-1),acc(m*s-2)')
ax3.set_xlim(0,1.2*t)
ax3.set_ylim(ymim3,ymax3)
ax3.plot(temps,tracking_ay,'r')
ax3.plot(temps,tracking_Vy,'g')
ax3.legend(['accélérations','vitesses'])
ax3.grid()

ax4.set_title('représentation des vitesses et accélérations en y')
ax4.set_xlabel('temps(s)')
ax4.set_ylabel('vitesse(m*s-1),acc(m*s-2)')
ax4.set_xlim(0,1.2*t)
ax4.set_ylim(ymin4,ymax4)
ax4.plot(temps,tracking_ay,'r')
ax4.plot(temps,tracking_ayp,'grey')
ax4.legend(['accélérations','dérivé d-accélération'])
ax4.grid()


#afficher les deux figures ensemble
plt.tight_layout()  # Pour éviter que les titres et les axes se chevauchent
plt.show()

#informations: