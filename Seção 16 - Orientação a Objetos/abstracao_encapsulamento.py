"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo
lógico e hierárquico utilizando classes.

Encapsular -> cápsula


            classe
_________________________________________
|                                       |
|          atributos e métodos          |
|                                       |
|_______________________________________|

# Relembrando Atributos/Métodos privados em Python
Imagine que temos ma classe chamada Pessoa, contendo
um atributo privado chamado __nome e um método privado
chamado __falar()

Esses elementos privados só devem/deveriam ser acessados
dentro da classe. Mas Python não bloqueia este acesso
fora da classe. Com python acontece um fenômeno chamado
Name Mangling, que faz uma alteração na forma de se acessar
os elementos privados, conforme:

_Classe__elemento

Exemplo - Acessando elementos fora da classe:

instancia._Pessoa__nome

instancia._Pessoa__falar()



Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo
atributos e métodos privados de usuário.



print(conta1.__dict__)

conta1.extrato()

print(conta1._Conta__titular)  # Name Mangling

conta1._Conta__titular = 'Anna Mirhan'

print(conta1.__dict__)


print(conta1.__dict__)

conta1.depositar(150)

print(conta1.__dict__)

conta1.sacar(1000)

print(conta1.__dict__)

"""


class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo Insuficiente')
        else:
            print('O valor precisa ser positivo')

    def tranferir(self, valor, conta_destino):
        """ 1 - Remover o valor da conta de origem """
        self.__saldo -= valor
        self.__saldo -= 10  # saldo de transferência

        """ 2 - Adicionar o valor na conta de destino """
        conta_destino.__saldo += valor


# Testando

conta1 = Conta('Diego Mirhan', 150.00, 1500)
conta1.extrato()

conta2 = Conta('Felicity', 300, 2000)
conta2.extrato()

conta2.tranferir(200, conta1)

conta1.extrato()
conta2.extrato()






