"""
Funções com Parâmetro Padrão(Default Paramters)

- Funções onde a passagem de parâmetro seja opcional;

# Exemplo de função onde a passagem de parâmetro seja opcional
print('Geek University')

print()


# Exemplo onde a passagemm de parâmetro seja obrigatória


def quadrado(numero):
    return numero ** 2


print(quadrado(3))
print(quadrado()) # TypeError




def exponencial(numero=4, potencia=2):
    return numero ** potencia


print(exponencial(2, 3))  # 2 * 2 * 2 = 8
print(exponencial(3, 2))  # 3 * 3 = 9

print(exponencial(3))  # Por padrão eleva ao quadrado
print(exponencial(3, 5))  # Eleva a potência indicada pelo usuário

# OBS:
# Se o usuário passar somente 1 argumento, este será atribuído ao parâmetro numero, e será calculado o quadrado deste
# número;

# Se o usuário passar 2 argumentos, o primeiro será atribuido ao parâmetro numero e o segundo ao parâmetro potência.
# Então será calculada esta potência.


print(exponencial())

# OBS: Em funções Python, os parâmetros com valores default(padrão) DEVEM sempre estar ao final da declaração.

# ERRO!


def teste(num=2, potencia):
    return num ** potencia

print(teste(6))



# Outros exemplos


def soma(num1=5, num2=3):
    return num1 + num2


print(soma(4, 3))
print(soma(1))
print(soma())


# Exemplo mais comlexo


def mostra_informacao(nome='Diego', instrutor=False):
    if nome == 'Diego' and instrutor:
        return 'Bem-Vindo Instrutor Diego'
    elif nome == 'Diego':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Ronaldo'))
print(mostra_informacao(nome='Ronaldo'))

# Por quê utilizar parâmetros com valor default?

- Nos permite sem mais flexiveis nas funções;
- Evita erros com parâmetros incorretos;
- Nos permite trabalhar com exemplos mais legíveis de código;


# Quais tipos de dados podemos utilizar com valores default com parâmetros?

- Qualquer tipo de dado:
     - Números, Strings, Floats, Boleanos, Listas, Tuplas, Dicionários, Funções e etc;



# Exemplos


def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, subtracao))




# Escopo - Evitar problemas e confusões...

# Variáveis Locais
# Variáveis Globais

instrutor = 'Geek'  # Variável Global


def diz_oi():
    instrutor = 'Diego'  # Variável Local
    return f'Olá {instrutor}'


print(diz_oi())

# Se tivermos uma local com o mesmo nome de uma variável global, a local terá preferência




def diz_oi():
    prof = 'Diego'  # Variável Local
    return f'Olá {prof}'


print(diz_oi())
print(prof)  # NameError




# ATENÇÃO com variáveis globais (Se puder evitar, evite!)

total = 0


def incrementa():
    total = total + 1  # UnboundLocalError (a variável local está sendo utilizada para processamento sem ter
    # sido inicializada)
    return total


print(incrementa())




total = 0


def incrementa():
    global total  # Avisando que queremos utilizar a variável global
    total = total + 1
    return total


print(incrementa())
print(incrementa())
print(incrementa())

"""

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável


def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador

    return dentro()


print(fora())
print(fora())
print(fora())



