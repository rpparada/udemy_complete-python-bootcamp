#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 23:23:16 2017

@author: Rodrigo Parada
"""
# Reglas extraidas desde http://www.casino.es/blackjack/como-jugar-blackjack/

# Importando clases propias
from Crupier import Crupier
from MazoCartas import MazoCartas
from Jugador import Jugador

# Importando para limpiar consola
import os

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
            if len(self.lista_jugadores) == 0:
                self.reset_juego()
            elif self.turno_jugador == len(self.lista_jugadores):
                self.turno_jugador = 0
        else:
            print 'Jugador no encontrado'
            
    def reset_juego(self):
        self.estado_juego = False
        self.lista_jugadores = []
        self.turno_jugador = 0
        self.crupier = None
        self.monto_inicial = 0
        self.monto_actual = 0
        
    def dame_posicion_jugador(self, nombre):
        for indice,jugador in enumerate(self.lista_jugadores):
            if jugador.dame_nombre() == nombre:
                return indice
        
    def abre_juego(self, mazo, crupier):
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
        print ' '
        print ' ------------- Estado Juego --------------- '
        if self.estado_juego:
            print 'Estado Juego ......: Activo' 
        else:
            print 'Estado Juego ......: Inactivo' 
        if len(self.lista_jugadores) > 0:
            print 'Lista Jugadores ...: (%r)' %len(self.lista_jugadores)
            for jugador in self.lista_jugadores:
                print 'Nombre: %s, estado <%r>, Apuesta actual <%r>' %(jugador.dame_nombre(), jugador.dame_estado_jugador(), jugador.dame_apuesta_actual())
                print '        Monto inicial <%r>, Monto restante <%r>' %(jugador.dame_monto_inicial(), jugador.dame_monto_restante())
        else:
            print 'Lista Jugadores....: Vacia'
        
        if len(self.lista_jugadores) > 0 and self.turno_jugador < len(self.lista_jugadores):
            print 'Turno Jugador .....: %s (%r)' %(self.lista_jugadores[self.turno_jugador].dame_nombre(),self.turno_jugador)
        else:
            print 'Turno Jugador .....: (%r)' %self.turno_jugador
            
        if self.crupier:
            print 'Crupier ...........: %s ' %self.crupier.dame_nombre()
        else:
            print 'Crupier ...........: Juego no tiene Crupier asignado'
        
        print 'Monto Inicial .....: %r ' %self.monto_inicial
        
    def mueve_turno(self):
        if self.turno_jugador == (len(self.lista_jugadores) - 1):
            self.turno_jugador = 0
        else:
            self.turno_jugador += 1
    
    def juego_apuesta_inicial(self, jugador, monto_apuesta_inicial):
        if monto_apuesta_inicial <= jugador.dame_monto_restante() and monto_apuesta_inicial > 0:
            jugador.definir_estado_jugador(1)
            jugador.definir_apuesta_actual(monto_apuesta_inicial)
        else:
            print '%s no tiene suficiente dinero' %jugador.dame_nombre()
    
    def inicia_juego(self):
        pass
            