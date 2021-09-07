"""

# Exercício 1 - Faça um programa que leia um número inteiro e o imprima.

num = 40
print(num)





# Exercício 2 - Faça um programa que leia um número real e o imprima.

num = 2.5
print(num)





# Exercício 3 - Peça ao usuário digitar três valores inteiros e imprima a soma deles.

num1 = int(input('Digite o 1º número:\n'))
num2 = int(input('Digite o 2º número:\n'))
num3 = int(input('Digite o 3º número:\n'))

print(' ')

soma = num1 + num2 + num3

print(f'A soma dos 3 números digitados é {soma}')





# Exercício 4 - Leia um número real e imprima o resultado do quadrado desse número.

num = 10.5
print(f'Dado que um número é {num}')

num **= 2
print(f'Sua resultado elevado ao quadrado será {num}')





# Exercício 5 - Leia um número real e imprima a quinta parte desse número

num = 25
print(f'Dado que um número é {num}')

num /= 5
print(f'Sua quinta parte será {num}')





# Exercício 6 - Leia uma temperatura em Graus Celsius e apresente-a convertida em graus Fahrenheit.
# A fórmula de conversão é: F = C * (9/5) + 32, sendo F a temperatura em Fahrenheit
# e C a temperatura em Celsius.

c = 25
print(f'Dado que a temperatura em uma cidade seja {c}ºC.')

f = c * (9/5) + 32
print(f'Sua temperatura em fahrenheit será de {f}ºF ')





# Exercício 7 - Leia uma temperatura em Graus Fahrenheit e apresente-a convertida em graus Celsius.
# A fórmula de conversão é: C = 5 * (F - 32) / 9, sendo F a temperatura em Fahrenheit
# e C a temperatura em Celsius.

f = 77
print(f'Dado que a temperatura de uma cidade é {f}ºF.')

c = 5 * (f - 32) / 9
print(f'Sua temperatura em Celsius será de {c}ºC.')





# Exercício 8 - Leia uma temperatura em Graus kelvin e apresente-a convertida em Graus Celsius.
# A fórmula de conversão é: C = K - 273, sendo C a temperatura em Celsius e K a temperatura em Kelvin.

k = 300
print(f'Dado que a temperatura de um frasco é {k}K')

c = k - 273
print(f'Sua temperatura em Celsius é {c}º')





# Exercício 9 - Leia uma temperatura em Graus Celsius e apresente-a convertida em Graus kelvin.
# A fórmula de conversão é: K = C + 273, sendo C a temperatura em Celsius e K a temperatura em Kelvin.

c = 27
print(f'Dado que um frasco está a {c}º Celsius.')

k = c + 273
print(f'Sua temperatura em kelvin é {k}K')





# Exercício 10 - Leia uma velocidade em km/h e apresente-a convertida em m/s. A fórmula de conversão é: M = K/3.6,
# sendo K a velocidade em km/h e M em m/s.

k = 90
print(f'Sendo um carro a {k}km/h.')

m = k / 3.6
print(f'Sua velocidade em m/s é {m}.')





# Exercício 11 - Leia uma velocidade em m/s e apresente-a convertida em km/h. A fórmula de conversão é: K = M * 3.6,
# sendo K a velocidade em km/h e M em m/s.

m = 10
print(f'Sendo um carro a {m}m/s.')

k = m * 3.6
print(f'Sua velocidade em km/h é {k}.')





# Exercício 12 - Leia uma distância em milhas e apresente-a convertida em quilómetros.
# A fórmula da conversão é: K = 1.61 * M, sendo K a distância em quilómetros e M a distância em milhas.

m = 160
print(f'Dada a velocidade de um carro que está a {m} milhas,')

k = 1.61 * m
print(f'Sua velocidade em quilómetros é {k}km/h!')





# Exercício 13 - Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lidos

num1 = 2
num2 = 4
num3 = 6

print(f'dado os valores {num1}, {num2} e {num3},')
total = num1 ** 2 + num2 ** 2 + num3 ** 2
print(f'A soma dos quadrados dos três valores é: {total}')





# Exercício 14 - Leia um número inteiro e imprima seu antecessor e seu sucessor.

num = 20

print(f'O antecessor e sucessor de {num} é respectivamente {num - 1} e {num + 1}.')
"""


