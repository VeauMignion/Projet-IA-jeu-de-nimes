#-*- coding: utf-8 -*-

"""
Crée par HUMBERT le 25/04/24
simulation de gravitation facilité par les classes
"""
#ici tu met les imports...
import math

#et ici les variables globales en majuscules

class Astre:
    def __init__(self,nom,posx,posy,v,angl,mass,rayon):
        self.nom=nom
        self.x=posx
        self.y=posy
        self.vit=v
        self.direct=angl
        self.mass=mass
        self.taille=rayon
    
    def calculacc(self,):
        pass
    
class Univers(Astre):
    pass

        

