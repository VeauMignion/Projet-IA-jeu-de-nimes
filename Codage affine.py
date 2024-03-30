Mode=2 #0 pour encrypter, 1 pour décrypter, 2 pour calculer une clé

alph=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#Décodeur 29/01/24
motadec=["T","A","X","G","U","J","A","J","S","A","V","V","A"]
nmot=[]
nlet=0
while nlet<len(motadec):
    trouv=0
    test=0
    while trouv==0:
        if motadec[nlet]==alph[test]:
            nmot.append(test)
            trouv=1
        else:
            test=test+1
    nlet=nlet+1

nlet=0
motdec=[]
while nlet<len(nmot):
    nletcorresp=(19*nmot[nlet]+4)%26
    motdec.append(alph[nletcorresp])
    nlet=nlet+1

if 1==Mode:
    print(nmot)
    print("######################")
    print(motdec)

#Codeur:
motacod=["M","A","T","H","S"]
nmot=[]
nlet=0
while nlet<len(motacod):
    trouv=0
    test=0
    while trouv==0:
        if motacod[nlet]==alph[test]:
            nmot.append(test)
            trouv=1
        else:
            test=test+1
    nlet=nlet+1

nlet=0
motcod=[]
while nlet<len(nmot):
    nletcorresp=(11*nmot[nlet]+8)%26
    motcod.append(alph[nletcorresp])
    nlet=nlet+1

if 0==Mode:
    print(nmot)
    print("@@@@@@@@@@@@@@@@@@@@@@@@")
    print(motcod)

#Trouver clé de codage
infos=["E","M","P","P"]
nlet=0
nmot=[]
while nlet<len(infos):
    trouv=0
    test=0
    while trouv==0:
        if infos[nlet]==alph[test]:
            nmot.append(test)
            trouv=1
        else:
            test=test+1
    nlet=nlet+1

print(nmot)

#(nmot[1]-nmot[3])a==(nmot[2]-nmot[4])|[26]

#Méthode tests multiples
trouv=0
a=0
while trouv==0:
    if ((nmot[1]-nmot[3])*a-(nmot[2]-nmot[4]))%26==0:
        trouv=1
    else:
        a=a+1

#nmot[1]*a+b==nmot[2]|[26]
trouv=0
while trouv==0:
    trouv=1

