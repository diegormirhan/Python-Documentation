"""
Listas

Listas em Python funcional como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem DINÂMICO
e também de podermos colocar QUALQUER tipo de dado.

Linguagem C/java: Arrays
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array será SEMPRE do tipo
    inteiro e poderá ter SEMPRE no máximo 5 valores.

Já em Python:

- Dinâmico: Não possui tamanho fixo: Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: não possuem tipo de dado fixo: Ou seja, podemos colocar qualquer tipo de dado;

As listas em python são representados por colchetes: []
"""

lista1 = [1, 99, 23, 5, 76, 26, 64, 87, 16, 73, 32, 2, 7, 8, 1, 54]

lista2 = ['D', 'i', 'e', 'g', 'o', ' ', 'M', 'i', 'r', 'h', 'a', 'n']

lista3 = []

lista4 = list(range(11))

lista5 = list('Diego Mirhan')


"""
# Podemos facilmente checar se determinado valor está contido na lista
num = 7
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')


# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

lista2.sort()
print(lista2)


# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('i'))

# Para adicionar elementos em listas, utilizamos a função append

print(lista1)
lista1.append(42)
print(lista1)

# OBS: Com append, só conseguimos adicionar 1 elemento por vez
# lista1.append(12, 34, 56)   # Erro

lista1.append([32, 43, 36]) # Coloca a lista como elemento único
print(lista1)

if [32, 43, 36] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67]) # Coloca cada elemento da lista como valor adicional à lista
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice
# Isso não substitui o valor inicial. O mesmo será deslocado para direita da lista.
lista1.insert(2, 'novo valor')
print(lista1)

# Podemos facilmente juntar duas listas

# lista1 = lista1 + lista2
lista1.extend(lista2)
print(lista1)

# Podemos facilmente inverter uma lista

# Forma 1
lista1.reverse()
lista2.reverse()

print(lista1)
print(lista2)

# Forma 2
print(lista1[::-1])
print(lista2[::-1])

# Copiar uma lista
lista6 = lista2.copy()
print(lista6)

# Podemos contar quantos elementos existem dentro de uma lista
print(len(lista1))

# Podemos remover facilmente o último elemento de uma lista
# O pop não só remove o último elemnto mas também o retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemnto pelo índice
# OBS: Os elemntos à direita deste índice serão deslocados pela direita.
# OBS: Se não houver elemento no índice imformado, teremos o erro IndexError.

lista5.pop(2)
print(lista5)

# Podemos remover todos os elemntos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos facilmente converter uma string para uma lista

# Exemplo 1

curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

# OBS: Por Padrão, o split separa os elementos da lista pelo espaço entre elas.

# Exemplo 2
curso = 'Programação.Em.Python:.Essencial'
print(curso)
curso = curso.split('.')
print(curso)

# Convertando uma lista em uma string

lista6 = ['Programação', 'em', 'Python', 'Essencial']
print(lista6)

# Abaixo estamos falando: Pega a lista 6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

# Abaixo estamos falando: Pega a lista 6, coloca espaço entre cada elemento e transforma em uma string
curso = '$'.join(lista6)
print(curso)

# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados

lista6 = [1, 2.23, True, 'Diego', 'f', [1, 2, 4], 32432432]
print(lista6)
print(type(lista6))

# Iterando sobre listas

# Exemplo 1 - Usando For
soma = ''
for elemento in lista2:
    print(elemento)
    soma = soma + elemento
print(f'\n{soma}')

# Exemplo 2 - Utilizando While

carrinho = []
produto = ''
while produto != 'sair':
    produto = input('Adicione um produto na lista ou digite "sair" para sair: ')
    if produto != 'sair':
        carrinho.append(produto)

print('')
print(carrinho)
print('')

for produto in carrinho:
    print(produto)

# Utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elemntos de forma indexada


cores = ['verde', 'amarelo', 'azul', 'branco']


#           0        1         2        3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0])     # verde
print(cores[1])     # amarelo
print(cores[2])     # azul
print(cores[3])     # branco

# Fazer acesso aos elementos de forma indexada inversa
# Para entender melhor o índice negativo, pense na lista como um círculo,
# onde o final de um elemento está ligado ao ínicio da lista

print(cores[-1])    # branco
print(cores[-2])    # azul
print(cores[-3])    # amarelo
print(cores[-4])    # verde
# print(cores[-5])    # Erro, pois não existe índice -5

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Gerar índice em um For
for indice, cor in enumerate(cores):
    print(indice, cor)
    
# Listas aceitam números repetidos
lista = []
lista.append(24)
lista.append(36)
lista.append(24)
lista.append(36)
print(lista)

# Outros métodos não tão importantes mas que são úteis

# Encontrar o índice de um elemento na lista

numeros = [5, 1, 2, 5, 10, 8, 6]

# Em qual índice da lista está o valor 6?
print(numeros.index(6))

# Em qual índice da lista está o valor 10?
print(numeros.index(10))

# print(numeros.index(19) # Gera ValueError

# OBS: Caso não tenha esse elemento na lista, será apresentado o erro ValueError

# OBS: Retorna o índice do premeiro elemento encontrado
print(numeros.index(5))

# Podemos fazer uma busca dentro de um range, ou seja, qual indice começa a buscar
print(numeros.index(5, 1))  # Buscando a partir do índice 1
print(numeros.index(5, 2))  # Buscando a partir do índice 2
print(numeros.index(5, 3))  # Buscando a partir do índice 3
# print(numeros.index(5, 4))  # Buscando a partir do índice 4
# Caso não tenha esse elemento na lista, será apresentado o ValueError

# Podemos fazer a busca dentro do range, início/fim
print(numeros.index(8, 3, 6))   # Buscar o índice do valor 8, entre os índices 3 a 6

# Revisão de slicing

# lista[início:fim:passo]
# range[início:fim:passo]

# Trabalhando com slice de lista com o parâmetro 'início'

lista = [1, 2, 3, 4]

print(lista[1:])    # Início no índice 1 e pegando todos os elementos restantes

# Trabalhando com slice de lista com o parâmetro 'fim'

print(lista[:2])    # Começa em 0, pega até o índice 2 - 1

print(lista[:4])    # Começa em 0, pega até o índice 4 - 1

print(lista[1:3])   # Começa em 1, pega até o índice 3 - 1


# Trabalhando com Slice de lista com o parâmetro 'passo'

print(lista[1::2])  # Começa em 1, vai até o final, de 2 em 2

print(lista[::2])   # Começa em 0, vai até o final, de 2 em 2

# Invertendo os valores em uma lista

nome = ['Diego', 'Mirhan']

nome[0], nome[1] = nome[1], nome[0]

print(nome)

nome = ['Diego', 'Mirhan']

nome.reverse()
print(nome)


# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho

# * Se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(sum(lista))   # Soma
print(min(lista))   # Mínimo Valor
print(max(lista))   # Máximo Valor
print(len(lista))   # Tamanho da Lista

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tuple))

# Desempacatamento de listas

lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# Se tivermos um número diferente de elemntos na lista ou variáveis para receber os dados, teremos ValueError

# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1 - Deep Copy

lista = [1, 2, 3]
print(lista)

nova = lista.copy()

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que ao utilizarmos lista.copy() copiamos os dados da lsita para uma nova lista, mas elas
# Ficaram totalmente independentes, ou seja, modificando uma lista, não afeta a outra. Isso em Python
# é chamado de Deep Copy (cópia profunda)

# Forma 2 - Shallow Copy

lista = [1, 2, 3]
print(lista)

nova = lista    # cópia

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas
# após realizar a modificação em uma das listas, essa modificação se refletiu em ambas as listas.
# Isso em Python é chamado de Shallow Copy.

"""


