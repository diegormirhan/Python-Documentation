"""
Teste de memória com Expressões Geradoras

# Generators (Geradores)


def nums():
    for num in range(1, 10):
        yield num


gen1 = nums()
print(gen1)

print(next(gen1))
print(next(gen1))


gen2 = (num for num in range(1, 10))
print(gen2)  # Generation Expression

print(next(gen2))
print(next(gen2))

"""

# Realizando o teste de velocidade
import time

# Generator Expression

gen_inicio = time.time()
print(sum(num for num in range(100000000)))
gen_tempo = time.time() - gen_inicio


# List Comprehension

list_inicio = time.time()
print(sum([num for num in range(100000000)]))
list_tempo = time.time() - list_inicio

print(f'Generator Expression levou {gen_tempo}')
print(f'List Comprehension levou {list_tempo}')
