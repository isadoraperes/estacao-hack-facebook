import random
import statistics

#exercicio 01
lista_aleatoria = []
contador = 0

while contador < 20:
    contador = contador + 1
    lista_aleatoria.append(random.randrange(1,20))

print(f'Aqui está a lista aleatória: {lista_aleatoria}')

#exercicio 02
def print_lista():
    numero_maior = 0

    for item in lista_aleatoria:
        if item > numero_maior:
            numero_maior = item

    return numero_maior

#função do professor para exercicio 02
def maior_valor(lista_aleatoria):

    #função max(iterable, [key])
    return max(lista_aleatoria, key=int)

print(f'Esse é o maior número da lista: {maior_valor(lista_aleatoria)}')
print(f'Esse é o maior número da lista: {print_lista()}')

#função para tirar média
def media(param):
    return statistics.mean(param)

print(f'Essa é a media dos numeros da lista: {media(lista_aleatoria)}')

#teste para verificar o funcionamento da função
numeros = [6, 8]

print(f'Teste {media(numeros)}')