"""
Set Comprehension

Lista = [1, 2, 3, 4, 5]
Set = {1, 2, 3, 4, 5}
"""

# Exemplos

numeros = {num for num in range(1, 11)}
print(numeros)

# Outro Exemplo

numeros = {x ** 2 for x in range(10)}
print(numeros)


# DESAFIO: faça uma alteração na estrutura acima para gerar um dicionário ao invés de set

numeros = {x: x ** 2 for x in range(10)}
print(numeros)

# Para Finalizar

numeros = {letra for letra in 'Diego Mirhan'}
print(numeros)




