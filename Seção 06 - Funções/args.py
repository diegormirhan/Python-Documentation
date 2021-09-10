"""
Entendendo o *args

- O args é um parãmetro, como outro qualquer. Isso significa que você poderá chamar de qualquer coisa,
desde que comece com asterísco.

Exemplo:

*xis

Mas por convenção, utilizamos *args para definí-lo

Mas o que é o *args?

O parâmetro *args é utilizado em uma função , coloca os valores extras informados como em uma tupla.
Então desde já lembre-se que tuplas são imutáveis



# Exemplos


def soma_todos_numeros(num1=1, num2=2, num3=3, num4=4):
    return num1 + num2 + num3 + num4


print(soma_todos_numeros(4, 6, 9))
print(soma_todos_numeros(4, 6))
print(soma_todos_numeros(4, 6, 9, 5))




# Entendendo o args


def soma_todos_elementos(nome, sobrenome, *args):
    return sum(args)


print(soma_todos_elementos('Diego', 'Mirhan'))
print(soma_todos_elementos('Diego', 'Mirhan', 1))
print(soma_todos_elementos('Diego', 'Mirhan', 2, 3))
print(soma_todos_elementos('Diego', 'Mirhan', 4, 5, 6))
print(soma_todos_elementos('Diego', 'Mirhan', 7, 8, 9, 2, 1))
print(soma_todos_elementos('Diego', 'Mirhan', 23.1, 78.2, 8.5))





# Outro exemplo de utilização do *args


def verifica_info(*args):
    if 'Diego' in args and 'Mirhan' in args:
        return 'Bem-Vindo Diego Mirhan'
    return 'Eu não tenho certeza de quem você é'


print(verifica_info())
print(verifica_info(1, 'Diego', True, 'Mirhan'))
print(verifica_info(23, 'Mirhan', 2.4))



def soma_todos_numeros(*args):
    return sum(args)


# print(soma_todos_numeros())
# print(soma_todos_numeros(3, 4, 5, 6))

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# Desempacotador

print(soma_todos_numeros(*numeros))


# OBS: o asterísco server para informarmos ao python que estamos
# passando como argumento uma coleção de dados. Desta forma, ele saberá
# que precisará antes desempacotar esses dados.


"""



