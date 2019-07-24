# 2 - crie uma função que receba uma lista de 20 valores aleatórios, retornar apenas o maior valor e printar em tela.
import random

def lista20():
    lista_aleatoria = []
    contador = 0 
    while contador < 20:
        lista_aleatoria.append(random.randrange(1, 100))
        contador = contador + 1

    print(f'{lista_aleatoria}')
    
    return lista_aleatoria


def print_maior(lista):
    maior_numero = 0

    for item in lista:
        if item > maior_numero:
            maior_numero = item

    return maior_numero


print(f'O maior número na lista é {print_maior(lista20())}')

