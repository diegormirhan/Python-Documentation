"""
POO - Polimorfismo

Poli -> Muitas
morfis -> Formas

Quando nós reimplementamos um método presente na classe pai em classes filhas
estamos realizando uma sobrescrita de método (Sobrescrita).

O overriding é a melhor representação do polimorfismo.
"""


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa ser implementada')

    def comer(self):
        return f'{self.__nome} está comendo'


class Cachorro(Animal):

    def __init__(self, nome):
        super(Cachorro, self).__init__(nome)

    def falar(self):
        return f'{self._Animal__nome} fala wau wau'


class Gato(Animal):

    def __init__(self, nome):
        super(Gato, self).__init__(nome)

    def falar(self):
        return f'{self._Animal__nome} fala miau'


class Rato(Animal):

    def __init__(self, nome):
        super(Rato, self).__init__(nome)

    def falar(self):
        return f'{self._Animal__nome} fala algo...'


# Testes

felix = Gato('Felix')
print(felix.comer())
print(felix.falar())

pluto = Cachorro('Pluto')
print(pluto.comer())
print(pluto.falar())

mickey = Rato('Mickey')
print(mickey.falar())
print(mickey.comer())
