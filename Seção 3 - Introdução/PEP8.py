"""
PEP8 - Python Enchancement Proposal

São propostas de melhorias para a linguagem python

The Zen of python

import this

A ideia da PEP8 é que possamos escrever códigos python de forma Pythônica (de forma mais bonita e organizada).

[1] - utilize Camel Case para nomes de classes

class Calculadora:
    pass


class CalculadoraCientifica:
    pass


[2] - Utilize nomes em minúsculo, separados por underline para funções ou variáveis;

def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_dois = 8

[3] - Utilize 4 espaços para identação! (Não use tab)

if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco
- Separar funções e definiciões de classe com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados com uma única linha em branco;

[5] - Imports ( importação de bibliotecas )

- Imports devem ser sempre feitos em linhas separadas;

# Import errado

import sys, os

# Import certo

import sys
import os

# Caso não tenha muitos imports no mesmo pacote, não há problemas em utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    outroType
)
# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e antes de
# constantes ou variáveis globais

[6] - espaços em expressões e instruções

# Não faça:

funçao( algo [ 1 ], { outro: 2 } )

# Faça:

funçao(algo[1], {outro: 2})

# Não Faça:

algo (1)

# Faça:

algo(1)

# Não Faça:

dict ['chave'] = lista [indice]

# Faça:

dict['chave'] = lista[indice]

# Não Faça:

x              = 2
y              = 3
variavel_longa = 5

# Faça:

x = 2
y = 3
variavel_longa = 5

[7] - Termine sempre uma instrução com uma nova linha
"""
import this
