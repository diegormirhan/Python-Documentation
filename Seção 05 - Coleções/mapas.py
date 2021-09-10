"""
Mapas -> Conhecidos em python como dicionários

Dicionários em Python são representados por chaves {}


receita = {'Jan': 100, 'Fev': 250, 'Mar': 400}


# Iterar sobre dicionários
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')

# Acessando as chaves
print(receita.keys())

for chave in receita.keys():    # Modo Pythonico
    print(receita[chave])

print(receita)

# Acessando os valores

print(receita.values())

for valor in receita.values():
    print(valor)

# Desempacotamento de dicioários

print(receita.items())

for chave, valor in receita.items():
    print(f'chave = {chave} e valor = {valor}')

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho

# * Se os valores forem todos inteiros  ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))


"""
