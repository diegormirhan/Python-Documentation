"""
Json e Pickle

Json -> JavaScript Object Notation

API -> São meios de comunicação entre os serviços oferecidos por empresas
(Twitter, Facebook, YouTube...) a terceiros (nós desenvolvedores).

import json

ret = json.dumps(['produto', {'Playstaion 5': ('2TB', 'Novo', '220V', 2500)}])  # reformata a string e o dicionário

print(type(ret))
print(ret)




import json


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Vira-Lata')
print(felix.__dict__)

ret = json.dumps(felix.__dict__)
print(ret)

Integrando Json com Pickle
pip install jsonpickle


import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Vira-Lata')

ret = jsonpickle.encode(felix)
print(ret)




# Escrevendo o arquivo json/pickle
import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Vira-Lata')

with open('felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)
"""
# Lendo o arquivo json/pickle
import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Vira-Lata')

with open('felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)



