"""
POO - Método super()

O método super() se refere à super classe
"""


class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        return f'{self.__nome} fala {som}'


class Gato(Animal):

    def __init__(self, nome, especie, raca):
        # Animal.__init__(self, nome, especie)
        super(Gato, self).__init__(nome, especie)
        self.__raca = raca


animal1 = Gato('Felix', 'Felino', 'Angorá')

print(animal1.faz_som('miau'))

print(animal1.__dict__)

