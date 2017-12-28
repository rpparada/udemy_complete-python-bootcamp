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
        # Estado 0 = inactivo, 1 = en juego (apuesta inicial hecha), 2 = gano, 3 = empato, 4 = perdio
        self.estado_jugador = 0
        self.lista_cartas_juego = []
        self.apuesta_actual = 0
    
    def dame_monto_inicial(self):
        return self.monto_inicial
    
    def dame_monto_restante(self):
        return self.monto_restante
    
    def dame_apuesta_inicial(self):
        return self.apuesta_inicial
    
    def dame_estado_jugador(self):
        return self.estado_jugador
    
    def dame_lista_cartas_juego(self):
        return self.lista_cartas_juego
    
    def dame_apuesta_actual(self):
        return self.apuesta_actual
    
    def definir_estado_jugador(self, nuevo_estado):
        if nuevo_estado == 0 or 1 or 2 or 3 or 4:
            self.estado_jugador = nuevo_estado
        else:
            print 'Estado desconosido, jugador %s mantendra su estado actual' %self.nombre
    
    def definir_apuesta_actual(self, monto):
        self.apuesta_actual = monto
        self.monto_restante -= monto
        
    def perdir_carta(self):
        pass
    
    def plantarce(self):
        pass
    
    def doblar_apuesta(self):
        pass
    
    def separar_cartas(self):
        pass
    
    
        