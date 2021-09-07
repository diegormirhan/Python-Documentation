"""
Bloco With

Passo para se trabalhar com arquivos

# 1 - Abrimos o arquivo
# 2 - Manipulamos o arquivo
# 3 – Fechamos o arquivo

O bloco With é utilizado para criar um contexto de trabalho onde os recursos
utilizados são fechados após o bloco with.

arquivo = open('texto.txt')
"""

# O bloco with - Forma Pythonica de manipular arquivos

with open('texto.txt', encoding='utf-8') as arquivo:
    print(arquivo.read())
    print(arquivo.closed)

# print(arquivo.read())
print(arquivo.closed)
