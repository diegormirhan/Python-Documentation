"""
Dictionary Comprehension

Pense no seguinte:

Se quisermos criar uma lista, fazemos:

lista = [1, 2, 3, 4, 5]

Se quiseros criar uma tupla:

tupla = (1, 2, 3, 4, 5)  # 1, 2, 3, 4, 5

Se quisermos criar um set (conjunto):

conjunto = {1, 2, 3, 4, 5}

Se quisermos criar um dicionário;

dicionário = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Sintaxe

{chave:valor for valor in iterável}

"""

# Exemplos

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

print(quadrado)


chave = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chave[i]: valores[i] for i in range(0, len(chave))}

print(mistura)


# Exemplos com lógica condicional

numeros = [1, 2, 3, 4, 5]

res = {num: ('Par' if num % 2 == 0 else 'Ímpar') for num in numeros}

print(res)

