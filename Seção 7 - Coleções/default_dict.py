"""
Módulo Collectios - Default Dict

https://docs.python.org/3/library/collections.html#collections.defaultdict

# Recap Dicionários

dicionario = {'nome': 'Diego Mirhan'}

print(dicionario)

print(dicionario['nome'])

print(dicionario['curso'])  # ??? KeyError

Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default,
podendo utilizar uma lambda para isso. Esse valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será
criada e o valor default será atribuido

OBS: Lambdas são funções sem nome, que podem ou não receber parâmetros de entrada e retornar valores.

# Fazendo Import

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['nome'] = 'Diego Mirhan'

print(dicionario)

print(dicionario['curso'])  # KeyError no dicionário comum, mas aqui não.

print(dicionario)

"""




