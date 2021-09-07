"""
Tuplas (tuple)

Tuplas são muito parecidas com listas.
Existem basicamente duas diferenças básicas:

1 - As tuplas são representadas por parenteses ()

2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda.
Toda operação em uma tupla gera uma nova tupla.


# Cuidado 1: As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# Cuidado 2: tuplas com um elemento

tupla3 = (4)    # Isso não é uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (4, )  # isso é uma tupla
print(tupla4)
print(type(tupla4))

# Conclusão: Podemos concluir que tuplas são definidas pela vírgula e não pelo parênteses

(4) - Não é tupla
(4,) -É tupla
4, - É tupla

# Podemos gerar uma tupla dinamicamente com range(início,fim,passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla

tupla = ('Diego Mirhan', 'Programação Python')

nome, curso = tupla

print(nome)
print(curso)

# OBS: Gera erro (ValueError) se colocarmos um número diferente de elemntos para desempacotar.

# Métodos de adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutáveis.


# Soma*, Valor máximo*, Valor mínimo* e Tamanho
# * Se os valores forem inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6)

print(f'soma = {sum(tupla)}')
print(f'valor máximo = {max(tupla)}')
print(f'valor mínimo = {min(tupla)}')
print(f'tamanho = {len(tupla)}')

# Concatenação de tuplas

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)  # Tuplas são imutáveis

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2
print(tupla3)

print(tupla1)
print(tupla2)

tupla1 = tupla1 + tupla2    # Tuplas são imutáveis, mas podemos sobrescrever seus valores
print(tupla1)

# Verificar se determinado elemnto está contido na tupla

tupla = (1, 2, 3)
print(3 in tupla)

# Iterando sobre uma tupla

tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'a', 'b', 'b')

print(tupla.count('a'))
print(tupla.count('b'))

escola = tuple('Diego Mirhan')
print(escola)
print(escola.count('i'))

# Dicas na utilização de tuplas

# Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção

# Exemplo 1

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

print(meses)

# Slicing

# tupla(inicio:fim:passo)

print(meses[0:7])
print(meses[4:8])
print(meses[::-1])

# O acesso a elementos de uma tupla também é semelhante a de uma lista

print(meses[5])

# Iterar com while
i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1

# Verificamos em qual índice um elemento está na tupla

print(meses.index('Junho'))

# OBS: Caso o elemento não exista, será gerado ValueError.


# Por quê utilizar tuplas?

# - Tuplas são mais rápidas do que listas.
# - Tuplas deixam seu código mais seguro*

# * Isso porque trabalhar com os elementos imutáveis traz mais segurança para o código.

# Copiando uma tupla para a outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla

print(nova)
print(tupla)

outra = (4, 5, 6)

nova = nova + outra
print(nova)
print(tupla)

"""

