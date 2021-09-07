"""
Recebendo dados do usuário

imput() -> todo dado recebido via imput é do tipo string

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'Diego'
- Aspas duplas -> "Diego"
- Aspas simples triplas -> '''Diego'''
"""
# Aspas duplas triplas -> """Diego"""

# Entrada de dados
# print('Qual seu nome?')
# nome = input()  # Imput -> Entrada

nome = input('Qual seu nome? ')

# Exemplo de print 'antigo'
# print('Seja Bem Vindo(a) %s' % nome)

# Exemplo de print 'moderno'
# print('Seja Bem Vindo(a) {0}'.format(nome))

# Exemplo de print 'atual'
print(f'Seja Bem Vindo(a) {nome}')

# print('Qual sua idade?')
# idade = input()

idade = int(input('Qual sua idade? '))

# Processamento

# Saída de dados
# Exemplo de print 'antigo'
# print('O(a) %s tem %s anos!' % (nome, idade))

# Exemplo de print 'moderno'
# print('O(a) {0} tem {1} anos!'.format(nome, idade))

# Exemplo de print 'atual'
print(f'O(a) {nome} tem {idade} anos!')

"""
int(idade) -> cast

Cast é a 'conversão' de um tipo de dado para outro.
"""

print(f'O(a) {nome} nasceu em {2020 - idade}')

