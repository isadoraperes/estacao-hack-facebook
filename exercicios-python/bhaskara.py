# 4 - Crie uma função python que cálcule uma função de 2º Grau
#   Delta = B² - 4AC
#   Bhāskara = -B +- (raiz de delta)/ 2A
import math

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

def delta(a, b, c):
    return b**2 - 4*a*c

def print_bhaskara(a, b, c):
    d = delta(a, b, c)
    if d < 0:
        print('A equação não possui raizes reais')
    else:
        raiz1 = (-b + math.sqrt(d))/(2*a)
        raiz2 = (-b - math.sqrt(d))/(2*a)
        print(f'Maior raiz {raiz1}')
        print(f'Menor raiz: {raiz2}')

print_bhaskara(a, b, c)