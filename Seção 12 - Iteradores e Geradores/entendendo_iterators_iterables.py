"""
Entendendo Iterators e Iterables

Iterator:
    - Um objeto que pode ser iterado.
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada;

Iterable:
    - Um objeto que irá retornar um iterator quando a função iter() for chamada.


nome = 'Diego'  # É UM ITERABLE MAS NÃO UM ITERATOR
number = [1, 2, 3, 4, 5]   # É UM ITERABLE MAS NÃO UM ITERATOR

it1 = iter(nome)
it2 = iter(number)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

print("\n")

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))

"""