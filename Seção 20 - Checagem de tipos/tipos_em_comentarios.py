"""
Tipos em comentários

É uma forma de type hinting que usamos em comentários para definir os tipos das variáveis.
"""
import math


# type hinting com uma variável na função
def circunferencia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio


print(circunferencia(8))


# type hinting com duas ou mais variáveis na função
def cabecalho(texto, alinhamento=True):
    # type: (str, bool) -> str
    return f'"{texto}": alinhamento = {alinhamento}'


print(cabecalho('diego mirhan', False))


# type hinting onde é passado as variáveis da função
def cabecalho2(
        texto1,  # type: str
        numero1  # type: int
):
    return f'{texto1} : {numero1}'


print(cabecalho2('diego mirhan', 17))
