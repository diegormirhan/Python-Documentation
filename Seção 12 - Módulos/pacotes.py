"""
Pacotes

Módulo -> É apenas um arquivo Python que pode ter diversas funções que utilizamos;

Pacote -> É um diretório contendo uma coleção de módulos;

OBS: Nas versões do Python 2.x, um pacote Python deveria conter dentro dele um
arquivo chamado __init__.py

Nas versões do Python 3.x, não é mais obrigatória a utlização deste arquivo, mas
normalmente ainda é utilizado para manter a compatibilidade




from geek import geek1, geek2

from geek.university import geek3, geek4


print(geek1.pi)
print(geek1.funcao1(3, 5))

print(geek2.nome)
print(geek2.funcao2())


print(geek3.funcao3())

print(geek4.funcao4())
"""

from geek.geek1 import funcao1

from geek.university.geek4 import funcao4

print(funcao1(3, 5))
print(funcao4())



