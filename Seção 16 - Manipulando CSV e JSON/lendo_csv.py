"""
Lendo arquivos CSV

CSV - Comma Separeted Values - Valores Separados por Vírgula

# Separador por Vírgula

1, 2, 3, 4, 5, 6

'diego', 'rodrilla', 'mirhan'

# Separador por ponto e vírgula

1; 2; 3; 4; 5; 6;

'diego'; 'rodrilla'; 'mirhan';

# Separador por espaço

1 2 3 4 5 6

'diego' 'rodrilla' 'mirhan'

https://dados.gov.br/dataset

# Possível de se trabalhar, mas não é o ideal (trbalhoso)
with open('lutadores.csv', encoding='UTF-8') as arquivo:
    dados = arquivo.read()
    print(type(dados))
    dados = dados.split(',')[2:]
    print(dados)

A linguagem python possui duas formas diferentes para ler dados em arquivos CSV:
    - reader -> permite que iteremos sobre as linhas do arquivo csv como listas;
    - DictReader -> Permite que iteremos sobre as linhas do arquivo csv como OrderedDict;

# Reader
from csv import reader

with open('lutadores.csv', encoding='UTF-8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)  # Pular o cabeçalho
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu no(a) {linha[1]} e mede {linha[2]} centímetros')


#DictReader

from csv import DictReader

with open('lutadores.csv', encoding='UTF-8') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha é uma OrderedDict
        print(f'{linha["Nome"]} nasceu no(a) {linha["País"]} e mede {linha["Altura (em cm)"]} centímetros')

"""
#DictReader

from csv import DictReader

with open('lutadores.csv', encoding='UTF-8') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    for linha in leitor_csv:
        # Cada linha é uma OrderedDict
        print(f'{linha["Nome"]} nasceu no(a) {linha["País"]} e mede {linha["Altura (em cm)"]} centímetros')


