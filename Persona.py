#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 21:05:16 2017

@author: rodrigoparada
"""

class Persona(object):
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def indicarNombre(self):
        print(self.nombre)
        
    def cambiarNombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre