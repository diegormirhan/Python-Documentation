"""
Tipo Booleano

Álgebra Booleana, criada por George Boole

2 constantes, Verdadeiro ou Falso

No python - True ou False

OBS: sempre com a inicial maiúscula

Errado: true, false
Certo: True, False
"""

ativo = True

print(ativo)

"""
Operações básicas:
"""

# Negação (not):
"""
fazendo a negação, se o valor booleano for verdadeiro o resultado será falso, 
se for falso o resultado será verdadeiro, ou seja, sempre o contrário.
"""

print(not ativo)

logado = True

# Ou (or):
"""
É uma operação binária, ou seja, depende de dois valores

True or True -> True
True or False -> True 
False or True -> True 
False or False -> False    

"""

print(ativo or logado)

# E (and):
"""
Também é uma operação binária, ou seja, depende de dois valores. Ambos os valores
devem ser verdadeiros para dar resultado verdadeiro.

True and True -> True
True and False -> False 
False and True -> False 
False and False -> False
"""
