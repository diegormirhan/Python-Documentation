"""
Exercício 1 - Escreva um código que apresente a classe Pessoa, com atributos
nome, endereço e telefone e, o método imprimir. O método imprimir deve mostrar
na tela os valores de todos os atributos.

class Pessoa:

    def __init__(self, nome, endereco, telefone):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone

    def mostrar(self):
        return f'Me chamo {self.__nome}. Meu endereço é {self.__endereco} e meu telefone é {self.__telefone}.'


p1 = Pessoa('Diego', 'Rua Senador Severo Gomes, 192', '12 99141-0569')

print(p1.mostrar())





Execício 3 - Escreva um código que apresente a classe Quadrado, com atributos
lado, área e perímetro e, os métodos calcular Area, calcular Perimetro e imprimir.
Os métodos calcular Area e Calcular Perímetro devem efetuar seus respectivos
cálculos e colocar os valores nos atributos area e perimetro. O método imprimir
deve mostrar na tela os valores de todos os atributos. Salienta-se que a área de um
quadrado é obtida pela fórmula (lado x lado) e o perímetro (4 x lado)


class Quadrado:
    area = 0
    perimetro = 0

    def __init__(self, lado):
        self.__lado = lado
        self.__area = Quadrado.area
        self.__perimetro = Quadrado.perimetro

    def calcular_area(self):
        if isinstance(self.__lado, int):
            self.__area = self.__lado * 2
            return f'A área do quadrado é {self.__area}'
        return 'Digite um valor válido!'

    def calcular_perimetro(self):
        if isinstance(self.__lado, int):
            self.__perimetro = self.__lado * 4
            return f'O perímetro do quadrado é {self.__perimetro}'
        return 'Digite um valor válido'

    def imprimir(self):
        return f'\nO lado do quadrado é: {self.__lado}\n' \
               f'A área do quadrado é: {self.__area}\n' \
               f'O perímetro do quadrado é: {self.__perimetro}\n'


q1 = Quadrado(3)

print(q1.calcular_area())
print(q1.calcular_perimetro())
print(q1.imprimir())





Exercício 5 - Escreva um código que apresente a classe Retângulo, com atributos
comprimento, largura, área e perímetro e, os métodos Calcular Área, Calcular Perímetro
e imprimir. Os métodos Calcular Área e Calcular Perímetro devem efetuar seus respectivos
cálculos e colocar os valores nos atributos área e perímetro. O método imprimir
deve mostrar na tela os valores de todos os atributos. Salienta-se que a área de um
retângulo é obtida pela fórmula (comprimento * largura) e o perímetro por (2 * comprimeto)
+ (2 * largura).

class Retangulo:

    area = 0
    perimetro = 0

    def __init__(self, comprimento, largura):
        self.__comprimento = comprimento
        self.__largura = largura
        self.__area = Retangulo.area
        self.__perimetro = Retangulo.perimetro

    def calcular_area(self):
        if isinstance(self.__comprimento and self.__largura, int):
            self.__area = self.__comprimento * self.__largura
            return self.__area
        return 'Digite um valor válido!'

    def calcular_perimetro(self):
        if isinstance(self.__comprimento and self.__largura, int):
            self.__perimetro = (2 * self.__comprimento) + (2 * self.__largura)
            return self.__perimetro
        return 'Digite um valor válido!'

    def imprimir(self):
        return f'\nO retângulo possui comprimento de {self.__comprimento}m;\n' \
               f'O retângulo possui largura de {self.__largura}m;\n' \
               f'O retângulo possui área de {self.__area}m;\n' \
               f'O retângulo possui perímetro de {self.__perimetro}m;\n'


rt1 = Retangulo(6, 4)

print(rt1.calcular_area())
print(rt1.calcular_perimetro())
print(rt1.imprimir())





Exercício 7 - Escreva um código que apresente a Classe Círculo, com atributos raio, área
e perímetro e, os métodos Calcular Area, Calcular Perimetro e Imprimir. Os métodos Calcular Area
e Calcular Perimetro devem efetuar seus respectivos cálculos e colocar os valores nos atributos
area e perimetro. O método Imprimir deve mostrar na tela os valores nos atributos. Salienta-se
que a área de um círculo é obtida pela fórmula (pi * raio * raio) e o perímetro por (2 * pi * raio),
onde pi = 3,14.

class Circulo:

    area = 0
    perimetro = 0

    def __init__(self, raio):
        self.__raio = raio
        self.__area = Circulo.area
        self.__perimetro = Circulo.perimetro

    def calcular_area(self):
        if isinstance(self.__raio, int):
            self.__area = (self.__raio ** 2) * 3.14
            return self.__area
        return 'Digite um valor válido'

    def calcular_perimetro(self):
        if isinstance(self.__raio, int):
            self.__perimetro = 2 * 3.14 * self.__raio
            return self.__perimetro
        return 'Digite um valor válido'

    def imprimir(self):
        return f'\nO círculo possui raio de {self.__raio}m;\n' \
               f'O círculo possui área de {self.__area}m²;\n' \
               f'O círculo possui perímetro de {self.__perimetro}m;\n'


c1 = Circulo(7)

print(c1.calcular_area())
print(c1.calcular_perimetro())
print(c1.imprimir())





Exercício 9 - Escreva um código que apresente a classe Moto, com atributos marca, modelo, cor e
marcha, e, o método imprimir. O método imprimir deve mostrar na tela os valores de todos os atributos.
O atributo marcha indica em que a marcha da Moto se encontra no momento, sendo representado de
forma inteira, onde 0 - neutro, 1 - primeira, 2 - segunda, etc.

Adicione os métodos Marcha Acima e Marcha Abaixo que deverão efetuar a troca de marchas, onde o
método Marcha Acima deverá subir uma marcha, ou seja, se a moto estiver em primeira marcha, deverá
ser trocada para a segunda marcha e assim por diante. O método Marcha Abaixo deverá realizar o
oposto, ou seja, descer a marcha. O método imprimir deve ser modificado de forma a mostrar na
tela os valores de todos os atributos.

Adicione os atributos Menor Marcha e Maior Marcha, onde o atributo Menor Marcha indica qual será a menor
marcha possível para a moto e o atributo Maior Marcha indica qual será a maior marcha possível. Desta
forma os métodos Marcha Acima e Marcha Abaixo deve ser reescritos de forma a não permitirem  a troca
de marchas para valores abaixo de Menor Marcha e acima de Maior Marcha. O método imprimir deve ser
modificado de forma a mostrar na tela os valores de todos os atributos.

Adicione o atributo ligada que terá a função de indicar se a moto está ligada ou não. Este atributo
deverá ser do tipo booleano. O método imprimir deve ser modificado de forma a mostrar na tela os valores
de todos os atributos.

Adicione os métodos ligar e desligar que deverão mudar o conteúdo do atributo ligada conforme o caso.


"""


class Moto:

    def __init__(self, marca, cor, marcha, maior_marcha):
        self.__marca = marca
        self.__cor = cor
        self.__marcha = marcha
        self.__menor_marcha = 0
        self.__maior_marcha = maior_marcha
        self.__ligada = True

    def marcha_acima(self):
        if isinstance(self.__marcha, int):
            if self.__marcha >= self.__menor_marcha:
                if self.__marcha < self.__maior_marcha:
                    self.__marcha += 1
                    return f'A moto aumentou 1 marcha e agora está na {self.__marcha}º marcha!'
                elif self.__marcha == self.__maior_marcha:
                    return 'A moto já está na maior marcha!'
                return 'Digite um valor válido!'
            return 'O valor precisa ser maior ou igual a zero!'
        return 'Digite um valor válido!'

    def marcha_abaixo(self):
        if isinstance(self.__marcha, int):
            if self.__marcha <= self.__maior_marcha:
                if self.__marcha > self.__menor_marcha:
                    self.__marcha -= 1
                    return f'A moto diminuiu 1 marcha e agora está na {self.__marcha}º marcha!'
                elif self.__marcha == self.__menor_marcha:
                    return 'A moto já está na menor marcha!'
                return 'Digite um valor válido!'
            return 'O valor precisa ser menor ou igual ao valor da maior marcha!'
        return 'Digite um valor válido!'

    def ligar(self):
        self.__ligada = True
        return 'A moto agora está ligada!'

    def desligar(self):
        self.__ligada = False
        return 'A moto agora está desligada!'

    def imprimir(self):
        if isinstance(self.__marcha, int):
            if self.__marcha >= self.__menor_marcha:
                if self.__marcha <= self.__maior_marcha:
                    return f'Caraterísticas da moto:\n' \
                           f'-> Marca: {self.__marca}\n' \
                           f'-> Cor: {self.__cor}\n' \
                           f'-> Marcha: {self.__marcha}º\n' \
                           f'-> Maior Marcha: {self.__maior_marcha}\n' \
                           f'-> Menor Marcha: {self.__menor_marcha}\n' \
                           f'-> Ligada: {self.__ligada}\n'
                return f'O valor da marcha precisa ser menor ou igual a {self.__maior_marcha}'
            return f'O valor da marcha precisa ser maior ou igual a {self.__menor_marcha}'
        return 'Digite um valor válido para a marcha!'


m1 = Moto('Honda', 'Dourado', 3, 7)
print(m1.imprimir())

print(m1.marcha_abaixo())
print(m1.desligar())
print(m1.imprimir())

