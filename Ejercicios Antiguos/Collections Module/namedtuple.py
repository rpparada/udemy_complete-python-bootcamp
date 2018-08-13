import os
from collections import namedtuple

os.system('clear')

perro = namedtuple('Perro','edad raza nombre')

juanito = perro(edad=1,raza='prueba',nombre='juanito')

print(juanito.nombre)
