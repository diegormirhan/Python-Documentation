"""
Modos de abertura de arquivos

r -> Abre para leitura - padrão
w -> Abre para escrita - sobrescreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo não existir. Caso o arquivo exista, gera FileExistsError
a -> Abre para escrita, adicionando conteúdo ao final do arquivo
+ -> Abra para o modo de atualização: Leitura e escrita
OBS: Abrindo no mado 'a' -> append, se o arquivo não existir, será criado. Caso exista, o novo conteúdo
será adicionado ao final do arquivo SEMPRE. Com o modo 'a', não controlamos o cursor
https://docs.python.org/3/library/functions.html#open

# Exemplo X
try:
    with open('texto.txt', 'x') as arquivo:
        arquivo.write('Teste de conteúdo \n')
except FileExistsError:
    print('arquivo já existe')

# Exemplo A
with open('frutas.txt', encoding='utf-8', mode='a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break


# Exemplo R+
with open('texto.txt', encoding='utf-8', mode='r+') as arquivo:
    arquivo.write('Adicionando \n')
    arquivo.seek(14)
    arquivo.write('Novo comentário \n')
    arquivo.seek(42)
    arquivo.write('Final \n')

"""

