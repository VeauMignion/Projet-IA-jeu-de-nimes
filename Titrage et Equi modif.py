# Créé par HUMBERT, le 26/09/2023 en Python 3.7
from pylab import *

print("")
print("**********************************************************")
print("*  Quantites de matiere et titrage                       *")
print("*  Reaction support du titrage :                         *")
print("* MnO4(-) + 5Fe(2+) + 8H(+) ---> Mn(2+) + 5Fe(3+) + 4H2O *")
print("*********************************************Hatier 2020**")

### A MODIFIER : DONNEES ###
### Concentration de la solution titree en mol/L
c1=0.0150
### Volume de solution titree en mL
V1=20.0
### Concentration de la solution titrante en mol/L
c=0.005
### Volume maximal affiche en mL
Vmax=25.0

### A MODIFIER (questions 2 et 3) : CALCULS ###
### Quantite de matiere apportee de reactif titre en mol
nFe2=c1*V1*1e-3

#Avancement à l'équivalance en mol
AvE=nFe2/5

### Volume equivalent en mL;
Ve=(AvE)/(c*1e-3)

### Quantite de matiere de MnO4- a Vmax en mol
nMnO4=c*(Vmax-Ve)*1e-3

#Quantité de matiere de Mn(2+) a Ve et Vmax en mol
nMn2=AvE

#Quantité de matiere de Fe(3+) a Ve et Vmax en mol
nFe3=5*AvE

### A MODIFIER (questions 2 et 3) : LISTES ###
V=[0,Ve,Vmax]
nFe2l=[nFe2,0,0]
nMnO4l=[0,0,nMnO4]
nFe3l=[0,nFe3,nFe3]
nMn2l=[0,nMn2,nMn2]


### A MODIFIER (questions 2b et 3) : TRACES ###
plot(V,nFe2l,"r",label=" Ion Fe2+ ")
plot(V,nMnO4l,"b",label=" Ion MnO4- ")
plot(V,nFe3l,"pink",label=" Ion Fe3+ ")
plot(V,nMn2l,"cyan",label=" Ion Mn2+ ")


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
