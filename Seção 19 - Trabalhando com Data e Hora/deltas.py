"""
Trabalhando com deltas de data e hora

data_inicial = dd/mm/yyyy 12:30:00
data_final = dd/mm/yyyy 18:45:00

delta = data_final - data_inicial


import datetime

data_hoje = datetime.datetime.now()
aniversario = datetime.datetime(year=2004, month=6, day=19, hour=11)
tempo_para_evento = data_hoje - aniversario

print(type(tempo_para_evento))
print(repr(tempo_para_evento))
print(tempo_para_evento)

idade = tempo_para_evento / 365
print(f'Idade = {idade.days} anos')
"""
import datetime

data_da_compra = datetime.datetime.now()
print(data_da_compra)

regra_boleto = datetime.timedelta(days=3)
print(regra_boleto)

vencimento_boleto = data_da_compra + regra_boleto
print(vencimento_boleto)