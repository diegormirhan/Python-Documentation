"""
# Exercício 1 - Faça um programa que receba dois números  e mostre qual deles é maior.

num1 = 20
num2 = 40

print(f'Dados os números {num1} e {num2},')

if num1 > num2:
    print(f'O número {num1} é maior')
else:
    print(f'O número {num2} é maior')





# Exercício 2 - Leia um nümero fornecido pelo usuårio. Se esse nümero for positivo, calcule a raiz quadrada do nümero.
# Se o nümero for negativo, mostre uma mensagem dizendo que o nümero é invålido.

num1 = int(input('Digite um número: '))

if num1 >= 0:
    num1 = num1 ** (1/2)
    print(f'A raiz quadrada do número digitado é {num1}')
else:
    print('O número digitado é inválido')





# Exercício 3 - Leia um numero real. Se o nümero for positivo imprima a raiz quadrada.
# Do contrário, imprima o numero ao quadrado.

num1 = 16
print(f'Dado o número {num1},')

if num1 >= 0:
    num1 = num1 ** (1/2)
    print(f'A raiz quadrada é {num1}')
else:
    num1 **= 2
    print(f'O mesmo elevado ao quadrado é {num1}')





# Exercício 4 - Faga um programa que leia um nümero e, caso ele seja positivo, calcule e mostre:
# • O nümero digitado ao quadrado
# • A raiz quadrada do nümero digitado

num = 49
print(f'Dado o número {num}:')

if num >= 0:
    print(f'O mesmo digitado ao quadrado é {num ** 2} e sua raiz quadrada é {num ** (1/2)}!')
else:
    print('O mesmo é inválido!')





# Exercício 5 - Faga um programa que receba um nümero inteiro e verifique se este nümero é par ou impar.

num = 11
print(f'Temos o valor {num};')

if num % 2 == 0:
    print('O número é par')
else:
    print('O número é ímpar')





# Exercício 6 - Escreva um programa que, dados dois nümeros inteiros,
# mostre na tela o maior deles, assim como a diferenqa existente entre ambos.

num1 = 10
num2 = 30

print(f'Dados dois números {num1} e {num2}:')

if num1 > num2:
    print(f'O maior deles é {num1};')
    print(f'A diferença entre eles é {num1 - num2}')
else:
    print(f'O maior deles é {num2};')
    print(f'A diferença entre eles é {num2 - num1}')





# Exercício 7 - Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois
# números forem iguais, imprima a mensagem Números iguais.

num1 = 20
num2 = 10

print(f'Dado dois números {num1} e {num2},')

if num1 > num2:
    print(f'O {num1} é maior')

elif num2 > num1:
    print(f'O {num2} é maior')

else:
    print('São números iguais')





# Exercício 8 - Faga um programa que leia 2 notas de um aluno, verifique se as notas são válidas e
# exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente, um
# valor entre 0.0 e 10.0, onde Caso a nota não possua um valor válido, este fato deve ser
# informado ao usuário e o programa termina.

print('Digite abaixo duas notas de um aluno entre 0.0 e 10.1')

nota1 = int(input('Primeira nota: '))
nota2 = int(input('Segunda nota: '))

if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
    print(f'Um aluno possui duas notas; {nota1} e {nota2}.')
    media = (nota1 + nota2) / 2
    print(f'A média das notas é: {media}.')

else:
    print('O aluno possui notas inválidas. Por favor insira notas válidas')





# Exercício 9 - Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a
# prestação for maior que 20% do salário imprima: Empréstimo não concedido, Caso
# contrario imprima: Empréstimo concedido.

# 100   200
# 20     x

salario = 1000
prestacao = 300

if prestacao > (20 * salario) / 100:
    print('Empréstimo Não Concedido!')
else:
    print('Empréstimo Concedido')





# Exercício 10 - Faga um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu
# peso ideal, utilizando as seguintes fórmulas (onde h corresponde altura):
# Homens: (72.7 * h) - 58
# Mulheres: (62,1 * h) - 44, 7

altura = float(input('Digite a sua altura: '))
sexo = (input('Digite o seu sexo: '))
sexo = sexo.lower()

if sexo == 'masculino' or sexo == 'homem':
    peso_ideal = (72.7 * altura) - 58
    print(f'Seu peso ideal é: {peso_ideal}')

elif sexo == 'feminino' or sexo == 'mulher':
    peso_ideal = (62.1 * altura) - 44.7
    print(f'Seu peso ideal é: {peso_ideal}')

else:
    print('Não foi possível identificar o sexo digitado! Reinicie o programa e tente novamente!')
"""


