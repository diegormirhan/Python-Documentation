"""
Preservando metadata com wraps

Matadados -> São dados intrísecos em arquivos.

wraps -> São funções que envolvem elementos com diversas finalizadas.


# Problema


def ver_log(funcao):
    def logar(*args, **kwargs):
        ""Eu sou uma função (logar) dentro da outra""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui está a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    ""Soma de números""
    return a + b


print(soma(10, 30))


print(soma.__name__)
print(soma.__doc__)

"""

# Resolução de Problema

from functools import wraps


def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro da outra"""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui está a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma de números"""
    return a + b


print(soma(10, 30))


print(soma.__name__)
print(soma.__doc__)
