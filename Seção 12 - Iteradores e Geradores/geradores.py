"""
Geradores

- Geradores(Generators) são Iteradores(Iterators);

OBS: O contrário não é verdadeiro. Ou seja, nem todo iterator é um gerador.

Outras informações:
- Generators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com Expressões Geradoras;

Diferenças entre Funções e Generator Functions(Funções Geradoras)

--------------------------------------------------------------------------------------------
| Funções                                       | Generator Functions                      |
--------------------------------------------------------------------------------------------
| utilizam return                               | utilizam yield                           |
--------------------------------------------------------------------------------------------
| retorna uma vez                               | podem utilizar yeild múltiplas vezes     |
--------------------------------------------------------------------------------------------
| quando executada, retorna um valor            | quando executada, retorna um generator   |
--------------------------------------------------------------------------------------------



gen = conta_ate(5)

print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
"""

# Exemplo Função geradora (Generator function)


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1

# Um generator function não é um generator. Ele gera um generator.


gen2 = conta_ate(5)

for num in gen2:
    print(list(gen2))

