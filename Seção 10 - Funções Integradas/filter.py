"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção

# Biblioteca para trabalhar com dados estátisticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 9.5, 1.4, 5.5, 6.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)

print(f'Média: {media}')

# OBS: Assim como a função map(), o filter() recebe dois parâmetros, sendo
# uma função e um iterável.

res = filter(lambda valor: valor > media, dados)
print(list(res))

# OBS: Assim como na função map(), após serem utilizados os dados de filter(), eles serão excluídos da memória.




paises = ['Brasil', '', 'França', 'Inglaterra', '', 'Estados Unidos', 'Áustralia', '']

# res = filter(lambda pais: len(pais) > 0, paises)
# res = filter(lambda pais: pais != '', paises)
res = filter(None, paises)


print(list(res))




# Diferença entre map() e filter()

# map() -> Recebe dois parâmetros, uma função e um iterável e retorna um
# objeto mapeando a função para cada elemento do iterável


# filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um
# objeto filtrando apenas os elementos de acordo com a função




# Exemplo mais complexo

usuarios = [
    {"usarname": "samuel", "tweets": ["Gosto de dançar", "Gosto de livros"]},
    {'usarname': "carlos", 'tweets': ['Gosto de gatos']},
    {'usarname': "marina", 'tweets': []},
    {'usarname': "pedro", 'tweets': ['Gosto de dormir', 'Amo livros']},
    {'usarname': "diego", 'tweets': []},
    {'usarname': "ana", 'tweets': []}
]

print(usuarios)

# Filtrar os usuários que estão inativos no twitter

# Forma 1
# inativos = filter(lambda usuario: len(usuario['tweets']) == 0, usuarios)

# Forma 2
# inativos = filter(lambda usuario: not usuario['tweets'], usuarios)
print(list(inativos))


"""
# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Lara', 'Marina']

# Devemos criaar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres

lista = map(lambda n: f'Sua instrutora é {n} ', filter(lambda nome: len(nome) < 6, nomes))

print(tuple(lista))
