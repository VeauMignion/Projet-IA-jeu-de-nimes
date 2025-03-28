#projet commencé le 11/10/23
#Créé par HUMBERT, le 23/10/2023 en Python 3.7
#créé par HUMBERT, le 21/10/2023
#aidé de Bouboy
#importations
from matplotlib import pyplot as plt
from math import exp, expm1, sqrt
from matplotlib.widgets import Slider
from matplotlib.gridspec import GridSpec
##le but de ce programme est de modéliser les zones où les interactions entre les ondes sont destructrices ou constructives, en fonction de:
##le mode ondes sur l'eau:                                le mode lumière(pas fait):
##a la distance entre les sources des ondes (cm)          (micro m)
##lamb la longeur d'onde (cm)                             (nm)(400-800)
##dT le déphasage temporel (micro s)(pas fait)             =0
##c la célérité de l'onde (m.s^-1)(pas fait)               =300 000 000m.s^-1
##D la distance par rapport à la source des ondes  (cm)    (m)

#fonction de la courbe
#def courbe (d):
#    traceh= a*0.5+(sqrt((d*d*a*a-d*d*d*d+4*d*d*D*D)/(a*a-d*d))*0.5)
#    traceb= a*0.5-(sqrt((d*d*a*a-d*d*d*d+4*d*d*D*D)/(a*a-d*d))*0.5)


#fonction de la courbe
def atraceh(d,a,x):
    return(a*0.5+(sqrt((d*d*a*a-d*d*d*d+4*d*d*x*x)/(a*a-d*d))*0.5))

def atraceb(d,a,x):
    return(a*0.5-(sqrt((d*d*a*a-d*d*d*d+4*d*d*x*x)/(a*a-d*d))*0.5))

#fonction d'actualisation, cette fonction à pour objectif de remmetre à jour le graphique dès que la valeur d'un curseur change
def update(val):
    ax1.cla()
    a=aS.val
    k=0
    cel=ce.val
    Dd=cel*100*dT.val/1000
    Ddp=Dd%lamb.val
    while k+cons < a/lamb.val-Ddp:#trace toutes les fonctions possibles 
        d=(k+cons)*lamb.val+Ddp #donne la nouvelle vaLeur de d
        ytraceh=[]
        ytraceb=[]
        ytracemh=[]
        ytracemb=[]
        i=0
        while i < len(Dx): #calcul et tracé de la courbe
            x=Dx[i]
            traceh=(a*0.5+(sqrt((d*d*a*a-d*d*d*d+4*d*d*x*x)/(a*a-d*d))*0.5))
            traceb=(a*0.5-(sqrt((d*d*a*a-d*d*d*d+4*d*d*x*x)/(a*a-d*d))*0.5))
            tracemh=(a*x/d)+a/2
            tracemb=(a*x/d)+a/2
            ytraceb.append(traceb)
            ytraceh.append(traceh)
            ytracemh.append(tracemh)
            ytracemb.append(tracemb)
            i=i+1
        ax1.plot(Dx,ytraceh,'b')
        ax1.plot(Dx,ytraceb,'b')
        ax1.plot(Dx,ytracemh,'r')
        ax1.plot(Dx,ytracemb,'g')
        k=k+1
    ax1.plot(0,0, marker="o", color="red") #place les points sources d'ondes sur le graphique
    ax1.plot(0,a, marker="o", color="red")
    ax1.axis([xmin, xmax, ymin_fixed, ymax_fixed]) #trace le grapfique et la grille
    ax1.grid()



#Conditions initiales
ModeA = 0

if ModeA == 0: #calcul pour l'eau
    cons=0.5 #cons dit si on recherche les zones d'interactions destructives(rentrer la valeur 0,5) ou constructives(0) 
    k=0      #
    pas=0.5
    i=0
    D=1
    x=0
    #calcul des limites de graphique
    ymin_fixed=-10
    ymax_fixed=20
    xmin=-20
    xmax=20

    #création de D (la liste Dx remplace x)
    Dx =[]
    D=xmin
    while D < xmax:
        Dx.append(D)
        D=D+pas
    ##créations des titres, légendes et sliders
    fig, (ax1) = plt.subplots(1, 1, figsize=(10, 5))
    ax1.axis([xmin, xmax, ymin_fixed, ymax_fixed])
    plt.xlabel('D en (cm)')
    plt.ylabel('y en (cm) ')
    if cons == 0:
        plt.title('zones d interactions constructives ')
    else:
        plt.title('zones d interactions destructives ')
    ax1.grid()
    ##les sliders permettent de modifier les valeurs de la distance entre les sources, la longueur d onde
    ##le déphasage temporel et célérité de l onde sans avoir à relancer le programme
    # Création d'un curseur, noté a, avec la position et les dimensions de ce curseur (rectangle_a)
    rectangle_a = plt.axes([0.25, 0.1, 0.5, 0.02])
    aS = Slider(rectangle_a, 'distance entre les sources (cm)', 1,20, valinit=10)
    # Création d'un curseur, noté lamb, avec la position et les dimensions de ce curseur (rectangle_b)
    rectangle_b = plt.axes([0.25, 0.13, 0.5, 0.02])
    lamb = Slider(rectangle_b, 'longueur d onde(cm)',0.5, 10, valinit=1)
    # Création d'un curseur, noté dT, avec la position et les dimensions de ce curseur (rectangle_c)
    rectangle_c = plt.axes([0.25, 0.16, 0.5, 0.02])
    dT = Slider(rectangle_c, 'déphasage temporel dT (ms)', 0, 200, valinit=0)
    # Création d'un curseur, noté c, avec la position et les dimensions de ce curseur (rectangle_d)
    rectangle_d = plt.axes([0.25, 0.19, 0.5, 0.02])
    ce = Slider(rectangle_d, 'célérité de l onde (m.s^-1)', 0.1, 1, valinit=0.5)
    aS.on_changed(update)
    lamb.on_changed(update)
    dT.on_changed(update)
    ce.on_changed(update)
    update(10)
    #Affichage
    ax1.grid()
    plt.tight_layout()
    plt.show()

#éléments de codes inutiles
#Tracé des courbes
#fig, ax = plt.subplots(figsize=(12,8))