"""
# Exercício 1 - Crie uma função que recebe como parâmetro um número inteiro e devolve o seu dobro.


def numero(num1):
    return num1 * 2


print(numero(18))





# Exercício 2 - Faça uma função que receba a data atual (dia, mês e ano em inteiro) e exiba-a na tela
# no formato textual por extenso. Exemplo: Data: 01/01/2000, Imprimir: 1 de janeiro de
# 2000.


def data(dia, mes, ano):
    if mes == 1:
        return f'{dia}/{mes}/{ano}\n{dia} de janeiro de {ano}'
    elif mes == 2:
        return f'{dia}/{mes}/{ano}\n{dia} de fevereiro de {ano}'
    elif mes == 3:
        return f'{dia}/{mes}/{ano}\n{dia} de março de {ano}'
    elif mes == 4:
        return f'{dia}/{mes}/{ano}\n{dia} de abril de {ano}'
    elif mes == 5:
        return f'{dia}/{mes}/{ano}\n{dia} de maio de {ano}'
    elif mes == 6:
        return f'{dia}/{mes}/{ano}\n{dia} de junho de {ano}'
    elif mes == 7:
        return f'{dia}/{mes}/{ano}\n{dia} de julho de {ano}'
    elif mes == 8:
        return f'{dia}/{mes}/{ano}\n{dia} de agosto de {ano}'
    elif mes == 9:
        return f'{dia}/{mes}/{ano}\n{dia} de setembro de {ano}'
    elif mes == 10:
        return f'{dia}/{mes}/{ano}\n{dia} de outubro de {ano}'
    elif mes == 11:
        return f'{dia}/{mes}/{ano}\n{dia} de novembro de {ano}'
    elif mes == 12:
        return f'{dia}/{mes}/{ano}\n{dia} de dezembro de {ano}'
    return 'Ocorreu um erro ao especificar a data!'


print(data(7, 12, 2020))





# Exercício 3 - Faça uma função para verificar se um número é positivo ou negativo. Sendo que o valor
# de retorno será 1 se positivo, -1 se negativo e O se for igual a 0.


def verificacao(num):
    if num < 0:
        return -1
    elif num > 0:
        return 1
    return 0


print(verificacao(0))





# Exercício 4 - Faça uma função para verificar se um número é um quadrado perfeito. Um quadrado
# perfeito é um número inteiro não negativo que pode ser expresso como o quadrado de
# outro número inteiro. Ex: 1, 4, 9...


def quadrado_perfeito(num):
    raiz = num ** 0.5
    if raiz == int(raiz):
        return f'O número {num} é um quadrado perfeito!'
    return f'O número {num} NÃO é um quadrado perfeito!'

print(quadrado_perfeito(4))





# Exercício 5 - Faça uma função e um programa de teste para o cálculo do volume de uma esfera.
# Sendo que o raio é passado por parâmetro.
# V = 4/3 * pi * R³


def volume(raio):
    v = 3/4 * raio ** 3
    return f'O volume da esfera será {v}π'


raio1 = int(input('Digite o raio da esfera: '))

print(volume(raio1))





# Exercício 6 - Faça uma função que receba 3 números inteiros como parâmetro, representando horas,
# minutos e segundos, e os converta em segundos.

def conversor(hora, minuto, segundo):
    converte = hora * 3600 + minuto * 60 + segundo
    return f'O equivalente do horário {hora}:{minuto}:{segundo} é {converte} segundos!'

while True:
    horas = int(input('Digite a hora: '))
    minutos = int(input('Digite os minutos: '))
    segundos = int(input('Digite os segundos: '))

    print(f'Confirmar o horário {horas}:{minutos}:{segundos}')
    confirma = str(input('[Sim/Não]: '))

    if confirma == 'sim' or confirma == 's':
        print(conversor(hora=horas, minuto=minutos, segundo=segundos))
        break
    elif confirma == 'não' or confirma == 'n':
        print('O programa será reiniciado para que você digite o número correto!\n')
    else:
        print('comando inválido\n')


# Exercício 7 - Faça uma função que receba uma temperatura em graus Celsius e retorne-a convertida
# em graus Fahrenheit. A fórmula de conversão é: F = C * (9.0/5.0) + 32.0, sendo F a
# temperatura em Fahrenheit e C a temperatura em Celsius.

import time
import sys


def conversor(c):
    f = c * (9 / 5) + 32
    return f'A temperatura convertida em Fahrenheit é: {f}º'


while True:
    celsius = int(input('Escreva ao lado a temperatura desejada: '))
    print('Está correta a temperatura?')
    confirma = str(input('[Sim/Não] '))

    if confirma == 'sim' or confirma == 's':
        print('Carregando... Aguarde!')
        carregamento = "....................\n"
        for l in carregamento:
            sys.stdout.write(l)
            time.sleep(0.1)
        print(conversor(c=celsius))
        break
    elif confirma == 'não' or confirma == 'n' or confirma == 'nao':
        print('O programa será reiniciado!')
        carregamento = "....................\n\n"
        for l in carregamento:
            sys.stdout.write(l)
            time.sleep(0.1)
    else:
        print('Comando inválido!\nO programa será reiniciado.')
        carregamento = "....................\n\n"
        for l in carregamento:
            sys.stdout.write(l)
            time.sleep(0.1)





# Exercício 8 - Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
# hipotenusa = (a² + b²) ** 0.5. Faça uma função que receba os valores de a e b e calcule o
# valor da hipotenusa através da equação.

import sys
import time

print('-----Descobrir a hipotenusa do triângulo-----')


def triangulo(a, b):
    h = (a**2 + b**2) ** 0.5
    return f'A hipotenusa do triângulo é: {h}'


while True:
    cateto1 = int(input('Digite o 1º cateto: '))
    cateto2 = int(input('Digite o 2º cateto: '))

    print('Está correto?')
    confirma = str(input('[Sim/Não] '))

    if confirma == 'sim' or confirma == 's':
        print('Carregando... Aguarde!')
        carregamento = '............\n\n'
        for l in carregamento:
            sys.stdout.write(l)
            time.sleep(0.1)
        print(triangulo(a=cateto1, b=cateto2))
        break
    elif confirma == 'não' or confirma == 'nao' or confirma == 'n':
        print('O programa será reiniciado')
        carregamento = '............\n\n'
        for l in carregamento:
            sys.stdout.write(l)
            time.sleep(0.1)
    else:
        print('Comando inválido!')
        carregamento = '............\n\n'
        for l in carregamento:
            sys.stdout.write(l)
            time.sleep(0.1)





# Exercício 9 - Faça uma função que receba a altura e o raio de um cilindro circular e retorne o volume
# do cilindro. O volume de um cilindro circular é calculado por meio da seguinte fórmula:
# V= π * raio² * altura, onde π = 3.141592.

print('------ Calcular o volume do cilindro ------\n')


def cilindro(h, r):
    v = 3.14 * r ** 2 * h
    return f'O volume do cilindro é: {v}'


while True:
    altura = int(input('Digite a altura do cilindro: '))
    raio = int(input('Digite o raio do cilindro: '))

    confirma = str(input('[Sim/Não] -> '))

    if confirma == 'sim' or confirma == 's':
        print(cilindro(h=altura, r=raio))
        break
    else:
        print('O programa será reiniciado!\n')





# Exercício 10 - Faça uma função que receba dois números e retorne qual deles é o maior.


def funcao(num1, num2):
    if num1 > num2:
        return f'O número {num1} é maior que o número {num2}'
    return f'O número {num2} é maior que o número {num1}'


numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))

print(funcao(num1=numero1, num2=numero2))





# Exercício 11 - Elabore uma função que receba três notas de um aluno como parâmetros e uma letra.
# Se a letra for A, a função deverá calcular a média aritmética das notas do aluno;
# se for P, deverá calcular a média ponderada com pesos 5, 3 e 2.

print('----- Descobrir a média ponderada ou aritmética do aluno -----')


def media(n1, n2, n3, l):
    a = (n1 + n2 + n3) / 3
    p = (5*n1 + 3*n2 + 2*n3) / 5 + 3 + 2

    if l == 'A' or l == 'a':
        return f'A média aritmética das notas do aluno é: {a}'
    elif l == 'P' or l == 'p':
        return f'A média ponderada das notas do aluno é: {p}'
    return 'Comando inválido'


nota1 = int(input('Digite a 1º nota do aluno: '))
nota2 = int(input('Digite a 2º nota do aluno: '))
nota3 = int(input('Digite a 3º nota do aluno: '))

print('\nDeseja calcular média ponderada ou aritmética?')
letra = str(input('[Aritmética = A; Ponderada = P ->  '))

print(media(n1=nota1,n2=nota2, n3=nota3, l=letra))





# Exercício 12 - Escreva uma função que receba um número inteiro maior do que zero e retorne a soma de
# todos os seus algarismos, Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1).
# Se o número lido não for maior do que zero, o programa terminará com a mensagem “Número inválido".

print('----- Descobrir a soma dos algarismos de um número -----')


def funcao(num):
    somaresto = 0
    soma = 0
    if num > 0:
        resto1 = num % 10  # O resto da 1ª divisão
        num2 = num // 10  # Divisão do número dado pelo usuário por 10 dando resultado em número inteiro
        quociente = num2 // 10  # Divisão do resultado anterior por 10 dando resultado em número inteiro
        resto2 = num2 % 10  # O resto da 2ª divisão

        while quociente > 9:
            resto = quociente % 10  # Resto das divisões que serão calculadas para números iguais ou acima de 4 digitos
            quociente = quociente // 10  # quociente dando resultado apenas em número inteiro
            somaresto = somaresto + resto  # Aqui é onde será armazenado a soma de todos os calculos de restos

        soma = resto1 + resto2 + somaresto + quociente  # soma de todos os algarismos

        return f'\nA soma dos algarismos do número digitado é: {soma}'
    return '\nNúmero Inválido'


numero = int(input('Digite um número qualquer: '))

print(funcao(num=numero))
"""















