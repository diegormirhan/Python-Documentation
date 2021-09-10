"""
POO - Herança Múltipla

Herança Múltipla nada mais é que a possibilidade de uma classe herdar de múltiplas classes,
fazendo com que a classe filha herde todos os atributos e métodos de todas as classes herdadas.

OBS: A herança múltipla pode ser feita de duas maneiras:
    - Por Multiderivação Direta;
    - Por Multiderivação Indireta;

# Exemplo 1 - Multiderivação Direta


class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class Multiderivada(Base1, Base2, Base3):
    pass

# Exemplo 2 - Multiderivada Indireta


class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class Multiderivada(Base3):
    pass


OBS: Não importa se a derivação é direta ou indireta. A classe que realizar a herança herdará
todos os atributos e métodos das super classes.
"""


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):

    def __init__(self, nome):
        super(Aquatico, self).__init__(nome)

    def cumprimentar(self):
        return f'Eu sou o {self._Animal__nome} do mar!'

    def nadar(self):
        return f'{self._Animal__nome} está nadando!'


class Terrestre(Animal):

    def __init__(self, nome):
        super(Terrestre, self).__init__(nome)

    def cumprimentar(self):
        return f'Eu sou o {self._Animal__nome} da terra!'

    def andar(self):
        return f'{self._Animal__nome} está andando!'


class Pinguim(Aquatico, Terrestre):

    def __init__(self, nome):
        super(Pinguim, self).__init__(nome)


# Testando

baleia = Aquatico('Wally')
print(baleia.cumprimentar())
print(baleia.nadar())

tatu = Terrestre('Xim')
print(tatu.cumprimentar())
print(tatu.andar())

pinguim = Pinguim('Tux')
print(pinguim.cumprimentar())   # Eu sou o Tux do mar! - Method Resolution Order (MRO)
print(pinguim.andar())
print(pinguim.nadar())

# Objeto é instância de...

print(f'Tux é instância de Pinguim? {isinstance(pinguim, Pinguim)}')    # True
print(f'Tux é instância de Aquatico? {isinstance(pinguim, Aquatico)}')    # True
print(f'Tux é instância de Terrestre? {isinstance(pinguim, Terrestre)}')    # True
print(f'Tux é instância de Animal? {isinstance(pinguim, Animal)}')    # True
print(f'Tux é instância de Object? {isinstance(pinguim, object)}')    # True
