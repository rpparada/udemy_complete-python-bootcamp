#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 22:53:03 2017

@author: Rodrigo Parada
"""

from Persona import Persona

class Jugador(Persona):
    
    def __init__(self, nombre, monto_inicial):
        Persona.__init__(self, nombre)
        self.monto_inicial = monto_inicial
        self.monto_restante = monto_inicial
    
    def monto_inicial(self):
        return self.monto_inicial
    
    def monto_restante(self):
        return self.monto_restante
    
    def perdir_carta(self):
        pass
    
    def plantarce(self):
        pass
    
    def doblar_apuesta(self):
        pass
    
    def separar_cartas(self):
        pass
    
    
        