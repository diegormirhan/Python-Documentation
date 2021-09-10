"""
Sorted

OBS: Não confunda, apesar do nome, com a função sort() que já estudamos em listas. O sort()
só funciona em listas.

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() serve para ordenar

OBS: O sorted, SEMPRE retorna uma lista com elementos do iterável ordenados.



# Exemplo

numeros = (5, 2, 1, 3, 4)
print(numeros)

print(sorted(numeros))  # Ordenar do menor para o maior

print(numeros)



numeros = (5, 2, 1, 3, 4)
print(numeros)

print(sorted(numeros))

# Adicionando parâmetros ao sorted()

print(sorted(numeros, reverse=True))  # Ordena do maior para o menor



# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {"username": "samuel", "tweets": ["Gosto de dançar", "Gosto de livros"]},
    {'username': "carlos", 'tweets': ['Gosto de gatos']},
    {'username': "marina", 'tweets': []},
    {'username': "pedro", 'tweets': ['Gosto de dormir', 'Amo livros']},
    {'username': "diego", 'tweets': []},
    {'username': "ana", 'tweets': []}
]

print(usuarios)

# Ordenando por username - Ordem Alfabética
print(sorted(usuarios, key=lambda usuario: usuario['username']))


# Ordenando pelo número de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))
"""

# Último exemplo

musicas = [
    {'título': 'No time to die', 'tocou': 10},
    {'título': 'Driving License', 'tocou': 43},
    {'título': 'Got you get into my life', 'tocou': 2},
    {'título': 'Burry a Friend', 'tocou': 9},
]
print(musicas)

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
