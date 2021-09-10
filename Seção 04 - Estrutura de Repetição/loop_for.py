"""
Loop for

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas.

C ou Java

for(i = 0; i < 10; i++) {
    //execução do loop
}

Python

for item in interavel:
    //esecução do loop


Utilixamos loops para iterar sobre sequências ou sobre valores iteráveis.

Exemplos de iteráveis:
- String
    nome = 'Diego Mirhan'
- Lista
    lista = [1, 3 ,5, 7, 9]
- Range
    numeros = range(1, 10)

nome = 'Diego Mirhan'
lista = [1, 3, 5, 7, 9]
valores = range(1, 10)  # Temos que transformar em uma lista

# Exemplo de For 1 (Iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de For 2 (iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de For 3 (Iterando sobre um range)

range(valor_inicial, valor_final)

OBS: o valor final não é inclusive.
1
2
3
4
5
6
7
8
9
10 - Não

for numero in range(1, 10):
    print(numero)


Enumerate:
((0, 'D'), (1, 'i'), (2, 'e'), (3, 'g'), (4, 'o')...)

for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

OBS: Quando não precisamos de um valor, podemos descartá-lo utilizando um underline (_)

for _, letra in enumerate(nome):
    print(letra)


quantidade = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, quantidade + 1):
    num = int(input(f'Digite o {n}º número: '))
    soma = soma + num

print(f'A soma é: {soma}')

nome = 'Diego Mirhan'
for letra in nome:
    print(letra, end='')

Tabela de emojis: https://apps.timwhitlock.info/emoji/tables/unicode

# Emoji:

# Original: U+1F60D
# Modificado: U0001F60D
for _ in range(3):
    for num in range(1, 11):
        print(f'\U0001F60D' * num)

"""


