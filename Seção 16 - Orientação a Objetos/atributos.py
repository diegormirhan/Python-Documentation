"""
POO - Atributos

Atributos -> Representam as características do objeto. Ou seja, pelos atributos
nós conseguimos representar computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de Instância;
    - Atributos de Classe;
    - Atributos Dinâmicos;

# Atributos de Instância: São atributos declarados dentro do método construtor.

# OBS: Método Construtor: É um método especial utilizado para a construção do objeto.


# Em java, uma Classe Lâmpada, incluindo seus atributos ficaria mais ou menos:

public class Lampada(){
    private int voltagem;
    private String cor;
    private Boolean ligada = false;

    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this cor = cor;
    }
}

Em Python, por convenção, fica estabelecido que, todo atributo de uma classe é público.
Ou seja, pode ser acessado em todo o projeto.
Caso queiramos demonstrar que determinado atributo deve ser tratado como privado, ou seja,
que deve ser acessado/utilizado somente dentro da própria classe onde está declarado,
utiliza-se __ duplo underline no início do seu nome.

Isso é conhecido também como Name Mangling.



# OBS: Lembre-se que isso é apenas uma convenção, ou seja, a lingugem Python não
# vai impedir que façamos acesso aos atributos sinalizados como privados fora da classe.

# Exemplo


user = Acesso('user@gmail.com', '1234')
print(user.email)
# print(user.__senha)  # AttributeError

print(user._Acesso__senha)  # Temos acesso. Mas não deveríamos fazer este acesso. (Name Mangling)

user.mostra_senha()
user.mostra_email()



# O que significa Atributos de Instância?

# Significa, que ao criarmmos instâncias/objetoos de uma classe, todas as instâncias
# terão esses atributos.

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '654321')

user1.mostra_email()
user2.mostra_email()




p3 = Produto('Playstation 5', 'Video Game', 7400)
p4 = Produto('XBox One X', 'Video Game', 5500)

print(p3.valor)
print(p4.valor)

# OBS: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe

print(Produto.imposto)

print(p3.contador)
print(p4.contador)

# OBS: Em linguagens como o Java, os atributos conhecidos como Atributos de Classe aqui em Python
# são chamados de atributos estáticos;

"""

# Classes com Atributo de Instância Público


class Lampada:

    def __int__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Classes com Atributo de Instância Privado


class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


# Atributos de Classe

p1 = Produto('Playstation 5', 'Video Game', 7000)
p2 = Produto('XBox One X', 'Video Game', 5000)

# Atributos de classe, são atributos que são declarados diretamente na classe, ou seja,
# fora do construtor. Geralmente já inicializamos um valor, e este valor é compartilhado entre
# todas as instâncias da classe. Ou seja, ao invés de cada instância da classse ter seus próprios
# valores como é o caso dos atributos de instância, com os atributos de classe todas as instãncias
# terão o mesmo valor para este atributo.


# Refatorar a classe Produto

class Produto:

    # Atributo de classe
    imposto = 1.05   # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.contador += 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.contador


# Atributos Dinâmicos -> Um atributo de instância que pode ser criado em tempo de execução

# OBS: O atributo dinânamico será exclusivo da instância que o criou.

p5 = Produto('Playstation 5', 'Video Game', 7000)
p6 = Produto('XBox One X', 'Video Game', 5000)

# Criando um atributo dinâmico em tempo de execução

p5.peso = "5kg"  # Note que na classe Produto não existe o produto peso

print(f'Produto: {p5.nome}, Descrição: {p5.descricao}, Valor: {p5.valor}, Peso: {p5.peso}')

# print(f'Produto: {p6.nome}, Descrição: {p6.descricao}, Valor: {p6.valor}, Peso: {p6.peso}')

# Deletando Atributos

print(p5.__dict__)
print(p6.__dict__)

print(Produto.__dict__)

del p5.peso
del p5.valor
del p5.descricao

print(p5.__dict__)
print(p6.__dict__)
