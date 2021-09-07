"""
Leitura de arquivos

Para o conteúdo de um arquivo em Python, utilizamos a função integrada open(),
que literalmente siginifica 'abrir'.

open() -> Na forma mais simples de utilização nós passamos apenas um parâmetro
de entrada, que neste caso é o caminho para o arquivo a ser lido. Essa funçõo retorna
um _io.TextIOWrapper e é com ele que trabalhamos então.

https://docs.python.org/3/library/functions.html#open

# OBS: Por padrão, a função open() abre o arquivo para leitura. Este arquivo
deve existir, ou então teremos o erro FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='utf-8'>

mode r -> Modo de leitura. r -> read() -> 'ler'
"""
# Exemplo

arquivo = open('texto.txt', encoding='utf-8')

# print(arquivo)

# print(type(arquivo))

# Para ler o conteúdo do arquivo, após sua leitura, devemos utilizar a função read()

ret = arquivo.read()

print(type(ret))

print(ret)

# print(arquivo.read())

# OBS: O python utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor,
# funciona como o cursor quando estamos escrevendo.

# print(arquivo.read())

# OBS: A função read() lê todo o conteúdo do arquivo.
