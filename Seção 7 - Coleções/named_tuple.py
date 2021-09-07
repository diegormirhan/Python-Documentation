"""
Módulo Collections - Named Tuple

# Recap tupla
tupla = {1, 2, 3}
print(tupla[1])

Named Tuple -> São tuplas, diferenciadas, onde especificamos um nome para a mesma e também parâmetros.

# Importando

from collections import namedtuple

# Precisamos definir o nome e parâmetros.

# Forma 1 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raça nome')

# Forma 2 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raça, nome')

# Forma 3 - Declaração Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raça', 'nome'])

# Usando

ray = cachorro(idade=2, raça='Vira-Lata', nome='Ray')
print(ray)

# Acessando os dados

# Forma 1

print(ray[0])   # idade
print(ray[1])   # raça
print(ray[2])   # nome

# Forma 2

print(ray.idade)   # idade
print(ray.raça)    # raça
print(ray.nome)    # nome

print(ray.index('Vira-Lata'))
print(ray.count('Vira-Lata'))
"""