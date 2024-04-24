#Idée du 06/04/24
#L'IA se défini par une liste calques: ces calques modélisent une situation que l'IA a affronté 
#(avec un système de coin indenté pour ne pas tenir compte des rotations) et s'accompagnent de probabilitées sur les coups que l'IA peut jouer 
#(qui s'adaptent en fonction des victoires et échecs de l'IA) quand l'IA affronte une situation qu'elle ne connaît pas, 
#elle cherche le calque le plus proche et joue selon ses probabilités (et elle crée un calque de la situation inconnue)
#créé le 13/04/24 par Paul HUMBERT
#pour plus d'infos voir documentation-IA-morpion.pdf


#on remet à 0 les IAS:
def resetIAS():
    ncalIA1=[] #liste de tout les numéros des calques
    

