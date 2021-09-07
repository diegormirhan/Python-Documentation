"""
Zip

zip() -> Cria um iterável (Zip Object) que agrega elemento de cada um dos iteráveis passados como entrada em pares.


# Exemplos

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)

print(zip1)
print(type(zip1))

# Sempre podemos gerar uma lista, Tupla ou Dicionário
print(list(zip1))


zip1 = zip(lista1, lista2)
print(tuple(zip1))

zip1 = zip(lista1, lista2)
print(set(zip1))

zip1 = zip(lista1, lista2)
print(dict(zip1))

# OBS: O zip() utiliza como parâmetro o menor tamanho em iterável. Isso significa que se estiver
# trabalhando com iteráveis de tamanhos diferentes, irá parar quando os elementos do menor
# iterável acabar.

lista3 = [7, 8, 9, 10, 11]
zip1 = zip(lista1, lista2, lista3)
print(list(zip1))



# Podemos utilizar diferentes iteráveis com zip

tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(tupla, lista, dicionario.values())
print(list(zt))

# Lista de Tuplas

dados = [(0, 1), (2, 3), (4, 5), (6, 7)]

print(list(zip(*dados)))
"""

# Exemplos mais complexos

prova1 = [90, 89, 51]
prova2 = [54, 83, 99]
alunos = ['julia', 'carla', 'pedro']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}

print(final)

# Podemos utilizar o map()

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

print(list(final))



