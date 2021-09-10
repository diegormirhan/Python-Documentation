"""
Tipo FLoat

conhecido também como tipo real, decimal.

apresenta casas decimais.

obs: o sepradador de casas decimais é o ponto e não a vírgula.
"""

# Errado do ponto de vista do float, mas gera uma tupla
valor = 1, 44
print(valor)
print(type(valor))

# Certo no ponto de vista do float
valor = 1.44
print(valor)
print(type(valor))

# É possível fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um float para int
"""
OBS: Ao converter valores float para inteiros, nós perdemos a precisão
"""
resultado = int(valor)
print(resultado)
print(type(resultado))

# Podemos trabalhar com números complexos
variavel = 5j
