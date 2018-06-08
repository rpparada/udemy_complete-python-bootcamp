# counter
import os

from collections import Counter
lista = [1,2,3,3,3,4,4,55,5,6,6,2,7,88,]
texto = 'holakdjfnsdfalksdfkhaksjdfasd'
print(Counter(lista))
print(Counter(texto))

texto2 = 'Hola munda hola chile rodrigo chao chao chile rodrigo Rodrigo'
palabras = texto2.split()
print(Counter(palabras))

os.system('clear')
cnt = Counter(palabras)
print(cnt.most_common())
print(sum(cnt.values()))
print(list(cnt))
