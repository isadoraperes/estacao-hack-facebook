#args

#função que imprima 3 itens
#por param.

listaNum = [10, 5, 15]

def printItens(lista):
    for item in lista:
        print(f'esses são os itens da lista {item}')

printItens(listaNum)


def lista1(pessoa, *args):
    print(f'lista de: {pessoa}')
    for params in args:
        print(params)

lista1('blabla', 'arroz', 'feijão', 'tomate')
print('#########')

def lista2(**kwargs):
    fruta = kwargs.get('fruta')
    if fruta is not None:
        print(f'Na lista tem 1 fruta: {fruta}')
    else:
        print('Não tem fruta')

lista2(fruta='banana', massas='nhoque', verdura='alface')