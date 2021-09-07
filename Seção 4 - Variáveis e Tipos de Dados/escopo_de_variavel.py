"""
Escopo de variáveis

Dois casos de escopo:

1 - Váriaveis Globais;
    - Variáveis globais são conhecidas, ou seja, seu escopo compreende todo o programa.

2 - Variáveis Locais;
    - Variáveis locais são conhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
      está limitado ao bloco onde foi declarada.

Para declarar variáveis em Python, fazemos:

nome_da_variável = valor_da_variável

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declararmos uma variável, nós não colocamos o tipo de
dado dela. Este tipo é inferido ao atribuírmos o valor à mesma.

Exemplo em C:
int numero = 10;

Exemplo em Java:
int numero: 10;
"""

numero = 10  # Exemplo de variável Global
print(numero)
print(type(numero))

numero = 'Diego'
print(numero)
print(type(numero))

numero = 20


if numero > 10:
    novo = numero + 10  # A variável 'novo' está declarada localmente dentro do bloco do if. Portanto é variável local.
    print(novo)


