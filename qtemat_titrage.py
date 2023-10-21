from pylab import *

print("")
print("*************************************")
print("*  Quantites de matiere et titrage  *")
print("*  Reaction support du titrage :    *")
print("*        H3O+ + HO- --> 2 H2O       *")
print("************************Hatier 2020**")

print("")
print("Attention : le separateur decimal est le point")
print("")

### A MODIFIER : DONNEES ###
### Concentration de la solution titree en mol/L
c1=0.120
### Volume de solution titree en mL
V1=10.0
### Concentration de la solution titrante en mol/L
c=0.1
### Volume maximal affiche en mL
Vmax=25.0

### A MODIFIER (questions 2 et 3) : CALCULS ###
### Quantite de matiere apportee de reactif titre en mol
ntitrei=c1*V1*1e-3
### Volume equivalent en mL
Ve=(c1*V1)/c
### Quantite de matiere de reactif titrant a Vmax en mol
ntitrantmax=c*(Vmax-Ve)*1e-3
#quantitées de Na et Cl
nNainit=ntitrei
nNae=ntitrei
nNafin=ntitrei
nCle=Ve*c*1e-3
nClfin=Vmax*c*1e-3

### A MODIFIER (questions 2 et 3) : LISTES ###
V=[0,Ve,Vmax]
ntitre=[ntitrei,0,0]
ntitrant=[0,0,ntitrantmax]
nNa=[nNainit,nNae,nNafin]
nCL=[0,nCle,nClfin]

### A MODIFIER (questions 2b et 3) : TRACES ###
plot(V,ntitre,"r",label="Reactif titre")
plot(V,ntitrant,"b",label="Reactif titrant")
plot(V,nNa,"y",label="Ion sodium")
plot(V,nCL,"pink",label="Ion Clhorure")

### NE PAS MODIFIER ###

### Ecriture des resultats
print("")
print("Volume equivalent :",round(Ve,2),"mL")
### Mise en forme des graphes
xlabel("V (en mL)")
ylabel("Quantites de matiere (en mol)")
legend()
grid(True)
show()

