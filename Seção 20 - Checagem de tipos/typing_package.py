"""
Pacote Typing


"""

# type hinting para ser declarado como uma coleção na variável global
lista1: list = [1, 2, 3, 4, 5]
tupla1: tuple = (1, 2, 3, 4, 5)
valor1: set = {1, 2, 3, 4, 5}
dicio1: dict = {'um': 1, 'dois': 2}

# um ou mais tipos a serem declarados no type hinting dentro da variável global
from typing import List, Tuple, Dict, Set

lista2: List[int] = [1, 2, 3, 4, 5]
tupla2: Tuple[int, int, int, int, int] = (1, 2, 3, 4, 5)
valor2: Set[int] = {1, 2, 3, 4, 5}
dicio2: Dict[str, int] = {'um': 1, 'dois': 2}

import random

naipe = '♠ ♣ ♥ ♦'.split()
carta = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()


def criar_baralho(aleatorio=False):
    """Cria baralho com 52 cartas"""
    baralho = [(n, c) for c in carta for n in naipe]
    if aleatorio:
        random.shuffle(baralho)
    return baralho


def distribuir_cartas(baralho):
    """Gerencia a mão de cartas de acordo com o baralho gerado"""
    return baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4]


def jogar():
    """Inicia um jogo de cartas para 4 jogadores"""
    cartas = criar_baralho(aleatorio=True)
    jogadores = 'P1 P2 P3 P4'.split()
    maos = {j: m for j, m in zip(jogadores, distribuir_cartas(cartas))}

    for jogador, cartas in maos.items():
        cartass = ' '.join(f"{j}{c}" for (j, c) in cartas)
        print(f'{jogador}: {cartass}')


if __name__ == '__main__':
    jogar()


