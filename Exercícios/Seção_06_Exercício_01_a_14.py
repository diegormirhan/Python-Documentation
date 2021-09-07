"""
# Exercício 1 - Faça um programa que determine ou mostre os cinco primeiros múltiplos de 3,
# considerando números maiores que 0.

numero = 0

for numero in range(1, 6):
    print(f'{numero * 3}')





# Exercício 2 - Escreva um programa que escreva na tela, de 1 até 100, de 1 em 1, 3 vezes. A primeira vez deve usar
# a estrutura de repetição for, a segunda while, e a terceira do while.

print('Primeira vez:')

for numero in range(1, 101):
    print(numero)

print('\nSegunda vez:')
numero = 0

while numero <= 99:
    numero = numero + 1
    print(numero)






# Exercício 3 - Faça um algorítimo utilizando o comando while que mostra uma contagem regressiva na tela,
# iniciando em 10 e terminando em 0. Mostrar uma mensagem "FIM!" após a contagem.

numero = 11

while numero >= 1:
    numero = numero - 1
    print(numero)
print('Fim!')





# Exercício 4 - Escreva um programa que declare um inteiro, inicialize-o com 0, e incremente-o de 1000 em 1000,
# imprimindo seu valor na tela, até que seu valor seja 100000 (cem mil).

num = 0

while num <= 100000:
    print(num)
    num = num + 1000





# Exercício 5 - Faça um programa que peça ao usúario para digitar 10 valores e some-os

soma = 0
num = 1

for num in range(1, 11):
    valor = int(input(f'Digite o {num} número: '))
    soma = soma + valor
print(f'A soma dos números digitados é: {soma}')





# Exercício 6 - Faça um programa que leia 10 inteiros e imprima sua média

media = 0
soma = 0
num = 0

for num in range(1, 11):
    valor = int(input(f'Digite o {num}º número: '))
    soma = soma + valor
media = soma / num
print(f'A média é: {media}')





# Exercício 7 - Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média.

valor = 0
soma = 0
media = 0

for num in range(1, 11):
    valor = valor + 5
    print(valor)
    soma = soma + valor

media = soma / 10
print(f'A média é: {media}')





# Exercício 8 - Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.

numero = 0
maior = 0
menor = 100000
num = 0
for num in range(1, 11):
    numero = int(input(f'Digite o {num}º número: '))
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')





# Exercício 9 - Faça um programa que leia um número inteiro N e depois imprima os N primeiros números naturais ímpares

n = int(input('Digite um número: '))

print(f'Os primeiros {n} números ímpares naturais são: ')
for num in range(1, n + 1):
    if num % 2 != 0:
        print(num)





# Exercício 10 - Faça um programa que calcule e mostre a soma dos 50 primeiros números pares.


num = 0
soma = 0
print('A soma dos 50 primeiros números pares é:')

for num in range(1, 51):
    if num % 2 == 0:
        soma = soma + num
print(soma)





# Exercício 11 - Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais de 0 até N
# em ordem crescente.

num = int(input('Digite um número inteiro positivo: '))
if num > 0:
    print(f'Todos os números naturais de 0 até {num} em ordem crescente são:')
    for n in range(num + 1):
        print(n)
else:
    print('Reinicie o programa e digite um número válido!')





# Exercício 12 - Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais de 0 até N
# em ordem decrescente.

num = int(input('Digite um número inteiro positivo: '))

if num > 0:
    print(f'Os números naturais de 0 até {num} em ordem decrescente são:')
    for n in range(num, 0, -1):
        print(n)
else:
    print('Reinicie o programa e digite um número válido!')





# Exercício 13 - Faça um programa que leia um número inteiro positivo par N e imprima todos os números naturais
# de 0 até N em ordem crescente.

num = int(input('Digite um número inteiro positivo: '))

if num > 0 and num % 2 == 0:
    print(f'Todos os números naturais de 0 até {num} em ordem crescente são:')
    for n in range(1, num):
        print(n)
else:
    print('Reinicie o programa e digite um número válido!')





# Exercício 14 - Faça um programa que leia um número inteiro positivo par N e imprima todos os números naturais
# de 0 até N em ordem decrescrescente.

num = int(input('Digite um número inteiro positivo e par: '))

if num > 0 and num % 2 == 0:
    for n in range(num, 0, -1):
        print(n)
else:
    print('Reinicie o programa e digite um válido!')
"""


