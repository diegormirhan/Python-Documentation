"""
Map

Com Map, fazemos mapeamento de valores para função
"""
import math


def area(r):
    """Calcula a area de um circulo com raio 'r'."""
    return math.pi * (r ** 2)


print(area(2))
print(area(4))


raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma Comum
areas = []
for r in raios:
    areas.append(area(r))
print(areas)

# Forma 2 - Map

# Map e uma funçao que recebe dois parametros: O primeiro e a funçao e o segundo e o iteravel. Retorna um Map Object

areas = map(area, raios)

print(areas)
print(type(areas))
print(list(areas))

# Forma 3 - Map com Lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))

# Apos utilizar a funçao map() depois da primiera utilizaçao do resultado, ele zera


# Para fixar - Map

# Temos dados iteráveis:

# Dados: a1, a2, ....,, an

# Temos uma função:

# Função: f(x)

# Utilizamos a função map(f, dados) onde map irá 'mapear' cada elemento dos dados e aplicar a função.

# O Map Object: f(a1), f(a2), f(...), f(an)


# Mais um exemplo

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Nova York', 4), ('Brasília', 32)]

print(cidades)

# f = 9/5 * c + 32

# Lambda

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(list(map(c_para_f, cidades)))
