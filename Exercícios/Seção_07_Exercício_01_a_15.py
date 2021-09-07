"""
Exercício 1 - Faça um programa que possua um vetor denominado A que armazene 6 números inteiros.
O programa deve executar os seguintes passos:
(a) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2,-5, 7
(b) Armazene em uma varíavel inteira (simples) a soma entre os valores das posições
A[O], A[1]‚ A[5] do vetor e mostre na tela esta soma.
(c) Moditique o vetor na posição 4, atrbuindo a esta posição o valor 100.
(d) Mostre na tela cada valor do vetor A, um em cada linha.

s = 1

print('---------------------')
print('Exercício 1')
print(f'---------------------\n')

vetor = [1, 0, 5, -2, -5, 7]
print(vetor)

soma = vetor[0] + vetor[1] + vetor[5]
print(f'soma = {soma}\n')

vetor[4] = 100

for n in vetor:
    print(f'{s}º valor: {n}')
    s = s + 1





Exercício 2 - Crie um programa que leia 6 valores inteiros , em seguida, mostre na tela os valores lidos.

print('---------------------')
print('Exercício 2')
print(f'---------------------\n')

valores = 1, 2, 3, 4, 5, 6
print(f'valores = {valores}')





Exercício 3 - Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado das
componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos têm
10 elementos cada. Imprimir todos os conjuntos.

vetor2 = set({})
print('---------------------')
print('Exercício 3')
print(f'---------------------\n')

vetor1 = set({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
print(f'Vetor 1 = {vetor1}\n')

for n in vetor1:
    s = n ** 2
    vetor2.add(s)

print(f'Vetor 2 = {vetor2}')





Exercício 4 - Faça um programa que leia um vetor de 8 posições e, em seguida, leia também dois valores X e Y
quaisquer correspondentes a duas posições no vetor. Ao final seu programa deverá escrever a soma dos valores
encontrados nas respectivas posições X e Y.

print('---------------------')
print('Exercício 4')
print(f'---------------------\n')

vetor = [10, 43, 32, 48, 23, 49, 79, 58]
print(f'Vetor = {vetor}\n')

x = vetor[2]
print(f'X = {x}')

y = vetor[5]
print(f'Y = {y}\n')

soma = x + y
print(f'Soma = {soma}')





Exercício 5 - Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui.

s = 0
print('---------------------')
print('Exercício 5')
print(f'---------------------\n')

vetor = (10, 43, 32, 48, 23, 49, 79, 58, 2, 55)
print(f'Vetor = {vetor}\n')

for n in vetor:
    if n % 2 == 0:
        s = s + 1

print(f'O vetor possui {s} números pares')





Exercício 6 - Faça um programa que receba do usuário um vetor com 10 pasições. Em seguida deverá
ser impresso o maior e o menor elemento do vetor.

print('---------------------')
print('Exercício 6')
print(f'---------------------\n')

vetor = [10, 43, 32, 48, 23, 49, 79, 58, 2, 55]
print(f'Vetor = {vetor}\n')

print(f'Menor valor = {min(vetor)}')
print(f'Maior valor = {max(vetor)}')





Exercício 7 - Escreva um programa que leia 10 números inteiros e os armazene em um vetor. Imprima
o vetor, o maior elemento e a posiGäo que ele se encontra.

print('---------------------')
print('Exercício 7')
print(f'---------------------\n')

numeros = 23, 55, 64, 56, 3, 5, 32, 94, 77, 88
print(f'Numeros = {numeros}')

vetor = list(numeros)

print(f'Vetor = {vetor}\n')

print(f'Maior elemento = {max(vetor)}')
print(f'Posição = {vetor.index(max(vetor))}\n')

print(f'Menor valor = {min(vetor)}')
print(f'Posição = {vetor.index(min(vetor))}\n')

print('VALORES PARES:')
for n in vetor:
    if n % 2 == 0:
        print(f'O valor par {n} está na posição {vetor.index(n)}')

print('')
print('VALORES ÍMPARES:')

for s in vetor:
    if s % 2 == 1:
        print(f'o valor ímpar {s} está na posição {vetor.index(s)}')

print('')

g = 0

for f in vetor:
    if f % 2 == 0:
        if f > g:
            g = f
print(f'O maior valor par: {g}')
print(f'Posição: {vetor.index(g)}')

print('')

h = 0

for j in vetor:
    if j % 2 == 1:
        if j > h:
            h = j
print(f'O maior valor ímpar: {h}')
print(f'Posição: {vetor.index(h)}')





Exercício 8 - Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos
na ordem inversa.

print('---------------------')
print('Exercício 8')
print(f'---------------------\n')

valores = [21, 72, 77, 95, 54, 80]
print(f'Valores = {valores}\n')

valores.reverse()
print(f'Ordem Inversa = {valores}')





Exercício 9 -  Crie um programa que lê 6 valores inteiros, em seguida, mostre na tela os valores
lidos na ordem inversa.

print('---------------------')
print('Exercício 9')
print(f'---------------------\n')

valores = [22, 84, 90, 10, 8, 66]
print(f'Valores = {valores}\n')

valores.reverse()
print(f'Ordem Inversa = {valores}')





Exercício 10 - Faça um programa para ler a nota da prova de 15 alunos e armazene em um vetor, calcule
e impima a média geral.

print('---------------------')
print('Exercício 10')
print(f'---------------------\n')

soma = float()

vetor = {'a1': 8, 'a2': 7, 'a3': 5.3, 'a4': 7.4, 'a5': 10, 'a6': 9.1, 'a7': 9.5, 'a8': 8.3, 'a9': 7.7, 'a10': 3.3,
         'a11': 6.9, 'a12': 10, 'a13': 9.1, 'a14': 9, 'a15': 8.5}

print(vetor)

for s in vetor.values():
    soma = soma + s

media = soma / 15
print(f'\nMédia = {media}')





Exercício 11 - Faça um programa que preencha um vetor com 10 números reais, calcule e mostre a
quantidade de números negativos e a soma dos númercs positivos desse vetor.

print('---------------------')
print('Exercício 11')
print(f'---------------------\n')

vetor1 = [-10, 23, -100, 83, -75, -43, 60, 91, -97, 66]
print(f'Valores = {vetor1}\n')

vetor2 = []
vetor3 = []

soma1 = 0
soma2 = 0

for s in vetor1:
    if s < 0:
        vetor2.append(s)
        soma1 = soma1 + s
    else:
        vetor3.append(s)
        soma2 = soma2 + s

print(f'Valores Negativos = {vetor2}')
print(f'Soma = {soma1}\n')

print(f'Valores Positivos = {vetor3}')
print(f'Soma = {soma2}')





Exercício 12 - Fazer um programa para ler 5 valores e, em seguida, mostre todos os valores lidos
juntamente com o maior, o menor e a média dos valores.

print('---------------------')
print('Exercício 12')
print(f'---------------------\n')

valores = [43, 77, 1, 9, 76, 763, 7, 1]
print(f'Valores = {valores}\n')

soma = 0
media = 0

for s in valores:
    soma = soma + s

media = soma / len(valores)

print(f'Maior = {max(valores)}')
print(f'Menor = {min(valores)}')
print(f'Média = {media}')





Exercício 13 - Fazer um programa para ler 5 valores e, em seguida, mostrar a posição onde se encontram
o maior e menor valor.

print('---------------------')
print('Exercício 13')
print(f'---------------------\n')

vetor1 = [43, 77, 1, 9, 768]
print(f'Valores = {vetor1}\n')

maior, menor = 0, 100000

for s in vetor1:
    if s > maior:
        maior = s
    if s < menor:
        menor = s

print(f'Posição do maior = {vetor1.index(maior)}')
print(f'Posição do menor = {vetor1.index(menor)}')


"""







