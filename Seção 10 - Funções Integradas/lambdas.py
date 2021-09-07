"""
Utilizando Lambdas

# Função em Python


def funcao(x):
    return 3 * x + 1


print(funcao(4))
print(funcao(7))

# Expressão Lambda
lambda x: 3 * x + 1

# E como podemos utilizar a expressão lambda:
calcular = lambda x: 3 * x + 1

print(calcular(4))
print(calcular(7))
"""

"""
# Podemos ter expressões lambdas com múltiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('DIEGO', 'mirhan'))
print(nome_completo('diego            ', '          mIRHAN'))





# Em funções Python podemos ter nenhuma ou várias entradas. Em Lambdas há também:

amar = lambda: 'Como não amar Python?'

uma = lambda x: x * 3 + 1

duas = lambda x, y: (x + y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

# n = lambda x1, x2, ...., xn: <expressão>

print(amar())
print(uma(4))
print(duas(3, 5))
print(tres(6, 7, 8))

# OBS: se passasemos mais argumentos do que parâmetros esperados teremos TypeError




# Outro Exemplo

autores = ['Isaac Assimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clark', 'Frank Herbert', 'Orson Scott Card']

print(autores)


autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)


"""

# Função Quadrática
# f(x) = a * x ** 2 + b * x + c

# Definindo a função


def geradora_funcao_quadratica(a, b, c):
    """Retorna f(x) = ax² + bx + c"""
    return lambda x: a * x ** 2 + b * x + c


teste = geradora_funcao_quadratica(2, 3, 4)

print(teste(0))
print(teste(1))
print(teste(2))

# Outra forma mais simples:

print(geradora_funcao_quadratica(2, 3, 4)(2))



