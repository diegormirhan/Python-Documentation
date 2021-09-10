"""
Definindo Funções

- Funções são pequenas partes do código que realizam tarefas específicicas;
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito úteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela,
é bom fazer uma verificação para que a função seja simplifacada.

Já utilizamos várias funções desde que iniciamos este curso:
- print()
- len()
- max()
- min()
- count()
- e muitas outras:
"""

# Exemplo de utilização das funções:

# cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (Built-in) do Python print()

# print(cores)

# curso = 'Diego Mirhan'

# print(curso)

# cores.append('roxo')
# print(cores)

# curso.append('mais dados...')  # AtributeError
# print(curso)

# cores.clear()
# print(cores)

# print(help(print))

# DRY - Don't repeat youself - Não repita a si mesmo / Não repita seu código.

# Mas então, como definir funções?

"""
Em Python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

Onde:

nome_da_funcao -> SEMPRE, com letras minúsculas, e se for composto, separado por underline (Snake Case);
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não;
bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde o processaamento da função acontece.
Nesse bloco, pode ter ou não retorno da função.

OBS: Veja que para definir uma função, utilizamos a palavra 'def' informando ao Python
que estamos definindo uma função. Também abrimos o bloco do código com o já conhecido dois pontos : que é
utilizado em Python para definir os blocos.
"""


# Definindo a primeira função

def diz_oi():
    print('oi')


"""
OBS:

1 - Veja que, dentro das nossas funções podemos utiliza putras funções;
2 - Veja que nossa função só executa 1 tarefa, ou seja, a única coisa que ela faz é dizer oi;
3 - Veja que esta função não recebe parâmetro de entrada;
4 - Veja que esta função não retorna nada;
 
"""

# Utilizando funções

# Chamada em execução
# diz_oi()

"""
ATENÇÃO:

Nunca esqueça de utilizar os parênteses ao executar uma função.

Exemplo:

# Errado!
diz_oi

# Certo
diz_oi()

# Errado!
diz_oi ()
"""

# Exemplo 2


def cantar_parabens():
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante')




# for s in range(5):
#     cantar_parabens()

# Em python, podemos inclusive criar variáveis do tipo de uma função e exucatar essa função através da variável

canta = cantar_parabens

canta()



def quadrado_de_7():
    return 7 * 7


print(quadrado_de_7() + 1)
