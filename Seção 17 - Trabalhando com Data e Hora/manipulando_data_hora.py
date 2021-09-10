"""
Manipulando Data e Hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora
chamado datetime

print(dir(datetime))

print(datetime.MAXYEAR)
print(datetime.MINYEAR)

# Retorna a data e hora corrente
print(datetime.datetime.now())  # 2021-08-06 20:35:14.232736

# datetime.datetime(year, month, day, hours, minutes, seconds, microseconds)
print(repr(datetime.datetime.now()))  # datetime.datetime(2021, 8, 6, 20, 37, 8, 253778)

# replace() para fazer ajustes na data e hora
inicio = datetime.datetime.now()
print(inicio)

# Alterar o horário para 21 horas, 0 minutos, 0 segundos, 0 microsegundos
inicio = inicio.replace(hour=21, minute=0, second=0, microsecond=0)
print(inicio)


# Recebendo dados do usuário e convertendo para data
evento = datetime.datetime(2021, 1, 1, 0)
print(type(evento))
print(evento)

print(type('01/01/2021'))
print('01/01/2021\n')

nascimento = input('Insira sua data de nascimento (dd/mm/yyyy): ')
print(nascimento)
print(type(nascimento))
nascimento = nascimento.split('/')

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
print(nascimento)
print(type(nascimento))
"""

import datetime

evento = datetime.datetime.now()

# Acesso individual dos elementos de data e hora

print(evento.year)
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.minute)
print(evento.second)
print(evento.microsecond)
