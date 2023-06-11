# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 15:47:55 2023

@author: nicolas.vincent
"""

from Module_Window import *
from Module_Rond_Point import *
from Module_Murs import *

width,height = 800,800
window = Window(width,height)





rplist = []

rplist.append(Rond_Point(Vector([width/2,height/2]),7.5,-1,9,2))



for rp in rplist :
    rp.get_forme(window.canvas)
murs = []
#30px = 1m
murs.append(Mur(Vector([347.5,362.5]),Vector([-1,0]),380,Vector([0,1])))
murs.append(Mur(Vector([347.5,437.5]),Vector([-1,0]),380,Vector([0,-1])))
murs.append(Mur(Vector([347.5,362.5]),Vector([0,-1]),380,Vector([1,0])))
murs.append(Mur(Vector([452.5,362.5]),Vector([0,-1]),380,Vector([-1,0])))
murs.append(Mur(Vector([452.5,362.5]),Vector([1,0]),380,Vector([0,1])))
murs.append(Mur(Vector([452.5,437.5]),Vector([1,0]),380,Vector([0,-1])))
murs.append(Mur(Vector([347.5,437.5]),Vector([0,1]),380,Vector([1,0])))
murs.append(Mur(Vector([452.5,437.5]),Vector([0,1]),380,Vector([-1,0])))


for m in murs :
    m.get_forme(window.canvas)


sol_murs = []

sol_murs.append(sol_mur(Vector([347.5,362.5]),[-1,-1]))
sol_murs.append(sol_mur(Vector([347.5,437.5]),[-1,1]))
sol_murs.append(sol_mur(Vector([452.5,362.5]),[1,-1]))
sol_murs.append(sol_mur(Vector([452.5,437.5]),[1,1]))

for s in sol_murs :
    s.get_forme(window.canvas)

coins = []

coins.append(Coin(Vector([342.5,442.5]),18,5))
coins.append(Coin(Vector([457.5,442.5]),18,5))
coins.append(Coin(Vector([342.5,357.5]),18,5))
coins.append(Coin(Vector([457.5,357.5]),18,5))

for c in coins :
    c.get_forme(window.canvas)
    
