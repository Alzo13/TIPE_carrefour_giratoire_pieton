# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 15:24:05 2022

@author: nicolas.vincent
"""

import tkinter as tk


class Window(tk.Tk):
    """ Classe Fenêtre"""
    def __init__(self,width,height):
        super().__init__()
        # Création du canvas (rempli de blanc)
        self.canvas = tk.Canvas(self, width = width, height=height, bg="white")
        self.canvas.pack()
    
