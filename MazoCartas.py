#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 23:14:37 2017

@author: rodrigoparada
"""

import random

class MazoCartas(object):
    
    # Tipo de Cartas (Trebol = T, Pica = P, Corazon = C, Diamante = D), Valor y Estado (A = disponible, U = no disponible)
    mazo_inicial = {'TA':[1,"A"],'T2':[2,"A"],'T3':[3,"A"],'T4':[4,"A"],'T5':[5,"A"],'T6':[6,"A"],'T7':[7,"A"],'T8':[8,"A"],'T9':[9,"A"],'T10':[10,"A"],'TJ':[10,"A"],'TQ':[10,"A"],'TK':[10,"A"],
                    'PA':[1,"A"],'P2':[2,"A"],'P3':[3,"A"],'P4':[4,"A"],'P5':[5,"A"],'P6':[6,"A"],'P7':[7,"A"],'P8':[8,"A"],'P9':[9,"A"],'P10':[10,"A"],'PJ':[10,"A"],'PQ':[10,"A"],'PK':[10,"A"],
                    'CA':[1,"A"],'C2':[2,"A"],'C3':[3,"A"],'C4':[4,"A"],'C5':[5,"A"],'C6':[6,"A"],'C7':[7,"A"],'C8':[8,"A"],'C9':[9,"A"],'C10':[10,"A"],'CJ':[10,"A"],'CQ':[10,"A"],'CK':[10,"A"],
                    'DA':[1,"A"],'D2':[2,"A"],'D3':[3,"A"],'D4':[4,"A"],'D5':[5,"A"],'D6':[6,"A"],'D7':[7,"A"],'D8':[8,"A"],'D9':[9,"A"],'D10':[10,"A"],'DJ':[10,"A"],'DQ':[10,"A"],'DK':[10,"A"]}
    
    numero_cartas = 13 * 4
    
    def __init__(self, numero_mazos = 1):
        self.mazos_cartas = [self.mazo_inicial] * numero_mazos
        self.numero_total_cartas = self.numero_cartas * numero_mazos
        self.numero_mazos = numero_mazos
            
    def dame_cartas(self, numero = 1):
        num = 0
        lista_cartas = []
        mazo_random = 0
        if self.numero_mazos > 1:
            mazo_random = random.randint(0,len(self.mazos_cartas)-1)
        while num < numero:
            carta = list(random.choice(self.mazos_cartas[mazo_random].items()))
            self.mazos_cartas[mazo_random].pop(carta[0])
            lista_cartas.append(carta)
            num += 1
            if self.numero_mazos > 1:
                mazo_random = random.randint(0,len(self.mazos_cartas)-1)
            
        return lista_cartas
    
    def numero_cartas_disponibles(self):
        contador = 0
        for mazo in self.mazos_cartas:
            print "largo mazo %r" %len(mazo)
            contador = contador + len(mazo)
        return contador

    def numero_cartas_nodisponibles(self):
        return (self.numero_cartas * self.numero_mazos) - self.numero_cartas_disponibles()
    
maz = MazoCartas(1)
print maz.numero_cartas_disponibles()
print maz.numero_cartas_nodisponibles()
print '------'
print maz.dame_cartas(2)
print maz.numero_cartas_disponibles()
print maz.numero_cartas_nodisponibles()
print '------'
print maz.dame_cartas(2)
print maz.numero_cartas_disponibles()
print maz.numero_cartas_nodisponibles()

