"""
Funções de Maior grandeza - Higher Other Functions - HOF

O que isso se significa?

- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções
que retornam outras funções como resultado ou mesmo que podemos passar funções
como argumentos para outras funções, e até mesmo criar variáveis do tipo de funções
nos nossos programas.

OBS: Na seção de funções, nós utilizamos isso.

Em Python, as funções são Cidadãos de Primeira Classe, First Class Citizen


# Exemplo - Definindo as funções


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, function):
    return function(num1, num2)


# Testndo as funções

print(calcular(10, 5, somar))

print(calcular(10, 5, subtrair))

print(calcular(10, 5, multiplicar))

print(calcular(10, 5, dividir))



# Nested Functions - Funções Aninhadas

# Em Python podemos também ter funções dentro de funções, que são conhecidas por Nested Functions
# ou também Inner Functions (Funções Internas).

# Exemplo

from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('Oi ', 'Suma daqui ', 'Gosto muita de você '))
    return humor() + pessoa


# Testando

print(cumprimento('Anna'))

print(cumprimento('Diego'))



# Retornando funções de outras funções

from random import choice


def faz_me_rir():
    def rir():
        return choice(('hahahahaha', 'kkkkkkkkkkkkkk', 'jajajajajajaja'))
    return rir


# Testando

rindo = faz_me_rir()
print(rindo())
"""

# Inner Functions (Funções internas /Nested Functions) podem acessar o escopo de funções mais externas.

from random import choice


def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahahaah', 'kakakakakakakka', 'jajajajajajaja'))
        return f'{risada} {pessoa}'
    return dando_risada


# Testando

rindo = faz_me_rir_novamente('Fernanda')

print(rindo())
print(rindo())
print(rindo())
