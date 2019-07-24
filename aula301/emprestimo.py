salario = float(input('Digite o seu salario: '))
if salario > 1000:
    emprestimo = float(input('Digite o valor do emprestimo desejado: '))
    if ((emprestimo > 2000) or (emprestimo < 15*salario)):
        input('Emprestimo aceito')
    else: 
        input('Emprestimo declinado')
else:
    print('Emprestimo declinado')


def media(*valores):
    sum = 0
    for n in valores[0]:
        sum += float(n)
    return sum/len(valores[0])

valor = None
lista = []

while True:
    valor = input('quais valores para média? digite sair para parar: ')
    if valor == 'sair':
        break
    lista.append(valor)

print('sua média é', media(lista))
