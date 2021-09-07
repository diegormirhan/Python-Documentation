"""
Decorators com diferentes Assinaturas


# Relembrando


def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá eu sou o {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'

# Testando


# print(saudacao('Diego'))

print(ordenar('Picanha', 'Batata Frita'))

# Para resolver, utilizamos um padrão de projeto chamado Decorator Pattern

# Assinatura de uma função é presentada pelo seu retorno, nome e parâmetros de entrada



# Refatorando com o Decorator Pattern


def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá eu sou o {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'


print(saudacao("Diego"))

print(ordenar('Picanha', 'Batata Frita'))


@gritar
def lol():
    return 'lol'


print(lol())


# OBS: Vale lembrar que podemos utilizar parâmetros nomeados

print(ordenar(acompanhamento='Batata Frita', principal='Picanha'))
"""


# Decorator com argumentos

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor Incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, *kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


# Testando

print(soma_dez(10, 12))

print(soma_dez(1, 12))

print(comida_favorita('pizza', 'churrasco'))

print(comida_favorita('sanduiche', 'pizza'))

