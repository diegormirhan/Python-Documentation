"""
Min e Max

max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos.


# Exemplos

lista = [3, 65, 99, 12, 9, 128]
print(max(lista))

tupla = (3, 65, 99, 12, 9, 128)
print(max(tupla))

conjunto = {3, 65, 99, 12, 9, 128}
print(max(conjunto))

dicionario = {'a': 3, 'b': 65, 'c': 99, 'd': 12, 'e': 9, 'f': 128}
print(max(dicionario))

dicionario = {'a': 3, 'b': 65, 'c': 99, 'd': 12, 'e': 9, 'f': 128}
print(max(dicionario.values()))


# Faça um programa que receba dois valores do usuário e mostre o maior
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(max(val1, val2))


print(max(94, 232, 43, 1, 54))

print(max('a', 'ab', 'abc'))

print(max('a', 'b', 'c', 'g'))

print(max(8.3232, 2.3))

print(max('Diego Mirhan'))




# Exemplos

lista = [3, 65, 99, 12, 9, 128]
print(min(lista))

tupla = (3, 65, 99, 12, 9, 128)
print(min(tupla))

conjunto = {3, 65, 99, 12, 9, 128}
print(min(conjunto))

dicionario = {'a': 3, 'b': 65, 'c': 99, 'd': 12, 'e': 9, 'f': 128}
print(min(dicionario))

dicionario = {'a': 3, 'b': 65, 'c': 99, 'd': 12, 'e': 9, 'f': 128}
print(min(dicionario.values()))


# Faça um programa que receba dois valores do usuário e mostre o maior
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(min(val1, val2))


print(min(94, 232, 43, 1, 54))

print(min('a', 'ab', 'abc'))

print(min('a', 'b', 'c', 'g'))

print(min(8.3232, 2.3))

print(min('Diego Mirhan'))



# Outros exemplos

nomes = ['Arya', 'Marina', 'Dudu', 'Ana', 'Pablo', 'Pedro']

print(max(nomes))

print(min(nomes))

print(max(nomes, key=lambda nome: len(nome)))

print(min(nomes, key=lambda nome: len(nome)))

"""

musicas = [
    {'título': 'No time to die', 'tocou': 10},
    {'título': 'Driving License', 'tocou': 43},
    {'título': 'Got you get into my life', 'tocou': 2},
    {'título': 'Burry a Friend', 'tocou': 9},
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# DESAFIO! Imprima somente o título da música mais ou menos tocada
print(max(musicas, key=lambda musica: musica['título'])['título'])
print(min(musicas, key=lambda musica: musica['título'])['título'])

# DESAFIO! Como encontrar a música mais tocada e a menos tocada sem usar max(), min() e lambda

max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['título'])


min = 99999
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['título'])
