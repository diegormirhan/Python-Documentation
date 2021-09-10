"""
Teste de memória com generators

# Teste 1
for n in fib_listas(10000):
    print(n)
"""

# Função usando listas 11mb


def fib_listas(max):
    nums = []
    a, b = 0, 1
    while len(nums) <= max:
        nums.append(b)
        a, b = b, a + b
    return nums

# Função usando geradores


def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador <= max:
        a, b = b, a + b
        yield a
        contador += 1


# Teste 2 geradores 4MB
for n in fib_gen(10000):
    print(n)
