"""
Trabalhando com Módulos Built-In (módulos integrados, que já vem instalados no Python
________________________
|Python|Módulos BuiltIn|


# Utilizando alias (apelidos) para módulos e funções
import random as rdm

print(rdm.random())


# Podemos importar todas as funções de um módulo utilizando o *
# Você não precisará imprimir random.random(). Apenas random()
from random import *

print(random())


# Importando todo o módulo

import random

print(random.random())



# Utilizando alias (apelidos) para funções

from random import randint as rdi

print(rdi(5, 10))


# Utilizando alias (apelidos) para mais de uma função

from random import randint as rdi, random as rdm

print(rdi(5, 10))
print(rdm())



"""
# http://docs.python.org/3/py-modindex.html
# Costumamos a utilizar tuple para colocar múltiplos imports de um mesmo módulo

from random import (
    random,
    randint,
    shuffle,
    choice,
)

print(random())

print(randint(3, 7))

lista = ['Diego', 'Mirhan', 'Rodrilla']
shuffle(lista)
print(lista)

print(choice('Diego Mirhan'))






