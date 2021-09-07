"""
POO - Métodos Mágicos

Métodos Mágicos são todos os métodos que utilizam dunder.

dunder init -> __init__()

Dunder -> Double Underscore

dunder repr -> Representação do objeto
"""


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas

    def __repr__(self):
        return f'{self.__titulo} escrito por {self.__autor}'

    def __str__(self):
        return self.__titulo

    def __len__(self):
        return self.__paginas

    def __del__(self):
        print('Um objeto do tipo Livro foi deletado da memória')

    def __add__(self, other):
        return f'{self} & {other}'

    def __mul__(self, other):
        if isinstance(other, int):
            msg = ''
            for n in range(other):
                msg += str(self) + '; '
            return msg
        return 'Não é possível multiplicar'


livro1 = Livro('Números do amor', 'Helen Hoang', 300)
livro2 = Livro('Ego', 'Osho', 150)

print(livro1)
print(livro2)

print(len(livro1))
print(len(livro2))

print(livro1 + livro2)
print(livro1 * 3)
