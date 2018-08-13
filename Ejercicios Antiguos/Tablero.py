#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 23:23:16 2017

@author: Rodrigo Parada
"""
# Reglas extraidas desde http://www.casino.es/blackjack/como-jugar-blackjack/

# Importando clases propias
#from Crupier import Crupier
#from MazoCartas import MazoCartas
#from Jugador import Jugador

class Tablero(object):
    
    numero_max_jugadores = 7    
    
    def __init__(self):
        # Estado juego: 0 = incativo, 1 = activo (en apuestas iniciales), 2 = juego iniciado, 3 = terminado
        self.estado_juego = 0
        self.lista_jugadores = []
        self.turno_jugador = 0
        self.crupier = None
        self.mazo = None
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
        self.estado_juego = 0
        self.lista_jugadores = []
        self.turno_jugador = 0
        self.crupier = None
        self.mazo = None
        self.monto_inicial = 0
        self.monto_actual = 0
        
    def dame_posicion_jugador(self, nombre):
        for indice,jugador in enumerate(self.lista_jugadores):
            if jugador.dame_nombre() == nombre:
                return indice
        
    def abre_juego(self, mazo, crupier):
        if len(self.lista_jugadores) == 0:
            print 'Juego no puede comenzar, no hay jugadores'
        elif self.estado_juego != 0:
            print 'Actualmente ya hay un juego en progreso - Estado actual (%r)' %self.estado_juego
        else:
            self.estado_juego = 0
            self.mazo = mazo
            self.crupier = crupier
            self.turno_jugador = 0
            self.monto_inicial = 1000
            
    def muestra_estado(self):
        print ' '
        print ' ------------- Estado Juego --------------- '
        # Estado juego: 0 = incativo, 1 = activo (en apuestas iniciales), 2 = iniciado, 3 = terminado
        if self.estado_juego == 0:
            print 'Estado Juego ......: Incativo (%r)' %self.estado_juego
        elif self.estado_juego == 1:
            print 'Estado Juego ......: Activo (%r)' %self.estado_juego
        elif self.estado_juego == 2:
            print 'Estado Juego ......: Iniciado (%r)' %self.estado_juego
        elif self.estado_juego == 3:
            print 'Estado Juego ......: Terminado (%r)' %self.estado_juego
        else:
            print 'Estado Juego ......: Desconocido (%r)' %self.estado_juego
            
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
        
        if self.mazo != None:
            if self.mazo.numero_cartas_disponibles() > 0:
                print 'Numero mazo .......: %r ' %self.mazo.numero_cartas_disponibles()
            else:
                print 'Numero mazo .......: 0 ' 
        else:
            print 'Numero mazo .......: No hay mazo asignado'
        print 'Monto Inicial .....: %r ' %self.monto_inicial
    
    def __str__(self):
        return 'Estado juego %s' %self.estado_juego
        
        
    def mueve_turno(self):
        if self.turno_jugador == (len(self.lista_jugadores) - 1):
            self.turno_jugador = 0
        else:
            self.turno_jugador += 1
    
    def juego_apuesta_inicial(self, jugador, monto_apuesta_inicial):
        if self.estado_juego != 0:
            print 'Juego no esta abierto a apuestas iniciales'
            return
        
        if monto_apuesta_inicial <= jugador.dame_monto_restante() and monto_apuesta_inicial > 0:
            jugador.definir_estado_jugador(1)
            jugador.definir_apuesta_actual(monto_apuesta_inicial)
        else:
            print '%s no tiene suficiente dinero para apuesta inicial' %jugador.dame_nombre()
    
    def inicia_juego(self):
        # Checkea que haya jugadores en juego estado = 1
        
        # Este codigo hacelo mismo que el comentado abajo, solo estamos utilizando Comprehensions
        lista_aux  = [jugador for jugador in self.lista_jugadores if jugador.dame_estado_jugador() == 1]
        if len(lista_aux) == 0:
            print 'No hay ningun jugador con apuesta inicial realizada'
            return
        '''
        for jugador in self.lista_jugadores:
            if jugador.dame_estado_jugador() == 1:
                break
        
        else:
            print 'No hay ningun jugador con apuesta inicial realizada'
            return
        '''
        
        # Chekea estado del juego
        if self.estado_juego != 0:
            print 'Juego no esta activo'
            return

        # Falta chekear creditos disponibles para jugador, por ahora asumiremos que tiene inlimitado numero de creditos
        self.estado_juego = 1
        print 'No va mas, juego iniciado.'
    
    def repartir_carta(self, jugador):
        # Chekea turno
        if self.turno_jugador != self.dame_posicion_jugador(jugador.dame_nombre()):
            print '%s aun no es tu turno' %jugador.dame_nombre()
            return
        
        if jugador.dame_estado_jugador() != 1:
            # Estado 0 = inactivo, 1 = en juego (apuesta inicial hecha), 2 = gano, 3 = empato, 4 = perdio
            if jugador.dame_estado_jugador() == 0:
                print 'No puedes pedir carta %s, no hiciste apuesta inicial' %jugador.dame_nombre()
                return
            elif jugador.dame_estado_jugador() == 2:
                print 'No puedes pedir carta %s, ya haz ganado' %jugador.dame_nombre()
                return
            elif jugador.dame_estado_jugador() == 3:
                print 'No puedes pedir carta %s, ya haz empatado' %jugador.dame_nombre()
                return
            elif jugador.dame_estado_jugador() == 4:
                print 'No puedes pedir carta %s, ya haz perdido' %jugador.dame_nombre()
                return
            else:
                print 'No puedes pedir carta %s tu estado es desconocido (%r) ' %(jugador.dame_nombre(), jugador.dame_estado_jugador())
                return
        
        jugador.perdir_carta(self.mazo.dame_cartas(1))
        
        if jugador.dame_suma_cartas() > 21:
            jugador.definir_estado_jugador(4)
            