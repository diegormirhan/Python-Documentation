import time
from threading import Thread

contador = 50000000


def contagem_regressiva(n):
    while n > 0:
        n -= 1


inicio = time.time()
contagem_regressiva(contador)
fim = time.time()

print(f'Tempo em segundos: {fim - inicio}')

# Tempo em segundos: 9.846121072769165

