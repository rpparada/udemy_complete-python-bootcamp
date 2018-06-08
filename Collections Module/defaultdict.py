import os
from collections import defaultdict

d = defaultdict(object)
d['hola']
print(d)

os.system('clear')

d1 = defaultdict(lambda:'chao')
d1['hola']
d1['hola1']
print(d1)
