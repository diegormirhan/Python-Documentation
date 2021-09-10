"""
Reversed

OBS: Não confunda com a função reverse() que estudamos em listas

A função reverse() só funciona em listas.

Já a função reversed() funciona com qualquer iterável.

Sua função é inverter o iterável.

A função reversed() retorna um iterável chamado List Reverse Iterator
"""

# Exemplos

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))

# Podemos converter o elemento retornado para uma Lista, Tupla ou Conjunto

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# OBS: Em conjuntos, não definimos a ordem dos elementos
# Conjunto(Set)
print(set(reversed(lista)))


# Podemos iterar sobre o reversed()
for letra in reversed('Diego Mirhan'):
    print(letra, end='',)
print('')

# Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('Diego Mirhan'))))

# Já vimos como fazer isso mais fácil com slice de strings
print('Diego Mirhan'[::-1])

# Podemos também utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n)
print('')

# Apesar de que também já vimos como fazer isso utilizando o próprio range()
for n in range(9, -1, -1):
    print(n)
