"""
Try / Except / Else / Finally

Dica de quando e onde tratar o código;

TODA ENTRADA DEVE SER TRATADA

OBS: A função do USUÁRIO é destruir seu sistema.

# Else ->É executado somente se não houver erro

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')



# Finally

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')
finally:
    print('Executando o finally')


# OBS: O bloco finally é SEMPRE executado. Independente se houve exceção ou não.

# O finally, geralmente, é utilizado para fechar ou desalocar recursos.



# Exemplo mais complexo ERRADO


def dividir(a, b):
    return a/b


try:
    num1 = int(input('Digite o 1º Valor: '))
    num2 = int(input('Digite o 2º Valor: '))

except ValueError:
    print('O valor precisa ser numérico')
else:
    print(dividir(num1, num2))




# Exemplo mais complexo CORRETO
# OBS: Você é responsável pelas entradas das suas funções. Então trate-as!


def dividir(a, b):
    try:
        return int(a)/int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possível realizar uma divisão por zero'


num1 = input('Digite o 1º Valor: ')
num2 = input('Digite o 2º Valor: ')

print(dividir(num1, num2))



# Exemplo mais complexo - Genérico
# OBS: Você é responsável pelas entradas das suas funções. Então trate-as!


def dividir(a, b):
    try:
        return int(a)/int(b)
    except:
        return 'Valor incorreto'


num1 = input('Digite o 1º Valor: ')
num2 = input('Digite o 2º Valor: ')

print(dividir(num1, num2))




# Exemplo mais complexo - Semi Genérico
# OBS: Você é responsável pelas entradas das suas funções. Então trate-as!


def dividir(a, b):
    try:
        return int(a)/int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Valor incorreto {err}'


num1 = input('Digite o 1º Valor: ')
num2 = input('Digite o 2º Valor: ')

print(dividir(num1, num2))
"""
