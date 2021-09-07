"""
POO - Métodos

- Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações
que este objeto pode realizar no seu sistema.

Em Python, dividimos os métodos, em 2 grupos: Métodos de instância e Métodos de Classe

# Métodos de Instância

# O método dunder init (__init__) é um método especial chamdo de construtor e sua função é
construir o objeto a partir da classe.

OBS: Todo o elemento em Python que inicia e finaliza com duplo underline é chamado
de dunder (Double Underline)

OBS: Os métodos/funções dunder em Python são chamados de métodos mágicos.

ATENÇÃO! Por mais que possamos criar nossas próprias funções utilizando dunder (underline no início e no fim)
não é aconselhado. Python possui vários métodos com esta forma de nomenclatura e pode ser que mudemos o comportamento
dessas funções mágicas internas da linguagem. Então, evite ao máximo. De prefêrencia nunca o faça.

# Métodos são escritos em letras minúsculas. Se o nome for composto, o nome terá as palavras separadas por underline.




class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__contador = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__contador


class Produto:

    contador = 99999

    def __init__(self, nome, descricao, valor):
        self.__contador = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        ContaCorrente.contador = self.__contador

    def desconto(self, porcentagem):
        Retorna o valor do produto com o desconto
        return (self.__valor * (100 - porcentagem)) / 100


p1 = Produto('Battlefield 2042', 'PS5', 540)

print(p1.desconto(40))

print(Produto.desconto(p1, 40))  # self, desconto


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False


user1 = Usuario('Diego', 'Mirhan', 'mirhan.diego@gmail.com', '1337xantares1337')
user2 = Usuario('Anna', 'Mirhan', 'anna.mirhan@gmail.com', 'annaluiza1234')

print(user1.nome_completo())
print(user2.nome_completo())

print(Usuario.nome_completo(user1))
print(Usuario.nome_completo(user2))

nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o e-mail: ')
password = input('Informe a senha: ')
confirma_password = input('Confirme a senha: ')

if password == confirma_password:
    user = Usuario(nome, sobrenome, email, password)

else:
    print('Senha não confere...')
    exit(42)

print('Usuário criado com sucesso!')
user_password = input('Informe a senha de acesso: ')

if user.checa_senha(user_password):
    print('Acesso permitido')
else:
    print('Acesso negado')

print(f'Senha User Criptografada: {user._Usuario__senha}')

# Métodos de Classe em Python são conhecidos como Métodos estáticos em outras linguagens.
"""
from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Classe {cls}')
        print(f'Temos {cls.contador} usuário(a) no sistema')

    @classmethod
    def ver(cls):
        print('Teste')

    @staticmethod
    def definicao():
        return 'Olá'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')

    def nome_completo(self):    # Método Público
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):   # Método Público
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):   # Método Privado
        return self.__email.split('@')[0]


# Métodos de Classe

user1 = Usuario('Diego', 'Mirhan', 'mirhan.diego@gmail.com', '1337xantares1337')

Usuario.conta_usuarios()  # Forma correta
user1.conta_usuarios()   # Possível, mas incorreta


user7 = Usuario('Diego', 'Mirhan', 'mirhan.diego@gmail.com', '1337xantares1337')
print(user7._Usuario__gera_usuario())   # Acesso, de forma ruim...


# Método Estático

print(Usuario.contador)

print(Usuario.definicao())

user8 = Usuario('Diego', 'Mirhan', 'mirhan.diego@gmail.com', '1337xantares1337')

print(user8.contador)

print(user8.definicao())

