import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
from matplotlib.gridspec import GridSpec
#Fonction d'actualisation des courbes
def update(val):
    '''
    Fonction qui permet d'actualiser la droite de modÃ©lisation
     et son Ã©quation, en fonction de la valeur du curseur
    '''
    y1=A.val*np.cos(2*np.pi/T.val*time)
    p1.set_ydata(y1)
    y2=A.val*np.cos(2*np.pi/T.val*time+PHI.val)
    p2.set_ydata(y2)
    y3=y1+y2
    p3.set_ydata(y3)


#Conditions initiales
initial_A = 1.00
initial_T = 2.00
initial_PHI = np.pi
# DÃ©finitions des courbes
time=np.linspace(0.,20.,2000)
y1=initial_A*np.cos(2*np.pi/initial_T*time)
y2=initial_A*np.cos(2 * np.pi / initial_T * time + initial_PHI)
y3=y1+y2
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
