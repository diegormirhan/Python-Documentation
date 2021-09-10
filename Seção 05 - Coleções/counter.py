"""
Módulo Collections - Counter (Contador)

Collections -> High-performance Container Datetypes

Counter -> Receba um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade
de ocorrrências desse elemento.

# Realizando o Import

from collections import Counter

# Exemplo 1

# Podemos utilizar qualquer iterável, aqui usamos uma lista
lista = [1, 1, 1, 1, 1, 1, 2, 2, 1, 3, 2, 2, 3, 4, 2, 3, 3, 3, 5, 5, 4, 5, 5, 5, 5, 6, 1, 4, 6]

# Utilizando o Counter
res = Counter(lista)
print(res)
print(type(res))

# Counter({1: 8, 5: 6, 2: 5, 3: 5, 4: 3, 6: 2})

# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências.

# Exemplo 2

print(Counter('Diego Mirhan'))
# Counter({'i': 2, 'D': 1, 'e': 1, 'g': 1, 'o': 1, ' ': 1, 'M': 1, 'r': 1, 'h': 1, 'a': 1, 'n': 1})

"""

from collections import Counter

# Exemplo 3

texto = """Guerri não fez segredo de que ele olha para a Astralis como um caso de sucesso. Em junho, ele elogiou os 
esforços da organização dinamarquesa para quebrar o que ele considera ser uma barreira cultural na cena de 
Counter-Strike, e admitiu que a ideia de trabalhar com uma lista expandida era atraente para ele."""

palavras = texto.split()

# print(palavras)

res = Counter(palavras)

print(res)

# Encontrando as 5 palavras com mais ocorrência no texto
print(res.most_common(5))

# [('de', 4), ('que', 3), ('ele', 3), ('para', 3), ('a', 2)]
