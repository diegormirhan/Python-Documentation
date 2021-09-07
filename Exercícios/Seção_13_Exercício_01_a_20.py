"""
Seção 13 - Exercícios

# Exercício 1 - a) crie um arquivo de nome "arq.txt"
# b) Permita que o usuário grave diversos caracteres nesse arquivo, até que o usuário entre com o caractére 0
# c) feche o arquivo
# Agora, abra e leia o arquivo, caractere por caractere, e escreva na tela todos os caracteres armazenados


text = str

with open('arq.txt', encoding='UTF-8', mode='w') as archive1:
    while True:
        text = input("Escreva o que deseja inserir no arquivo: ")
        if '0' in text:
            break
        else:
            archive1.write(text)
            archive1.write('\n')

print('\n\n')

archive1 = open('arq.txt', encoding='UTF-8', mode='r')
print(archive1.read())
archive1.close()





# Exercício 2 - Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas linhas
# esse arquivo possui

import os
from colorama import Fore

print(Fore.CYAN + "-*- Exercício 2 -*-")

nome_arquivo = input(Fore.WHITE + 'Digite o nome do arquivo: ')

with open(f'{nome_arquivo}.txt', encoding='UTF-8', mode='w') as archive:
    print("Escreva o que deseja inserir no arquivo e no fim escreva 'STOP':")
    while True:
        text = input("")
        if 'STOP' in text:
            break
        else:
            archive.write(text)
            archive.write('\n')

print('\n')

with open(f'{nome_arquivo}.txt', encoding='UTF-8', mode='r') as archive1:
    print("Quantidade de linhas do arquivo " + Fore.BLUE + f'{archive1.name}')
    soma = 0
    for line in archive1:
        soma += 1

print(Fore.RESET + f'{soma}')

"""








