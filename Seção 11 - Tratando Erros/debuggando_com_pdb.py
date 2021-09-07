"""
Debuggando com PDB

PDB -> Python Debugger

Bug -> Inseto


# OBS: A utilização do print() para debugar código é uma prática ruim.

def dividir(a, b):
    print(f'a={a}, b={b}')
    try:
        return int(a)/int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Valor incorreto {err}'


print(dividir(4, 7))




# Existem formas mais profissionais de se fazer esse 'debug', utilizando o debugger
# Em Python, podemos fazer isso em diferentes IDEs, como o Pycharm  ou utilizando
# o PDB - Python Debugger

# Exemplo PyCharm


def dividir(a, b):
    try:
        return int(a)/int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Valor incorreto {err}'


print(dividir(543, 7))




# Exemplo com PDB - Python Debugger - Exemplo 1

# Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb e então utilizar a função set_trace()

# Comandos básicos do PDB
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)

import pdb

nome = 'Diego'
sobrenome = 'Mirhan'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação Python'
final = nome_completo + ' faz o curso ' + curso
print(final)


# Exemplo 2

nome = 'Diego'
sobrenome = 'Mirhan'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação Python'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Por que utilizar esse formato?
# O debug é utilizado durante o desenvolvimento. Costumamos realizar todos os imports da bibliotecas
# no início do arquivo. Por isso, ao invés de colocarmos o import do pdb mo início do arquivo,
# nós colocamos somente onde vamos debuggar, e ao finalizar já fazemos a remoção.




# Exemplo 3

# A partir do Python 3.7, não é mais necessário importar a biblioteca pdb, pois o comando de debug foi
# incorporado como função built-in (integrada) chamada breakpoint()
nome = 'Diego'
sobrenome = 'Mirhan'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação Python'
final = nome_completo + ' faz o curso ' + curso
print(final)



# OBS: Cuidado com conflitos entre nomes de variáveis e os comandos do pdb


def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c


print(soma(1, 4, 5, 7))

# Como os nomes das variáveis são os mesmos do comando do pdb, devemos utilizar o comando p para imprimir
# as variáveis. Ou seja: p nome_da_variavel

# Nada de colocar nomes não representativos em variáveis. Sempre optar por nomes significativos.
"""


