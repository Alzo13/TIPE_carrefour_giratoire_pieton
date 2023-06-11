from math import sqrt, exp
from Module_Vector import Vector

Tau = 0.01 # Temps caractéristique de modélisation
entered = 0


class People():
    def __init__(self,m:float,q:float,r0:Vector,v0:Vector,va:float,ra:list,T:float,epsilon:list,color,rad:int) -> None:
        """ Objet Personne """
        
        # Propriétés
        self.rad = rad  # Taille du point
        self.m = m      # inertie
        self.q = q      # Charge

        # Dynamique
        self.va = va            # Vitesse souhaitée
        #self.ra = ra            # Point d'arrivée
        self.r = r0             # Position
        self.v = v0             # Vitesse
        self.a = Vector([0,0])  # Accélération
        self.T = T              # Temps de relaxation

        self.entered = False
        self.out = False

        # Propriétés de simulation
        self.t = 0          # Nombre de boucles passées dans la simulation
        #self.E = epsilon    # Distance d'arrivée

        # Attributs graphiques
        self.color = color  # Couleur du point


        self.check = 0 # Pour suivre un trajet
        self.dest = ra
        self.epsilonlist = epsilon
        self.ra = self.dest[0]
        self.E = self.epsilonlist[0]

    def update_acceleration(self,others,rplist,murs,coins,center):
        """ PFD sur le point
        Entrées :
            self : personne sur laquelle appliquer le PFD
            others : liste des autres personnes
            rplist : liste des rond-points
            murs : liste des murs
            coins : liste des coins
            center : vecteur coordonnées du centre
        Sortie : modifie l'accélération de la personne
        """
        ## BILAN DES FORCES :
        #  - Direction privilégiée
        sommeF = self.F_direction()

        #  - Distance sociale
        for o in others :
            sommeF = sommeF + self.F_repulsion_doc(o)
        
        #  - Rotation autour du rond-point
        for rp in rplist:
            sommeF += self.F_rondpoint_mag(rp)
        
        #  - Répulsion des murs et des coins
        """
        if abs(murs[0].r+murs[0].dir*1-self.r) < abs(murs[1].r+murs[1].dir*1 - self.r) :
            plusproches = [murs[0],murs[1]]
        else:
            plusproches = [murs[1],murs[0]]
        for m in murs :
            if abs(m.r+m.dir*1-self.r) < abs(plusproches[0].r+plusproches[0].dir*1 - self.r) :
                plusproches[1] = plusproches[0]
                plusproches[0] = m
        for m in plusproches:
            sommeF += self.F_mur(m)
        """ 
        plusproche = murs[0]  
        for m in murs :
            #décalage de 1 du centre de l'origines des murs car confondues sinon
            if abs(m.r+m.dir*1-self.r) < abs(plusproche.r+plusproche.dir*1 - self.r) : 
                plusproche = m
        sommeF += self.F_mur(plusproche)

        for c in coins :
            sommeF += self.F_coin(c,center)
        
        ## PFD
        self.a = sommeF/self.m
    
    def update(self):
        """ Mise à jour de la position de la personne par la méthode d'Euler
        Entrée : self (personne à mettre à jour)
        Sortie : Modifie le vecteur position self.r
        """
        global entered
        # Intégration première
        self.v += self.a*Tau
        self.v = min(self.v,self.v*self.va/abs(self.v)) # Majoration
        #self.v *= self.va/abs(self.v) # Renormalisation

        # Intégration seconde
        self.r += self.v*Tau

        self.t += 1 # Incrément du compteur de boucles
        
        if not self.entered and 335 < self.r[0] < 465 and 335 < self.r[1] < 465 :
            entered += 1
            self.entered = True
            if entered == 1 :
                print("Entrée : ",(self.t*Tau))
        if self.entered and not self.out and (335 > self.r[0] or self.r[0] > 465 or 335 > self.r[1] or self.r[1] > 450) :
            entered -= 1
            self.out = True
            if entered == 0 :
                print("Sortie : ",(self.t*Tau))

    def ea(self)->Vector:
        """ Direction privilégiée par la personne 
        Entrée : self
        Sortie : Vecteur unitaire de direction souhaitée
        """
        if abs(self.ra - self.r) == 0 :
            return Vector([0,0])
        else :
            return Vector(self.ra - self.r)/(abs(self.ra - self.r))

    def F_direction(self)->Vector:
        """ Force de direction 
        Entrée : self
        Sortie : Vecteur force poussant dans la direction souhaitée à la vitesse souhaitée
        """
        # Référence : Modelisation macroscopique de mouvements de foule, Aude Roudneff
        return  ((self.ea()*self.va - self.v))/(self.T)

    def F_repulsion_elec(self,other)->Vector:
        """Force de répulsion éléctrostatique 
        Entrée :    self : point sur lequel appliquer la force
                    other : objet générant le champ extérieur)
        Sortie : Vecteur force électrostatique s'appliquant à la surface des objets
        """ 
        if abs(other.r-self.r)*(abs(other.r-self.r) - self.rad - other.rad)**2 == 0 :
            # Pas de division par 0
            return Vector([0,0])

        # prise en compte du rayon de la personne (la force s'applique à la surface des points)
        return (self.r - other.r)/(abs(other.r-self.r)*(abs(other.r-self.r) - self.rad - other.rad)**2)*self.q*other.q

    # def F_rondpoint(self,rondpoint)->Vector:
    #     """ Force de rotation et d'attraction du rond point """
    #     Fattr = (self.r-rondpoint.r)*self.m*rondpoint.m/(abs(rondpoint.r-self.r)**3)*0.9 # Force radiale
    #     Frotate = (self.r - rondpoint.r)/((abs(self.r- rondpoint.r)-rondpoint.rad)**2)*(rondpoint.rad)*rondpoint.sens # Force orthoradiale 
    #     Frotate.coords = [Frotate.coords[1],-Frotate.coords[0]]
    #     return Frotate - Fattr

    
    def F_rondpoint_mag(self,rondpoint)->Vector:
        """ Force de champ électromagnétique du rond-point 
        Entrée :    self : objet sur lequel appliquer la force
                    rondpoint : générateur du champ
        Sortie : Vecteur force de Laplace dû au champ issu du rond-point
        """
        # Champ magnétique (rotation)
        Fmag = ((self.r-rondpoint.r)/abs(self.r-rondpoint.r)).vectorial(rondpoint.B(self))*abs(self.v) *self.q/2
        
        # Champ électrique (répulsion)
        Fmag += rondpoint.E(self)*-self.q 
        
        return Fmag
    
    def F_mur(self,mur)->Vector:
        """ Calcule la force de répulsion du mur 
        Entrée : self
                 mur : mur générant la force
        Sortie : Vecteur force
        """
        # Distance 
        d = mur.distance_algebrique(self)
        absd = abs(d)
        
        if absd == 0 :
            # Pas de division par 0
            return Vector([0,0])
        Frep = d/(abs(d)**2)
        Frep = Frep*self.q*100
        


        return Frep

    def F_repulsion_doc(self,other)->Vector: 
        """ Calcule la force de répulsion entre deux personnes 
        Entrée : self
                 other (autre personne)
        Sortie : Vecteur force de répulsion
        """
        if abs(self.r - other.r) == 0 :
            # Pas de division par 0
            return Vector([0,0])

        # Référence : Simulation of Pedestrian Crowds in Normal and Evacuation Situations, Dirk Helbing, Illés J. Farkas, Péter Molnar, and Taḿas Vicsek
        nij = ((self.r-other.r)/abs(self.r-other.r))    # vecteur unitaire orienté vers l'autre personne
        nij = (nij*6 + nij.vectorial(-1)*4)/10/sqrt(2)
        Ai = other.q*self.q                             # intensité de la répulsion
        Bi = 2                                          # Facteurs sociaux
        l = 0.69                                        # largeur de champ
        cosphi = -(nij.scalar(self.v)/abs(self.v))      # cosinus de l'angle entre le vecteur vitesse et le vecteur nij 

        return  nij * (l + (1-l)*(1+cosphi)/2) * Ai * exp(((self.rad + other.rad) - abs(self.r-other.r))/Bi)

    def F_coin(self,coin,center)->Vector:
        """ Calcule la force de répulsion du coin - permet d'éviter de traverser les murs aux discontinuités et le piéton
        est plus repoussé par les coins
        Entrée : self
                 coin : coin générant la force
        Sortie : Vecteur force
        """

        if abs(coin.r-self.r)*(abs(coin.r-self.r) - self.rad - coin.rad)**2 == 0 :
            # Pas de division par 0
            return Vector([0,0])
        
        # prise en compte du rayon de la personne (la force s'applique à la surface des points)
        F = (self.r - coin.r)/(abs(coin.r-self.r)*(abs(coin.r-self.r) - self.rad - coin.rad))*self.q*coin.q/10
    
        # On oblige la force à pointer vers le centre
        return (Vector(center)-self.r)/abs(Vector(center)-self.r) * F.norme()

    def arrive(self)->bool:
        """ Détecte si la personne est arrivé à une distance inférieure à self.E de la position voulue
        Entrée : self
        Sortie : Booléen
        """
        if self.r.distance(self.ra) < self.E :
            self.check += 1
            if self.check < len(self.dest)  :
                self.ra = self.dest[self.check]
                self.E = self.epsilonlist[self.check]
                return False
            return True
        return False

    def get_forme(self,canvas):
        """ Renvoie l'ellipse tk représentant la personne après l'avoir dessinée sur le canvas 
        Entrée : self
                 canvas (Tk.canvas)
        Sortie : ellipse tkinter
        """
        return canvas.create_oval(self.r[0]-self.rad,
                                  self.r[1]-self.rad,
                                  self.r[0]+self.rad,
                                  self.r[1]+self.rad,
                                  fill = self.color)
