"""
Sistema de arquivos - Manipulação

# Descobrindo se um arquivo ou diretório existe

# Arquivo
print(os.path.exists('arquivo.txt'))  # False
print(os.path.exists('frutas.txt'))   # True



# Diretório

# Paths relativos
print(os.path.exists('geek'))   # True
print(os.path.exists('geek/university'))   # True
print(os.path.exists('outro'))   # False

# Paths absolutos
print(os.path.exists('C:\\Users\\diego\\PycharmProjects\\CursoPython'))  # True
print(os.path.exists('C:\\Users\\diego\\PycharmProjects\\CursoPython\\geek'))   # True
print(os.path.exists('C:\\Users\\diego\\PycharmProjects\\CursoPython\\geek\\first.txt'))   # False



# Forma 1
open('arquivo-teste1.txt', 'w').close()

# Forma 2
open('arquivo-teste2.txt', 'a').close()

# Forma 3
with open('arquivo-teste.txt', 'w') as arquivo:
    pass


# Criando arquivos

os.mknod('arquivo-teste4.txt')
os.mknod('\\CursoPython\\geek\\arquivo-teste.txt')

# OBS: Se você estiver utilizando o MAC OS, pode haver um erro de PermissionError

# Criando um arquivo via mknod(), se o arquivo já existir teremos o erro FileExistsError


# Criando diretórios - unícos (um a um)
os.mkdir('templates')

# OBS: A função mkdir() cria um diretório se este não existir. Caso exista, teremos FileExistsError

os.mkdir('\\CursoPython\\geek\\templates')


# Criando multi-diretórios (árvore de diretórios)
os.makedirs('templates\\geek\\university')

# OBS: Se já existir, teremos um FileExistsError

os.makedirs('templates\\geek\\university\\templates2', exist_ok=True)


# Renomear arquivos e diretórios

# Arquivos
os.rename('frutas.txt', 'cesta.txt')



# Atenção! Tome cuidado com o comandos de remoção. Ao deletarmos um arquivo oudiretório, os mesmos
# não vão para a lixeira. Eles somem.

# Removendo arquivos
os.remove('arquivo-teste.txt')

# OBS: Se você estiver no Windows e o arquivo que você for deletar estiver em uso, você terá um erro

# OBS: Caso o arquivo não exista, teremos o FileNotFoundError

# OBS: Se você informar um diretório ao invés de um arquivo, teremos um IsADirectoryError


# Removendo diretórios vazios

os.rmdir('teste123')

# OBS: Se o diretório tiver qualquer conteúdo, teremos um OSError

# OBS: Se o diretório não existir teremos um FileNotFoundError


v# Removendo uma árvore de arquivos
for arquivo in os.scandir('university'):
    if arquivo is_file():
        os.remove(arquivo.path)



# ATENÇÃO: Ao remover arquivos e diretórios com Python, eles não vão para  lixeira. Eles são deletados permanentemente

# Importando a biblioteca send2trash

from send2trash import send2trash

send2trash('arquivo-teste1.txt')  # Vai para a lixeira. Pode ser restaurado.

# OBS: Se o arquivo não existir, teremos OSError




# Criando um diretório temporário

import os
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Diego Mirhan\n')
    input()

# Estamos criando um diretório temporário, abrindo o mesmo e dentro dele, criando
# um arquivo para escrevermos um texto. No final, usamos um input() só para mantermos
# os arquivos temporários 'vivos' dentro dos blocos with.



# Criando um arquivo temporário

import os
import tempfile

with tempfile.TemporaryFile() as tmp1:
    print(f'{tmp1}')
    tmp1.write(b'Diego Mirhan')
    tmp1.seek(0)
    print(tmp1.read())


# OBS: Em arquivos temporários só conseguimos escrever bits. POr isso utilizamos 'b'



# Sem o bloco with

arquivo = tempfile.TemporaryFile()
arquivo.write(b'Diego Mirhan')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()




import os
import tempfile

arquivo1 = tempfile.NamedTemporaryFile()
arquivo1.write(b'Diego Mirhan')
arquivo1.seek(0)
print(arquivo1.name)
print(arquivo1.read())
input()
arquivo1.close()

"""

