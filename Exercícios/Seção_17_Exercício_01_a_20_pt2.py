"""
-> 1 - Crie um novo pacote com o nome herança. Todas as 3 classes criadas
abaixo deverão ser salvas nesse pacote.
-> 2 - Crie uma classe Equipamento com dois atributos privados.
-> 3 - Crie uma classe Computador com dois atributos à sua escolha, também
privados. A classe Computador herdará tudo da classe Equipamento.
-> 4 - Crie os métodos de acesso e de modificação para todos os atributos
definidos em ambas as classes.
-> 5 - Crie uma classe Testa Equipamento, que deverá contar o método main(),
crie nela um objeto da classe Equipamento e instancie os dois atributos
que você declarou na Classe Equipamento. Crie também um objeto da classe
Computador, utilizando os dois atributos declarados na própria classe e os
dois herdados da classe Equipamento.
-> 6 - O método main() deve exibir as informações dos dois objetos criados.
-> 7 - Criar o método exibe() na classe Equipamento para mostrar os dados
dessa classe.
-> 8 - Reescreva o método exibe() na classe Computador, aproveitando o que
já está escrito na superclasse Equipamento.
"""


class Equipamento:

    def __init__(self, modelo, peso):
        self.__modelo = modelo
        self.__peso = peso

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, novo_modelo):
        self.__modelo = novo_modelo

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, novo_peso):
        self.__peso = novo_peso


class Computador(Equipamento):

    def __init__(self, modelo, peso, cor, resolucao):
        super(Computador, self).__init__(modelo, peso)
        self.__cor = cor
        self.__resolucao = resolucao

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, novo_modelo):
        self.__modelo = novo_modelo

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, novo_peso):
        self.__peso = novo_peso

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, nova_cor):
        self.__cor = nova_cor

    @property
    def resolucao(self):
        return self.__resolucao

    @resolucao.setter
    def resolucao(self, nova_resolucao):
        self.__resolucao = nova_resolucao

