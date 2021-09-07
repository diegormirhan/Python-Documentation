def comer(comida, eh_saudavel):
    if eh_saudavel:
        final = 'quero manter a forma.'
    else:
        final = 'a gente só vive uma vez.'
    return f'Estou comendo {comida} porque {final}'


def dormir(num_horas):
    if num_horas > 8:
        return f'Putz, dormi muito! Estou atrasado para o trabalho!'
    else:
        return f'Continuo cansado após dormir por {num_horas} horas. :('


def cor_favorita(cor):
    cores = ['branco', 'vermelho', 'azul']
    if cor in cores:
        return True
    return False


def numeros(numero):
    if numero >= 10:
        return None
    return False
