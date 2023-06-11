from math import sqrt, acos

class Vector():
    def __init__(self,coords) -> None:
        """ Objet Vecteur """
        # Coords est une liste de flottants
        self.coords = coords

    def __len__(self):
        """ Renvoie la dimension du vecteur """
        return len(self.coords)

    def __str__(self)->str:
        """ Conversion en chaîne de caractères """
        string = "("
        for i in range(len(self)):
            string += str(self[i])
            if i < len(self.coords)-1 :
                string += ";"
        string += ")"
        return string

    def norme(self)->float:
        """ Renvoie la norme d'un vecteur """
        res = 0
        for i in range(len(self)):
            res += self[i]**2
        return sqrt(res)

    def pos(self):
        """ Renvoie un vecteur dont les composantes sont les valeurs absolue de celles du vecteur entré """
        coords = []
        for i in range(len(self)):
            coords.append(abs(self[i]))
        return Vector(coords)


    def __lt__(self,other)->bool:
        return abs(self) < abs(other)

    def __add__(self,other):
        """ Addition de deux vecteurs """
        coords = []
        for i in range(len(self)):
            coords.append(self[i]+other[i])
        return Vector(coords)

    def __sub__(self,other):
        """ Soustraction de deux vecteurs """
        coords = []
        for i in range(len(self)):
            coords.append(self[i]-other[i])
        return Vector(coords)

    def __mul__(self,other):
        """ Multiplication de deux vecteurs compostante par composante / Multiplication par un flottant (à droite uniquement) """
        coords = []
        if isinstance(other,Vector):
            for i in range(len(self)):
                coords.append(self[i]*other[i])
        else :
            for i in range(len(self)):
                coords.append(self[i]*other)
        return Vector(coords)

    def __truediv__(self,other):
        """ Division de deux vecteurs compostante par composante / Division par un flottant (à droite uniquement) """
        coords = []
        if isinstance(other,Vector):
            for i in range(len(self)):
                coords.append(self[i]/other[i])
        else :
            for i in range(len(self)):
                coords.append(self[i]/other)
        return Vector(coords)
    
    def __getitem__(self,i):
        """ Accès à une coordonnée """
        return self.coords[i]

    def __setitem__(self,i,v):
        """ Changement d'une coordonnée """
        self.coords[i] = v

    def __abs__(self):
        """ Renvoie la norme d'un vecteur """
        return self.norme()

    def distance(self,other)->float:
        """ Renvoie la distance à un autre vecteur """
        return abs(self-other)
    
    def __pow__(self,k):
        """ Elève chaque composante à la puissance k """
        coords = []
        for i in range(len(self.coords)):
            coords.append(self[i]**k)
        return Vector(coords)
    
    def __len__(self)->int:
        """ Renvoie la dimension du vecteur """
        return len(self.coords)
        
    def scalar(self,other):
        """ Produit scalaire entre deux vecteurs """
        return sum((self*other).coords)
    
    def angle(self):
        """ Renvoie l'angle formé entre le vecteur et le vecteur horizontal """
        if abs(self) == 0 :
            return 0
        sign = -1 if self.coords[1] < 0 else 1
        return acos(self.scalar(Vector([1,0]))/abs(self))*sign
    
    def vectorial(self,w):
        """ Calcule le produit vectoriel entre deux vecteurs self ^ w
        On considère que le vecteur self est dans le plan (x,y)
        que le vecteur w = (0,0,w)
        """
        coords = [0,0]
        coords[0] = self.coords[1]*w
        coords[1] = -self.coords[0]*w
        return Vector(coords)
        
    
    def draw(self,x,y,canvas):
        return canvas.create_line(x,
                                  y,
                                  x+self.coords[0],
                                  y+self.coords[1])

    