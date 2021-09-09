"""
Annotations

Tipos de parâmetros de função, também conhecido como dicas de tipo.
Este PEP adiciona sintaxe ao Python para anotar os tipos de variáveis,
incluindo variáveis de classe e variáveis de instância
"""
import math


def circunferencia(raio: float) -> float:
    return 2 * math.pi * raio


print(circunferencia.__annotations__)  # Mostra as annotations da função circunferencia

nome1: str = 'Diego Mirhan'
peso1: int = 23
ativo1: bool = True

print(__annotations__)  # Mostra as annotions das variáveis globais


class Pessoa:

    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso

    def andar(self) -> str:
        return f'{self.__nome} está andando.'


p = Pessoa('diego', 17, 52.4)
print(p.__dict__)
# print(p.__annotations__) Não há annotations

print(p.andar.__annotations__)
print(p.__init__.__annotations__)



