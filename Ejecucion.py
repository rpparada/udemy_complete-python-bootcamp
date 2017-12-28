# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 15:02:11 2017

@author: Rodrigo Parada
"""

# Importando clases propias
from Crupier import Crupier
from MazoCartas import MazoCartas
from Jugador import Jugador
from Tablero import Tablero

# Importando para limpiar consola
import os

# Limpiam consola
clear = lambda: os.system('cls')
clear()

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

# Crea jugador Chino con 200 puntos de juego y lo agregar al actual juego sin iniciar
chino = Jugador("Chino", 50)
tablero.agrega_jugador(chino)

# Crea crupier llamado Pedro
crupier = Crupier("Pedro")
# Crea mazo de juegoa
mazo = MazoCartas()

# Inicia juego en objeto tabla asignado el mazo y crupier 
tablero.abre_juego(mazo, crupier)

# Muestra estado actual del juego en tablero
tablero.muestra_estado()

for jugador in tablero.dame_listado_jugadores():
    tablero.juego_apuesta_inicial(jugador, 60)

# Muestra estado actual del juego en tablero
tablero.muestra_estado()

# Quitar jugador Chino
#tablero.quitar_jugador('Rodrigo')

# Muestra estado actual del juego en tavlero
#tablero.muestra_estado()

# Resetea juego
#tablero.reset_juego()

# Muestra estado actual del juego en tavlero
#tablero.muestra_estado()


    