# 1 - Escreva um programa que leia o nome de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o nome e o salário do funcionário.

nome = input('Digite o seu nome: ')
horas_trabalhadas = float(input('Digite as horas trabalhadas: '))
valor_hora = float(input('Digite o valor por hora: '))

def salario(hr_trb, vl_hr):
    calc_salario = hr_trb * vl_hr
    return calc_salario

print(f'{nome}, obrigada por nos consultar. De acordo com as informações fornecidas o seu salário é de {(salario(horas_trabalhadas, valor_hora))}')

