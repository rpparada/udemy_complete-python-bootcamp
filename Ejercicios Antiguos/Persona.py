#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 21:05:16 2017

@author: Rodrigo Parada
"""

class Persona(object):
    
    def __init__(self, nombre):
        self.nombre = nombre
        
    def dame_nombre(self):
        return self.nombre
            
    def cambiarNombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre