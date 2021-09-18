"""
O operador Walrus permite fazer a atribuição e retorno de valor em uma única expressão.

variavel := expressão
"""
nome = 'Geek University'
print(nome)

print(nome := 'Geek University')

# Python 3.7
cesta1 = []
fruta1 = input('Informe a fruta: ')
while fruta1 != 'jaca':
    cesta1.append(fruta1)
    fruta1 = input('Informe a fruta: ')


# Python 3.8
cesta = []
while (fruta := input('Informe a fruta: ')) != 'jaca':
    cesta.append(fruta)
