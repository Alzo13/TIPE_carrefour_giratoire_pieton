# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 15:49:00 2022

@author: nicolas.vincent
"""
from Module_People import Vector

class Rond_Point():
    def __init__(self,r,rad,sens,q,b):
        """ Objet Rond-point """
        self.r = r       # Vecteur position
        self.rad = rad   # Rayon

        self.e = q       # Force de champ électrique
        self.b = b       # Force de champ magnétique

        self.sens = sens # Sens de rotation (+1 = trigonométrique ; -1 = horaire)
    
    def E(self,other)->Vector:
        """ Calcule le champ électrique en un point donné
        Entrée : self
                 other : point en lequel évaluer le champ
        Sortie : Vecteur champ électrique en other.r
        """
        if abs(other.r-self.r)*(abs(other.r-self.r) - self.rad - other.rad)**2 == 0 :
            # Pas de division par 0
            return Vector([0,0])

        # La distance calculée est celle de bordure à bordure
        # Décroissance en 1/r²
        return (self.r-other.r)*(2*self.rad*self.e/(abs(other.r-self.r)*(abs(other.r-self.r) - self.rad - other.rad)**2))

    def B(self,other)->float:
        """Calcule le champ magnétique à une coordonnée r
        Entrée : self
                 other : point en lequel évaluer le champ
        Sortie : Scalaire w représentant le vecteur (0,0,w)
        """
        if abs(other.r-self.r)*(abs(other.r-self.r) - self.rad - other.rad) == 0 :
            # Pas de division par 0
            return Vector([0,0])

        # La distance calculée est celle de bordure à bordure
        # Décroissance en 1/r
        return self.sens*self.b/(abs(self.r-other.r)-other.rad-self.rad)
    
    def get_forme(self,canvas):
        """ Renvoie l'ellipse tk représentant le rond-point après l'avoir dessinée sur le canvas 
        Entrée : self
                 canvas (Tk.canvas)
        Sortie : ellipse tkinter
        """
        return canvas.create_oval(self.r[0]-self.rad,
                                  self.r[1]-self.rad,
                                  self.r[0]+self.rad,
                                  self.r[1]+self.rad,
                                  outline = "black",
                                  fill = "#094535")