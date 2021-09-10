"""
Erros mais comuns

ATENÇÃO: É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução
do nosso código

Os erros mais comuns:

1 - SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, você escreveu algo que o Python
não reconhece como parte da linguagem.

Exemplos SysntaxError
a)
    def funcao:
        print('Diego')

b)
    def = 1

c)
    return


2 - NameError -> Ocorre quando uma variável ou função não foi definida.

Exemplos NameError

a)
    print(geek)

b)
    geek()


3 - TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado.

Exemplos TypeError

a)
    print(len(5))

b)
    print('Diego' + [])


4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado
utilizando um índice inválido.

Exemplos IndexError

a)
    lista = ['Diego']
    print(lista[2])

b)
    lista = ['Diego']
    print(lista[0][10])


5 - ValueError -> Ocorre quando uma função/operação built-in(integrada) recebeum argumento com tipo correto
mas valor inapropriado

Exemplos ValueError

print(int('Geek'))


6 - KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe.

Exemplos KeyError

a)
    dic = {'python': 'Diego'}
    print(dic['Geek'])



7 - AttributeError -> Ocorre quando uma variável não tem um atributo/função.

Exemplos AttributeError

a)
    tupla = (32, 1, 7, 23)
    print(tupla.sort())


8 - IndentationError -> Ocorre quando não respeitamos a indentação do Python (4 espaços)

Exemplos IndentationError

a)
    def nova():
    print('Diego')

b)
    for i in range(10):
    i + 1

OBS: Exceptions e Erros são sinônimos na programação.

OBS: Importante ler e prestar atenção na saída de erro
"""







