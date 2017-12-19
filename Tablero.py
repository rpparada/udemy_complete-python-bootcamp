#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 23:23:16 2017

@author: Rodrigo Parada
"""
# Reglas extraidas desde http://www.casino.es/blackjack/como-jugar-blackjack/

from Crupier import Crupier

class Tablero(object):
    
    numero_max_jugadores = 7    
    
    def __init__(self, crupier = Crupier("Carlos"), monto_incial = 0):
        self.estado_juego = False
        self.lista_jugadores = []
        self.lista_cartas_activas = []
        self.lista_cartas_inactivas = []
        self.turno_jugador
        self.crupier = crupier
        self.monto_inicial = monto_incial
    
    def agrega_jugador(self, jugador):
        if self.lista_jugadores.count() < 7:
            self.lista_jugadores.append(jugador)
        else:
            print 'Numero Max de Jugadore es 7'
    
    def iniciar_juego(self, numero_juegos_cartas):
        if self.lista_jugadores.count() == 0:
            print 'Juego no puede comenzar, no hay jugadores'
        elif self.estado_juego:
            print 'Actualmente ya hay un juego en proceso'
        elif numero_juegos_cartas < 0:
            print 'Numero de Juego de Cartas debe ser mayor que 0'
        else:
            self.estado_juego = True
            self.lista_cartas_activas = 
            self.lista_cartas_inactivas[:] = []
            self.turno_jugador = 0
            self.monto_inicial = 1000
    
    