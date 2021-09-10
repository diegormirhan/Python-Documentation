"""
Seek e Cursors

arquivo = open('texto.txt', encoding='utf-8')

print(arquivo.read())

# seek() -> A função seek() é utilizada para a movimentação do cursor pelo arquivo. Ela recebe
# um parâmetro que indica onde queremos colocar o cursor.

# Movimentando o cursor pelo arquivo com a função seek() -> procurar
arquivo.seek(0)

print(arquivo.read())

arquivo.seek(24)

print(arquivo.read())




# readline() -> Função que lê o arquivo linha a linha (readline -> lê linha)

ret = arquivo.readline()

print(type(ret))

print(ret)

print(ret.split(' '))


# readlines()

linhas = arquivo.readlines()

print(linhas)
print(len(linhas))


OBS: Quando abrimos um arquivo com a função open(), é criada uma conexão entre o arquivo
no disco do computador e o nosso programa. Essa conexão é chamada de streaming. Ao finalizar
os trabalhos com o arquivo, devemos fechar essa conexão. Para isso utilizamos a função close()

Passos para trabalhar com um arquivo:

1 - Abrir o arquivo;

2 - Trabalhar o arquivo;

3 - Fechar o arquivo;



# 1 - Abrir o arquivo;
arquivo = open('texto.txt', encoding='utf-8')

# 2 - Trabalhar o arquivo;
print(arquivo.read())
print(arquivo.closed)   # False - Verifica se o arquivo está aberto ou fechado

# 3 - Fechar o arquivo;
arquivo.close()
print(arquivo.closed)   # True - Verifica se o arquivo está aberto ou fechado


print(arquivo.read())
# OBS: Se tentarmos manipular o arquivo após seu fechamento, teremos um ValueError


"""

arquivo = open('texto.txt', encoding='utf-8')


# Coma função read() podemos limitar a quantidade de caracteres a serem lidos no arquivo
print(arquivo.read(50))
