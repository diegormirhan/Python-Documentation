"""
Decoradores (Decorators)

O que são Decorators?

- Decoradores são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- Decorators também são exemplos de Higher Order Functions;
- Decorators tem uma sintaxe própria, usando '@' (Sysntax Sugar)


# Decorators como funções (Syntax Não Recomendada / Sem Syntax Sugar)


def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você')
        funcao()
        print('Tenha um ótimo dia')
    return sendo()


def saudacao():
    print('Seja Bem-Vindo a Geek University')

# Testando 1

# saudacao()


seja_educado(saudacao)


# Testando 2

def raiva():
    print('EU TE ODEIO')


seja_educado(raiva)



# Decorators com Syntax Sugar (Sugar Syntax)


def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia')
    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print('Meu nome é Diego')


# Testando

apresentando()


@seja_educado_mesmo
def dormir():
    print('Quero Dormir...')


dormir()



-------------------------------------------------------------------------------
|      Home     |     Serviços     |    Produtos     |     Administrativo     |
-------------------------------------------------------------------------------

https://www.suaempresa.com.br/home
https://www.suaempresa.com.br/servicos
https://www.suaempresa.com.br/produtos
https://www.suaempresa.com.br/admin

# OBS: Não é código funcional. É apenas exemplo

def checa_login():
    if not request.usuario:
    redirect('https://www.suaempresa.com.br/login')


def home(request):
    return 'Pode Acessar Home'

def servicos(request):
    return 'Pode acessar serviços'

def produtos(request):
    return 'Pode acessar produtos'

@checa_login
def admin(request):
    return 'Pode acessar Login'
"""

# OBS: Não confunda Decorator com Decorator Function
