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
        self.monto_actual = 0
    
    def dame_turno(self):
        return self.turno_jugador
    
    def dame_estado_juego(self):
        return self.estado_juego
    
    def dame_listado_jugadores(self):
        return self.lista_jugadores
    
    def dame_monto_inicial(self):
        return self.monto_inicial
    
    def dame_monto_actual(self):
        return self.monto_actual
    
    def agrega_jugador(self, jugador):
        if len(self.lista_jugadores) < 7:
            self.lista_jugadores.append(jugador)
        else:
            print 'Numero Max de Jugadore es 7'
            
    def quitar_jugador(self, jugador):
        pos = self.dame_posicion_jugador(jugador)
        if pos != None:
            self.lista_jugadores.pop(pos)
        else:
            print 'Jugador no encontrado'
        
    def dame_posicion_jugador(self, nombre):
        for indice,jugador in enumerate(self.lista_jugadores):
            if jugador.dame_nombre() == nombre:
                return indice
        
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
            

# Crea objeto tablero
tablero = Tablero()

# Muestra estado actual del juego en tablero
tablero.muestra_estado()

# Crea jugador Rodrigo con 100 puntos de juego y lo agregar al actual juego sin iniciar
rodrigo = Jugador("Rodrigo", 100)
tablero.agrega_jugador(rodrigo)

# Crea jugador Juan con 200 puntos de juego y lo agregar al actual juego sin iniciar
juan = Jugador("Juan", 200)
tablero.agrega_jugador(juan)

# Crea crupier llamado Pedro
crupier = Crupier("Pedro")

# Crea mazo de juego
mazo = MazoCartas()

# Inicia juego en objeto tabla asignado el mazo y crupier 
tablero.iniciar_juego(mazo, crupier)

# Muestra estado actual del juego en tavlero
tablero.muestra_estado()

# Quitar jugador Rodrigo
tablero.quitar_jugador('Rodrigo')

# Muestra estado actual del juego en tavlero
tablero.muestra_estado()
    