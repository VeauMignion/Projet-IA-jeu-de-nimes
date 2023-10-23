# Créé par HUMBERT, le 23/10/2023 en Python 3.7
#créé par HUMBERT, le 21/10/2023
#importations
from matplotlib import pyplot as plt
from math import exp, expm1, sqrt
from matplotlib.widgets import Slider
from matplotlib.gridspec import GridSpec
##le but de ce programme est de modéliser les zones où les interactions entre les ondes sont destructrices ou constructives, en fonction de:
##le mode ondes sur l'eau:                                le mode lumière:
##a la distance entre les sources des ondes (cm)          (micro m)
##lamb la longeur d'onde (cm)                             (nm)(400-800)
##dT le déphasage temporel (micro s)                       =0
##c la célérité de l'onde (m.s^-1)                         =300 000 000m.s^-1
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

#fonction d'actualisation
def update(val):
    a=aS.val
    plt.cla()
    k=0
    while k+cons < a/lamb.val:
        d=k+cons
        ytraceh=[]
        ytraceb=[]
        i=0
        while i < len(Dx):
            x=Dx[i]
            traceh=(atraceh(d,a,x))
            traceb=(atraceb(d,a,x))
            ytraceb.append(traceb)
            ytraceh.append(traceh)
            i=i+1
        plt.plot(Dx,ytraceh,'r')
        plt.plot(Dx,ytraceb,'b')
        k=k+1



#Conditions initiales
ModeA = 0

if ModeA == 0: #calcul pour l'eau
    cons=0.5
    k=0
    pas=0.01
    i=0
    D=1
    x=0
    #calcul des limites de graphique
    ymin=-10
    ymax=20
    xmin=-20
    xmax=20

    #création de D
    Dx =[]
    D=xmin
    while D < xmax:
        Dx.append(D)
        D=D+pas

    #Tracé des courbes
    fig, ax = plt.subplots(figsize=(12,8))
    fig.subplots_adjust(bottom=0.3)
    plt.axis([xmin,xmax,ymin,ymax])
    plt.xlabel('D en (cm)')
    plt.ylabel('y en (cm) ')
    if cons == 0:
        plt.title('zones d interactions constructives ')
    else:
        plt.title('zones d interactions destructives ')
    plt.grid()
    plt.legend()
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
    c = Slider(rectangle_d, 'célérité de l onde (m.s^-1)', 0.1, 1, valinit=0.5)
    plt.show()
    aS.on_changed(update)
    lamb.on_changed(update)
    dT.on_changed(update)
    c.on_changed(update)
    #Affichage