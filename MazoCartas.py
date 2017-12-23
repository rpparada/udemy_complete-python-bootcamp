#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 23:14:37 2017

@author: rodrigoparada
"""

import random

class MazoCartas(object):
    
    # Tipo de Cartas (Trebol = T, Pica = P, Corazon = C, Diamante = D), Valor y Estado (A = disponible, U = no disponible)
    mazo_inicial = {'TA':1,'T2':2,'T3':3,'T4':4,'T5':5,'T6':6,'T7':7,'T8':8,'T9':9,'T10':10,'TJ':10,'TQ':10,'TK':10,
                    'PA':1,'P2':2,'P3':3,'P4':4,'P5':5,'P6':6,'P7':7,'P8':8,'P9':9,'P10':10,'PJ':10,'PQ':10,'PK':10,
                    'CA':1,'C2':2,'C3':3,'C4':4,'C5':5,'C6':6,'C7':7,'C8':8,'C9':9,'C10':10,'CJ':10,'CQ':10,'CK':10,
                    'DA':1,'D2':2,'D3':3,'D4':4,'D5':5,'D6':6,'D7':7,'D8':8,'D9':9,'D10':10,'DJ':10,'DQ':10,'DK':10}
    
    numero_cartas = 13 * 4
    
    def __init__(self):
        self.mazos_cartas = self.mazo_inicial.copy()
        self.cartas_disponibles = self.numero_cartas
            
    def dame_cartas(self, numero = 1):
        num = 0
        lista_cartas = []
        while num < numero:
            carta = list(random.choice(self.mazos_cartas.items()))
            self.mazos_cartas.pop(carta[0])
            lista_cartas.append(carta)
            self.cartas_disponibles -= 1
            num += 1
            
        return lista_cartas
    
    def numero_cartas_disponibles(self):
        return self.cartas_disponibles

    def numero_cartas_nodisponibles(self):
        return self.numero_cartas - self.cartas_disponibles
    
    def restaurar_mazo(self):
        self.mazos_cartas = self.mazo_inicial.copy()
        self.cartas_disponibles  = len(self.mazo_inicial)
