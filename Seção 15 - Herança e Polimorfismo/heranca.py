"""
POO - Herança (Inheritance)

A ideia de herança é a de reaproveitar código. Também extender nossa classes.

OBS: Com a herança, a partir de uma classe existente, nós extendemos outra
classe que passa a herdar atributos e métodos da classe herdada.

Cliente
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionário;
    - nome;
    - sobrenome;
    - cpf;
    - matrícula;

Pergunta: Existe alguma entidade genérica o suficiente para encapsular o atributos
e métodos comuns a outras entidades?


class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


cliente1 = Cliente('Diego', 'Mirhan', '123.456.789-00', 8432)
funcionario1 = Funcionario('Anna', 'Mirhan', '098.765.432-11', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

OBS: Quando uma classe herda de outra classe ela herda TODOS os atributos e métodos da classe herdada.

Quando uma classe herda de outra classe, a classe herdada é conhecida por:
    [Pessoa]
    - Super Classe;
    - Classe Mãe;
    - Classe Pai;
    - Classe Base;
    - Classe Genérica;

Quando uma classe herda de outra classe, ela é chamada de:
    [Cliente, Funcionario]
    - Sub Classe;
    - Classe Filha;
    - Classe Específica;



class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    #  Cliente herda de Pessoa
    def __init__(self, nome, sobrenome, cpf, renda):
        super(Cliente, self).__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    #  Funcionário herda de Pessoa
    def __init__(self, nome, sobrenome, cpf, matricula):
        super(Funcionario, self).__init__(nome, sobrenome, cpf)
        self.__matricula = matricula


cliente1 = Cliente('Diego', 'Mirhan', '123.456.789-00', 8432)
funcionario1 = Funcionario('Anna', 'Mirhan', '098.765.432-11', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

print(funcionario1.__dict__)
print(cliente1.__dict__)

# Sobrescrita de Métodos (Overriding)

Sobrescrita de método, ocorre quando reescrevemos/reimplementamos um método
presente na super classe em classes filhas.
"""


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    """Cliente herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, renda):
        super(Cliente, self).__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionário herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, matricula):
        super(Funcionario, self).__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        print(super(Funcionario, self).nome_completo())
        print(self._Pessoa__cpf)
        return f'Funcionário: {self.__matricula}  Nome: {self._Pessoa__nome}'


cliente1 = Cliente('Diego', 'Mirhan', '123.456.789-00', 8432)
funcionario1 = Funcionario('Anna', 'Mirhan', '098.765.432-11', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

