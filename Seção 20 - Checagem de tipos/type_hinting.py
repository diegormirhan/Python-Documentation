"""
Type Hinting

-> Com o type hinting, você poderá encontrar facilmente os erros antes de executar seu código.
-> Irá melhorar a documentação do seu código

"""

# Você pode definir o tipo do parâmetro na definição da função.
# Se a função tiver retorno, poderá ser colocado "-> 'tipo do parâmetro'"


def cumprimentar(nome: str) -> str:
    return f'Olá {nome}'


print(cumprimentar('Diego'))


# Exemplo 1
def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()} \n{'-' * len(texto)}"
    else:
        return f' {texto.title()} '.center(50, '*')


print(cabecalho('Diego Mirhan'))
print(cabecalho('Diego Mirhan', alinhamento=False))

# Biblioteca Mypy: pip install mypy
# Com o mypy, você pode checar se os tipos de um arquivo para ver se estão corretos
# No terminal, digite mypy nome_do_arquivo.py
