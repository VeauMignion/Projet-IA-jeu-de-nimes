#créé par HUMBERT, le 21/10/2023
#importations 

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

 

#Conditions initiales
ModeA = 0

if ModeA == 0: #calcul pour l'eau
    a=10
    lamb=2
    dT=0
    c=0.5
    ai=a
    lambi=lamb
    dTi=dT
    ci=c
    cons=0.5
    k=0
    pas=0.01
    i=0
    D=1
    x=0
    while 0==0:
        # Création d'un curseur, noté a, avec la position et les dimensions de ce curseur (rectangle_a)
        rectangle_a = plt.axes([0.25, 0.1, 0.5, 0.02])
        Sla = Slider(rectangle_a, 'distance entre les sources (cm)', 1,20, valinit=ai)
        # Création d'un curseur, noté lamb, avec la position et les dimensions de ce curseur (rectangle_b)
        rectangle_b = plt.axes([0.25, 0.155, 0.5, 0.02])        
        lamb = Slider(rectangle_b, 'longueur d onde(cm)',0.5, 10, valinit=lambi)        
        # Création d'un curseur, noté dT, avec la position et les dimensions de ce curseur (rectangle_c)
        rectangle_c = plt.axes([0.25, 0.210, 0.5, 0.02])
        dT = Slider(rectangle_c, 'déphasage temporel dT (ms)', 0, 200, valinit=dTi)
        # Création d'un curseur, noté c, avec la position et les dimensions de ce curseur (rectangle_d) 
        rectangle_d = plt.axes([0.25, 0.265, 0.5, 0.02])
        dT = Slider(rectangle_d, 'célérité de l onde (m.s^-1)', 0.1, 1, valinit=ci)
        
        #calcul des limites de graphique
        a = Sla.val
        ymin=-10
        ymax=a+10
        xmin=-20
        xmax=20

        #création de D
        Dx =[]
        D=xmin
        while D < xmax:
            Dx.append(D)
            D=D+pas

        #Tracé des courbes
        G = GridSpec(10, 8)
        fig, ax = plt.subplots(figsize=(12,8))
        plt.axis([xmin,xmax,ymin,ymax])
        plt.xlabel('D en (cm)')
        plt.ylabel('y en (cm) ')
        if cons == 0:
            plt.title('zones d interactions constructives ')
        else:
            plt.title('zones d interactions destructives ') 
        plt.grid()
        while k+cons < a/lamb.val:
            d=k+cons
            ytraceh=[]
            ytraceb=[]
            i=0
            while i < len(Dx):
                x=Dx[i]
                traceh= a*0.5+(sqrt((d*d*a*a-d*d*d*d+4*d*d*x*x)/(a*a-d*d))*0.5)
                traceb= a*0.5-(sqrt((d*d*a*a-d*d*d*d+4*d*d*x*x)/(a*a-d*d))*0.5)
                ytraceb.append(traceb)
                ytraceh.append(traceh)
                i=i+1
            plt.plot(Dx,ytraceh,'r')
            plt.plot(Dx,ytraceb,'b')
            k=k+1
        plt.legend()
        #Affichage
        plt.show()  