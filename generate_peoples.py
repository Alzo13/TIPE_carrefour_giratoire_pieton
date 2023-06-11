from Module_Vector import *
from Module_People import *
from world import *
from random import *

### FONCTIONS

def neighbours(list,elt,delta):
    """ Renvoie la liste des personnes à une distance inférieure à delta """
    ret = []
    for e in list :
        if e != elt and e.r.distance(elt.r) < delta:
            ret.append(e)
    return ret

def generatepeople_random(T):
    """ Génère une personne aléatoire """
    return People(0.2,0.2,Vector([randint(0,width),randint(0,height)]),Vector([0,0]),50,Vector([randint(0,width),randint(0,height)]),T,random()+1*10,"gray",4)

def generatepeople_crowd(T,deltax,deltay,x,y,path):
    """ Génère une personne dans la zone supérieure cherchant à aller dans la zone inférieure, au milieu +- delta """
    return People(0.02,10,Vector([randint(x-deltax,x+deltax),randint(y-deltay,y+deltay)]),Vector([0,1]),36,path,T,[50,10],"gray",7.5)

##########

peoples = []

colors = {(0,1):"green",(0,2):"cyan",(0,3):"turquoise",(1,0):"red",(1,2):"orange",(1,3):"maroon",
          (2,0):"blue",(2,1):"purple",(2,3):"pink",(3,0):"yellow",(3,1):"gray",(3,2):"dark gray"}



  # Version carrefour à 4 directions
choicesfrom = [(30,20,100,400),(30,20,700,400),(20,30,400,100),(20,30,400,700)]
#choicesto = [(100,400),(700,400),(400,100),(400,700)]
choicesto = [(200,385), # Sortie à gauche
             (600,415), # Sortie à droite
             (435,200), # Sortie en haut
             (365,600)] # Sortie en bas


#choicesfrom = [(100,20,50,400)]
#choicesto = [(400,100)]

#for i in range(10):
#    from_ = choice(choicesfrom)
#    to_ = choice(choicesto)
#    peoples.append(generatepeople_crowd(50,from_[0],from_[1],from_[2],from_[3],to_[0],to_[1]))
#    peoples[-1].color = "magenta"


# Version carrefour à 2 directions 
#for i in range(15):
#    peoples.append(generatepeople_crowd(50,100,40,50,400,1000,400))
#    peoples[-1].color = "red"
#    peoples.append(generatepeople_crowd(50,100,40,750,400,-200,400))
#    peoples[-1].color = "blue"

# Version carrefour à 4 directions
for i in range(2):

    for f in range(4) :
        for t in range(4) :
            if t != f :
                from_ = choicesfrom[f]
                to_ = choicesto[t]
                peoples.append(generatepeople_crowd(5,from_[0],from_[1],from_[2],from_[3],[Vector([width/2,height/2]),Vector([to_[0],to_[1]])]))
                peoples[-1].color = colors[(f,t)]
                i += 1

# for f in range(2) :
#     from_ = choicesfrom[f]
#     to_ = choicesto[f-1]
#     peoples.append(generatepeople_crowd(5,from_[0],from_[1],from_[2],from_[3],[Vector([width/2,height/2]),Vector([to_[0],to_[1]])]))
#     peoples[-1].color = colors[(f,(f-1)%4)]

