#26/03/24 solution second degré
from math import exp, expm1, sqrt,log
import random

def solfind(a,b,c):
    delta=b*b-4*a*c
    j=(-1)**0.5
    if delta >= 0:
        x1=(-b-sqrt(delta))/2*a
        x2=(-b+sqrt(delta))/2*a
    if delta < 0:
        x1=(-b-sqrt(abs(delta))*j)/2*a
        x2=(-b+sqrt(abs(delta))*j)/2*a
    return x1,x2

print(solfind(2,0,18))



    