# 3 - crie uma lista com 10 números aleatórios, itere essa lista e printar em tela os valores que são ímpares e pares.
# exemplo de resultado em tela:
# Essa foi a lista gerada aleatóriamente:
# [37, 52, 73, 91, 49, 67, 19, 64, 58, 22]
# ímpares: [37, 73, 91, 49, 67, 19]
# pares: [52, 64, 58, 22]
import random

def lista10():
    lista_aleatoria = []
    contador = 0 
    while contador < 10:
        lista_aleatoria.append(random.randrange(1, 100))
        contador = contador + 1
    print(f'Essa é a lista aleatória {lista_aleatoria}')
    return lista_aleatoria

def oddnumbers():
    lista = lista10()
    listaPar = []
    listaImpar = []
    for item in lista:
        if item % 2 == 0:
            listaPar.append(item)
        else:
            listaImpar.append(item)
    
    print(f'Esses são os numeros impares: {listaPar}')
    print(f'Esses são os numeros pares: {listaImpar}')

    
oddnumbers()
