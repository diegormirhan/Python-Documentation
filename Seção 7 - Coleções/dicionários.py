"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos por mapas.

Dicionários são coleções de tipo chave/valor.

Dicionários são representados por chaves {}.

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podem misturar tipos de dados;

print(type({}))

# Forma 1 (Mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'ue': 'União Europeia'}

print(paises)
print(type(paises))

# Forma 2 (Menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', ue='União Europeia')

print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
# print(paises['ru'])

# OBS: Caso tentarmos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError

# Forma 2 - Acessando via get - Recomendada
print(paises.get('br'))
print(paises.get('ru'))

# Caso o get não encontre o objeto com a chave informada será retornado valor None e não será gerado o KeyError

pais = paises.get('ue')

if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')


# Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada
pais = paises.get('ue', 'Não encontrado')

print(f'Encontrei o país {pais}')

# Podemos verificar se determinada chave se encontra em um dicionário
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'us' in paises:
    russia = paises['ru']

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla e dicionário, como chaves
# de dicionários.

# Tuplas por exemplo são bastante interessantes de serem utilizadas como chave de dicionários, pois as mesmas
# são imutáveis

localidades = {
    (23.4444, 54.5765): 'Escritório em São Paulo',
    (57.7453, 93.2495): 'Escritório em Tókio',
    (93.0883, 11.5011): 'Escritório em Nova York'
}

print(localidades)
print(type(localidades))

# Adicionar elementos em im dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

# Forma 1 - Mais comum

receita['abr'] = 350

print(receita)

# Forma 2 - Menos comum

novo_dado = {'mai': 500}

receita.update(novo_dado)  # receita.update({'mai': 500})

print(receita)

# Atualizando dados em um dicionário

# Forma 1

receita['mai'] = 550

print(receita)

# Forma 2

receita.update({'mai': 600})

print(receita)

# Conclusão 1: A forma  de adicionar novos elementos ou atualizar dados em dicionários é a mesma.
# Conclusão 2: Em dicionários, NÃO podemos ter chaves repetidas.


# Remover os dados de um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)

# Forma 1 - Mais comum

ret = receita.pop('mar')
print(ret)

print(receita)

# OBS 1: Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemnto, um KeyError será retornado.
# OBS 2: Ao removermos um objeto, o valor desse objeto é sempre retornado.

# Forma 2

del receita['fev']
print(receita)

# Se a chave não existir, será gerado um KeyError
# OBS: Neste caso o valor removido não é retornado.

# Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras na qual adicionamos produtos.

Carrinho de compras:
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    Produto 2:
        - nome;
        - quantidade;
        - preço;


# 1 - Poderíamos utilizar uma lista para isso? Sim

carrinho = []

produto1 = ['Playtation 4', 1, 4000.00]
produto2 = ['GTA V', 1, 190.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teríamos que saber qual é o índice de cada informação no produto.

# 2 - Poderíamos utilizar uma Tupla para isso? Sim

produto1 = ('Playstation 4', 1, 4000.00)
produto2 = ('GTA V', 1, 190.00)

carrinho = (produto1 + produto2)

print(carrinho)

# Teríamos que saber qual é o índice de cada informação no produto.

# 3 - Poderíamos utilizar um dicionário para isso? Sim

carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preço': 4000.00}
produto2 = {'nome': 'GTA V', 'quantidade': 1, 'preço': 190.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
# Podemos ter a certeza sobre cada informação

# Métodos de dicionários

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Limpar o dicionário (Zerar dados)

d.clear()

print(d)

# Copiando um dicionário para o outro

# Forma 1 - Deep Copy

novo = d.copy()
print(novo)

novo['d'] = 4
print(d)
print(novo)

# Forma 2 - Shallow Copy

novo = d
print(novo)

novo['d'] = 4

print(d)
print(novo)

# Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O método fromkeys recebe dois parâmetros: um iterável e um valor.
# Ele vai gerar para cada valor do iterável um chave e irá substituir a esta chave o valor informado.

# não reporduziu com todas as letras, pois elas se repetem e nos dicionários não é permitida a repetição
veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)
"""
