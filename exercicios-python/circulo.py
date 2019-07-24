# 5 - Faça um programa que leia o raio de um círculo e faça duas funções: uma que calcule a área do círculo e outra que calcule o comprimento do círculo.
import math 

raio = float(input('Digite o valor do raio do circulo: '))

def pi():
    return 3.141592

def area_circulo(r):
    area = (pi()*(r**2))
    print(f'A area é {area}')
    return area

def comp_circulo(r):
    comprimento = ((pi()*2)*r)
    print(f'O comprimento é {comprimento}')
    return comprimento

area_circulo(raio)
comp_circulo(raio)