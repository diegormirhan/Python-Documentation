"""
Asseritions (Afirmações/Checamos/Questionamentos)

Em Python utilizamos a palavra reservada 'assert' para realizar simples
afirmações utilizadas em testes.

Utilizamos o 'assert' em uma expressão que queremos checar se é válida ou não.
Se a expressão for verdadeira, retorna None e caso seja falsa levanta um erro
do tipo AssertionError.

OBS: Nós podemos especificar, opcionalmente, um segundo argumento ou mesmo uma mensagem
de erro personalizada.

OBS: A palavra 'assert' pode ser utilizada em qualquer função ou código nosso... não precisa ser
exclusivamente nos testes.

ALERTA: Cuidado ao utilizar 'assert'

Se um programa Python for executado com o parâmetro -O, nenhum assertion
será validado. Ou seja, todas as suas validações já eram.
"""


def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos números precisam ser positivos!'
    return a + b


# print(soma_numeros_positivos(-3, 5))


def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doce',
        'batata frita',
        'cachorro quente'
        'hambúrguer',
        'refrigerante'
    ], 'A comida precisa ser fast food'
    return f'Eu estou comendo {comida}!'


print(comer_fast_food('pizzas'))
