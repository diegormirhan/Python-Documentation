"""
**kwqrgs

Poderíamos chamar este paramâmetro de **xix, mas por convernção chamamos de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla,
o **kwargs exige que utilizemos parâmetros nomeados, e transforma esses parâmetros extras em dicionários.


# Exemplo


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marcos='verde', giulia='roxo', ronaldo='azul', marina='rosa', anna='amarelo')

# Os parâmetros *args e **kwargs não são obrigatórios

cores_favoritas()

cores_favoritas(agatha='vermelho')


# Exemplo mais complexo


def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return "Você recebeu um comprimento Pythonico"
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek"
    return 'Não tenho certeza de quem você é...'


print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Olá'))
print(cumprimento_especial(diego='Mirhan'))
print(cumprimento_especial())


# Nas nossas funções, podemos ter(NESSA ORDEM):

- Parâmetros obrigatários;
- *args;
- Parâmetros default(não obrigatórios);
- **kwargs



def minha_funcao(nome, idade, *args, solteiro = True, **kwargs):
    print(f'{nome} tem {idade} anos!')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Namorando')
    print(kwargs)
    print()


minha_funcao('Diego', 16, 3, 4, 5, solteiro=False, ele='nada', ela='tudo')
minha_funcao('Diego', 17)
minha_funcao('Anna', 21, 6, 34, 87)
minha_funcao('Anna', 22, escola='ruim')
minha_funcao('Anna', 22, solteiro=False)


# Entenda porquê é importante manter a ordem dos parâmetros na declaração

# Função com a ordem correta dos parâmetros
# def mostra_info(a, b, *args, instrutor = 'Diego', **kwargs):
    # return [a, b, args, instrutor, kwargs]

# Função com a ordem incorreta dos parâmetros
def mostra_info(a, b,  instrutor = 'Diego', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]

a = 1
b = 2
args = 3
instrutor = 'Diego'
kwargs = {'Nome': 'Anna', 'idade': '21'}


print(mostra_info(1, 2, 3, Nome='Anna', idade='21'))


# Desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Diego', 'sobrenome': 'Mirhan'}

print(mostra_nomes(**nomes))



def soma_multiplos_numeros(a, b, c):
    print(a + b + c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario)

# OBS: Os nomes da chave em um dicionário devem ser os mesmos dos parâmetros da função

"""



