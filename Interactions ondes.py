#créé par HUMBERT, le 21/10/2023
#importations 
import numpy  as np
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
#

#Conditions initiales
ModeA = 0

if ModeA == 0: #calcul pour l'eau
    a=10
    lamb=2
    dT=0
    c=0.5


#TracÃ© des courbes
G = GridSpec(10, 8)
fig, ax = plt.subplots(figsize=(12,8))
axes_1 = plt.subplot(G[:-3, :])
plt.axis([0,20,-10,10])
plt.xlabel('$t$ (s)')
plt.ylabel('Amplitude ')
plt.title('Somme de deux ondes sinusoÃ¯dales synchrones ')
plt.grid()
p1, = plt.plot(time, y1, '-g',label=r'$y_1 = A \times \cos( \frac{2\pi}{T}\times t)$')
p2, = plt.plot(time, y2, '-b',label=r'$y_2 = A \times \cos( \frac{2\pi}{T}\times t + \Phi)$')
p3, =  plt.plot(time, y3, '-r',label=r'$y_3= y_1 + y_2$')
plt.legend()
################################################################################
#Sliders
################################################################################
# CrÃ©ation d'un curseur, notÃ© T, avec la position et les dimensions de ce curseur (rectangle_a)
rectangle_a = plt.axes([0.25, 0.1, 0.5, 1])
T = Slider(rectangle_a, 'PÃ©riode $T$ (s)', 1,10, valinit=initial_T)
# CrÃ©ation d'un curseur, notÃ© A, avec la position et les dimensions de ce curseur (rectangle-b)
rectangle_b = plt.axes([0.25, 0.155, 0.5, 0.02])
A = Slider(rectangle_b, 'Amplitude $A$ (m)', 0, 5, valinit=initial_A)
# CrÃ©ation d'un curseur, notÃ© PHI, avec la position et les dimensions de ce curseur (rectangle_c)
rectangle_c = plt.axes([0.25, 0.210, 0.5, 0.02])
PHI = Slider(rectangle_c, 'Phase $\phi$ (rad)', 0, 7, valinit=initial_PHI)
# appel de la fonction update lorsque le curseur est actionnÃ©
A.on_changed(update)
T.on_changed(update)
PHI.on_changed(update)
#Affichage
print(np.pi)
plt.show()



