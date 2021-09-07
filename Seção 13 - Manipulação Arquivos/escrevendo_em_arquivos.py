"""
Escrevendo Em Arquivos

# OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele. Apenas ler.
Da mesma forma, se abrirmos um arquivo para escrita, não podemos lê-lo, somente escrever nele.

# OBS: Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional.

Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write().
Esta função recebe uma string como parâmetro, caso contrário teremos um TypeError

Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir, será criado.
Caso ele já exista, o anterior será apagado e um novo será criado. Dessa forma, todo
o conteúdo no arquivo anterior será perdido.


# Exemplo de escrita - modo 'w' - write (escrita)

with open('novo.txt', encoding='utf-8', mode='w') as arquivo:
    arquivo.write('Novos dados.\n')
    arquivo.write('Podemos colocar quantas linhas quizermos. \n')
    arquivo.write('Mas esta é a última linha.\n')




# Forma tradicional de escrita em arquivo (Não Pythônica)
arquivo = open('mais.txt', mode='w', encoding='utf-8')

arquivo.write('Alguma coisa escrita\n')
arquivo.write('Última linha escrita')

arquivo.close()



with open('geek.txt', encoding='utf-8', mode='w') as arq:
    arq.write('Diego\n' * 300)



"""

with open('frutas.txt', encoding='utf-8', mode='w') as arquivo:
    while True:
        fruta = input('Informa uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break
