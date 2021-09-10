"""
Tipo String

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre áspas simples: 'uma string', '2', 'a', 'True', '2.2'
- Estiver entre áspas duplas: "uma string", "2", "a", "True", "2.2"
- Estiver entre áspas simples triplas: '''uma string''', '''2''', '''a''', '''True''', '''2.2'''

nome = 'diego mirhan'
print(nome)
print(type(nome))

nome = "diego's bar"
print(nome)
print(type(nome))

nome = "diego \" mirhan"
print(nome)
print(type(nome))

nome = 'Diego \nMirhan'
print(nome)
print(type(nome))

print(nome.upper())

print(nome.lower())

print(nome.split()) # Transforma em uma lista de strings

print(nome[0:4])    # Slice de string

print(nome[0:4])    # Slice de string

# [   0,        1   ]
# ['Diego', 'Mirhan']
print(nome.split()[0])

print(nome.split()[1])
"""
# Estiver entre áspas triplas: """uma string""", """2""", """a""", """True""", """2.2"""

# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,  10,  11,  12 ]
# ['D', 'i', 'e', 'g', 'o', ' ', 'M', 'i', 'r', 'h', 'a', 'n']
nome = 'Diego Mirhan'

"""
[::-1] -> Começa no primeiro elemento, vai até o último elemento e inverte
"""
print(nome[::-1])   # Inversão da String Pythônica

print(nome.replace('o', 'a'))

print(type(nome))

texto = 'socorram me subino onibus em morrocos'
print(texto)

print(texto[::-1])
