"""
Criando Loops

"""


def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


nome = "Diego Mirhan"
meu_for(nome)
