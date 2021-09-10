"""
Estruturas Lógicas:
and (e), or (ou), not (não), is (está)

Operadores unários:
    - not
Operadores binários:
    - and, or, is

Regras de funcionamento:

Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleano é invertido, ou seja, se for True vira False, se for false vira True
Pra o 'is', o valor é comparado com um segundo.
"""
"""
ativo = True
logado = True

if ativo and logado:
    print('Bem-Vindo usuário!')
else:
    print('Você precisa ativar a sua conta. Por favor verifique seu email!')
"""

"""
ativo = True
logado = False

if ativo or logado:
    print('Bem-Vindo usuário!')
else:
    print('Você precisa ativar a sua conta. Por favor verifique seu email!')
"""

"""
ativo = True
logado = True

if not ativo:
    print('Você precisa ativar a sua conta. Por favor verifique seu email!')

else:
    print('Bem-Vindo usuário!')
"""

ativo = False
logado = False

if ativo is False:
    print('Você precisa ativar a sua conta. Por favor verifique seu email!')

else:
    print('Bem-Vindo usuário!')
