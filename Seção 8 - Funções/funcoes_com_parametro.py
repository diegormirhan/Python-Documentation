"""
Funções com parâmetro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:
    - Não possuem entrada;
    - Não possuem saída;
    - Possuem entrada mas não possuem saída;
    - Não possuem entrada mas possuem saída;
    - Possuem entrada e saída;

# Refatorando uma função


def quadrado(numero):
    # return numero * numero
    return numero ** 2


print(quadrado(2))
print(quadrado(3))
print(quadrado(4))
print(quadrado(5))

# print(quadrado())  # TypeError


# Refatorando a função


def cantar_parabens(aniversariante):
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o {aniversariante}')


cantar_parabens('Ronaldo')


def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(2, 4))
print(soma(6, 9))

print(multiplica(1, 12))
print(multiplica(4, 15))

print(outra(5, 1, 'Diego '))
print(outra(7, 9, 'Mirhan '))


# OBS: Se a gente informar um número errado de parâmetro e argumentos, teremos TypeError

# print(soma(2, 4, 6)) # TypeError - Passando argumentos a mais
# print(soma(4)) # TypeError - Passando argumentos a menos




# Nomeando Parâmetros


def nome_completo(nome, sobrenome):
    return f"Seu nome completo é {nome} {sobrenome}"


print(nome_completo("Diego", "Mirhan"))

# A diferença entre parâmetros e argumentos

# Parâmetros são variáveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função;

# A ordem dos parâmetros importa!

nome = 'Diego'
sobrenome = 'Mirhan'

print(nome_completo(sobrenome, nome))

# Argumentos nomeados (Keyword Arguments)

# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos
# utilizar qualquer ordem

print(nome_completo(nome='Diego', sobrenome='Mirhan'))
print(nome_completo(sobrenome='Mirhan', nome='Diego'))
print(nome_completo(nome=nome, sobrenome=sobrenome))


# Erro comum na utilização do return
"""


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total  # O return deve estar abaixo do for e não do if, se não o resultado derá errado


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print(soma_impares(lista))

    tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
    print(soma_impares(tupla))


