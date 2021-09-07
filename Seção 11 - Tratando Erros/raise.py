"""
Levantando os próprios erros com raise

raise -> Lança excessões

OBS: O raise não é uma função. É uma palavra reservada, assim como def ou qualquer outra em Python.

Para simplificar, pense no raise como sendo útil para que possamos criar nossas própriias excessões e mensagens
de erro.

A forma geral de utilização é:

raise TipoDeErro('Mensagem de erro')

# Exemplo real


def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('O texto precisa ser uma String')
    if type(cor) is not str:
        raise TypeError('A cor precisa ser uma String')
    return f'O texto {texto} será impresso na cor {cor}.'


print(colore('Geek', 'Azul'))


# Exemplo refatorado


def colore(texto, cor):
    cores = ('azul', 'verde', 'amarelo', 'vermelho')
    if type(texto) is not str:
        raise TypeError('O texto precisa ser uma String')
    if type(cor) is not str:
        raise TypeError('A cor precisa ser uma String')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    return f'O texto {texto} será impresso na cor {cor}.'


print(colore('Geek', 'preto'))

OBS: O raise, assim como o return,finaliza a função. Ou seja, nada após o raise é executado.
"""
