from Module_Vector import Vector

class Mur():
    def __init__(self,r:Vector,direction:Vector,longueur:int,normale:Vector):
        self.r = r                                              # Vecteur position de l'origine
        self.dir = direction                                    # Vecteur direction du segment
        self.rep = Vector([direction[1],direction[0]]).pos()    # direction orthogonale
        self.l = longueur                                       # longueur du mur
        self.normale = normale                                  # Normale au mur

    def get_forme(self,canvas):
        """ Renvoie le segment tk représentant le mur après l'avoir dessiné sur le canvas 
        Entrée : self
                 canvas (Tk.canvas)
        Sortie : ligne tkinter
        """
        return canvas.create_line(self.r[0],
                                  self.r[1],
                                  (self.r+self.dir*self.l/abs(self.dir))[0],
                                  (self.r+self.dir*self.l/abs(self.dir))[1])

    def distance_algebrique(self,other):
        """ Calcule le projeté de other.r - self.r selon la direction orthogonale au mur
        Entrée : self (mur)
                 other : personne
        Sortie : Vecteur
        """
        dp = self.rep * self.rep.scalar(other.r)
        #print( self.rep)
        dp = dp.pos() - self.rep*other.rad
        dr = (self.r-other.r).pos() - self.rep*other.rad
        if abs(dp)>abs(dr):
            d = dp
        else:
            d = dr
        if self.r[0] > 400 and self.r[0] > other.r[0]:
            return d*-1
        if self.r[0] < 400 and self.r[0] < other.r[0] :
            return d
        if self.r[1] > 400 and self.r[1] > other.r[1] :
            return d*-1
        if self.r[1] < 400 and self.r[1] < other.r[1] :
            return d
        return Vector([0,0])
        

class Coin():
    def __init__(self,r,q,rad):
        """ Objet coin (compense les discontinuités du mur) """
        self.r = r      # Vecteur position
        self.rad = rad  # Rayon
        self.q = q      # Charge
    
    def get_forme(self,canvas):
        """ Renvoie l'ellipse tk représentant le coin après l'avoir dessinée sur le canvas 
        Entrée : self
                 canvas (Tk.canvas)
        Sortie : ellipse tkinter
        """

        return canvas.create_oval(self.r[0]-self.rad,
                                  self.r[1]-self.rad,
                                  self.r[0]+self.rad,
                                  self.r[1]+self.rad)
class sol_mur():
    def __init__(self,r,dir):
        """Objet de mur colorié"""
        self.r=r
        self.dir=dir
        
    def get_forme(self,canvas):
        """Renvoie le rectangle tk représentant le coin après l'avoir dessinée sur le canvas 
        Entrée : self
                 canvas (Tk.canvas)
        Sortie : rectangle tkinter"""
        
        return canvas.create_rectangle(self.r[0],
                                  self.r[1],
                                  self.r[0]+380*self.dir[0],
                                  self.r[1]+380*self.dir[1],
                                  outline = "black",
                                  fill = "grey")
        