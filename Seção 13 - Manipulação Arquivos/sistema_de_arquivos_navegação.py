"""
Sistema de arquivos e navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar
e fazer uso do módulo "os"

os -> Operation System - Sistema Operacional


# getcwd() -> pega o current work directory - diretório de trabalho corrente
# Retorna o path (caminho) absoluto
print(os.getcwd())

# Para mudar o diretório, podemos utilizar o chdir()

os.chdir('..')

print(os.getcwd())


os.chdir('..')

print(os.getcwd())


os.chdir('..')

print(os.getcwd())


os.chdir('..')

print(os.getcwd())


# OBS para usuários Windows
# se você, infelizmente, estiver utilizando um computador com windows.
# terá que ter cuidado ao verificar diretórios.

print(os.path.isabs('C:\\Users\\diego'))


# Podemos identificar o sistema operacional com o módulo os
print(os.name)  # posix (Linux e Mac), nt (Windows)


# Podemos ter mais detalhes do sistema operacional
print(platform.uname())


import sys
print(sys.platform)



print(os.getcwd())  # C:\\Users\\diego\\PycharmProjects\\CursoPython

res = os.path.join(os.getcwd(), 'geek', 'university')

os.chdir(res)

print(os.getcwd())  # C:\\Users\\diego\\PycharmProjects\\CursoPython\\geek\\university

# Veja que o os.path.join() recebe dois parâmetros, sendo o primeiro o diretório atual e o segundo o
# diretório que será juntado ao atual.


"""
# Fazer import
import os

# Podemos listar os arquivos e diretórios com mais detalhes com scandir()


scanner = os.scandir()

arquivos = list(scanner)

# print(dir(arquivos[2]))

print(arquivos[2].inode())
print(arquivos[2].is_dir())  # É um diretório? False
print(arquivos[2].is_file())  # É um arquivo? true
print(arquivos[2].name)  # Nome do arquivo
print(arquivos[2].path)  # Caminho até o arquivo
print(arquivos[2].stat())  # Estatísticas

# OBS: Quando utilizamos afunção scandir(), nós precisamos fechá-la, assim quando abrimos um arquivo.

scanner.close()