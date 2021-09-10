"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência à Teoria dos Conjuntos da Matemática.

- Aqui no Python, os conjuntos são chamados de Sets.

Dito isso, da mesma forma que na matemática:

- Sets (Conjuntos) não possuem valores duplicados;
- Sets (Conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar
com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos (Sets) e Mapas (Dicionários) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;


# Definindo um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 6, 3, 5, 6})    # Repare que temos valores repetidos.
print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo
# será ignorado sem gerar erro e não fará parte do conjunto.

# Forma 2 - Mais comum

s = {1, 2, 3, 4, 5, 6, 5, 6, 1}
print(s)
print(type(s))

# Podemos verificar se determinado elemento está contido no conjunto

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

# Importante lembrar que, além de não termos valores duplicados, não temos ordem

# Listas aceitam valores duplicados, então temos 12 elementos
lista = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 80, 90]
print(f'lista {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados, então temos 12 elementos
tupla = (1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 80, 90)
print(f'tupla {tupla} com {len(tupla)} elementos')

# Dicionários não aceitam chaves duplicadas, então temos 10 elementos
dicionario = {}.fromkeys([1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 80, 90], 'dict')
print(f'diconário {dicionario} com {len(dicionario)} elementos')

# Conjuntos não aceitam valores duplicados, então temos 10 elementos
conjunto = {1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 80, 90}  # Tem ordenação própria
print(f'conjunto {conjunto} com {len(conjunto)} elementos')


# Usos interessantes com sets

# Imagine que fizemos um formulário de cadastro de visitantes de uma feira ou um museu e os visitantes
# Informam manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista python, já que em uma lista podemos adicionar novos elementos
# e ter repetição

cidades = ['São Paulo', 'Rio de Janeiro', 'Paraná', 'Campo Grande', 'São Paulo', 'Rio de Janeiro']

print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos.

# O que você faria? Faria um lop de lista....?

# Podemos utilizar o set para isso:

print(len(set(cidades)))

# Adicionando elementos em um conjunto
s = {1, 2, 3}
print(s)

s.add(4)
s.add(4)    # Duplicidade não gera erro, Simplesmente é ignorado e não é adicionado
print(s)

# Removendo elementos em um conjunto
s = {1, 2, 3}
print(s)

# Forma 1

s.remove(3) # NÃO é índice! Informamos o valor a ser removido.
print(s)

# OBS: Caso o valor não seja encontrado será gerado o KeyError, Nenhum valor é retornado.

# Forma 2

s.discard(2)
print(s)

# OBS: Se o valor não for encontrado, nenhum erro é gerado.

# Copiando um conjunto para o outro...
s = {1, 2, 3}
print(s)

# Forma 1 - Deep Copy

novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

# Forma 2 - Shallow Copy

novo = s

novo.add(4)

print(novo)
print(s)

# Podemos remover todos os itens de um conjunto

s.clear()
print(s)

# Métodos Matemáticos de conjuntos

# Imagine que temos dois conjuntos: Um contendo estudantes do curso Python e um
# Contendo estudantes do curso Java.

estudantes_python = {'Diego', 'Pedro', 'Julia', 'Marina', 'Ana', 'Paulo', 'Sophia'}
estudantes_java = {'Rafael', 'Jodana', 'Olavo', 'Diego', 'Yasmim', 'Pedro'}

# Veja que alguns alunos que estudam Python também estudam Java.

# Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - Utilizando union

unicos1 = estudantes_python.union(estudantes_java)
# {'Marina', 'Sophia', 'Olavo', 'Rafael', 'Diego', 'Paulo', 'Yasmim', 'Jodana', 'Julia', 'Pedro', 'Ana'}
# unicos1 = estudantes_java.union(estudantes_python)
# {'Pedro', 'Diego', 'Rafael', 'Julia', 'Paulo', 'Ana', 'Sophia', 'Olavo', 'Jodana', 'Marina', 'Yasmim'}

print(unicos1)

# Forma 2 - Utilizando o caractere pipe |
unicos2 = estudantes_python | estudantes_java

print(unicos2)

# Gerar um conjunto de estudantes que estão em ambos os cursos


# Forma 1 - Utilizando Intersection

ambos1 = estudantes_java.intersection(estudantes_python)
print(ambos1)

# Forma 2 -Utilizando o &

ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Gerar um conjunto de estudantes que não estão no outro curso

so_python = estudantes_python.difference(estudantes_java)
print(so_python)
so_java = estudantes_java.difference(estudantes_python)
print(so_java)

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho

# * Se os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6, 7}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))

"""



