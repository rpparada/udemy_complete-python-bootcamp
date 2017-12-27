#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 23:23:16 2017

@author: Rodrigo Parada
"""
# Reglas extraidas desde http://www.casino.es/blackjack/como-jugar-blackjack/

from Crupier import Crupier
from MazoCartas import MazoCartas
from Jugador import Jugador

class Tablero(object):
    
    numero_max_jugadores = 7    
    
    def __init__(self):
        self.estado_juego = False
        self.lista_jugadores = []
        self.turno_jugador = 0
        self.crupier = None
        self.monto_inicial = 0
    
    def agrega_jugador(self, jugador):
        if len(self.lista_jugadores) < 7:
            self.lista_jugadores.append(jugador)
        else:
            print 'Numero Max de Jugadore es 7'
            
    def quitar_jugador(self, jugador):
        pass
    
    def iniciar_juego(self, mazo, crupier):
        if len(self.lista_jugadores) == 0:
            print 'Juego no puede comenzar, no hay jugadores'
        elif self.estado_juego:
            print 'Actualmente ya hay un juego en progreso'
        else:
            self.estado_juego = True
            self.mazo = mazo
            self.crupier = crupier
            self.turno_jugador = 0
            self.monto_inicial = 1000
    
    def muestra_estado(self):
        print ' ------------- Estado Juego --------------- '
        if self.estado_juego:
            print 'Estado Juego ......: Activo' 
        else:
            print 'Estado Juego ......: Inactivo' 
        if len(self.lista_jugadores) > 0:
            print 'Lista Jugadores ...: (%r)' %len(self.lista_jugadores)
            for jugador in self.lista_jugadores:
                print jugador.dame_nombre()
        else:
            print 'Lista Jugadores....: Vacia'
        
        if len(self.lista_jugadores) > 0 and self.turno_jugador < len(self.lista_jugadores):
            print 'Turno Jugador .....: %s ' %self.lista_jugadores[self.turno_jugador].dame_nombre()
            
        if self.crupier:
            print 'Crupier ...........: %s ' %self.crupier.dame_nombre()
        else:
            print 'Crupier ...........: Juego no tiene Crupier asignado'
        
        print 'Monto Inicial .....: %r ' %self.monto_inicial
            

tablero = Tablero()
tablero.muestra_estado()
rodrigo = Jugador("Rodrigo", 100)
juan = Jugador("Jugador", 200)
tablero.agrega_jugador(rodrigo)
tablero.agrega_jugador(juan)
tablero.iniciar_juego(MazoCartas(),Crupier("Pedro"))
tablero.muestra_estado()
    