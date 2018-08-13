import os
from collections import OrderedDict

os.system('clear')

d = OrderedDict()
d['a'] = 1
d['f'] = 6
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

for item,index in d.items():
    print item,index
