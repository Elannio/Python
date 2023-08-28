'''Escreva um programa que pergunte o salário de um 
funcionário e calcule o valor do seu aumento. Para 
salários superiores a R$1.250,00, calcule um aumento 
de 10%. Para inferiores ou iguais, o aumento é de 15%'''

salario = float(input('Qual o seu salário? '))

if salario <= 1250:
    salario2 = salario + (salario * 0.15)
    print(f'Seu salário com aumento é de {salario2}')
else:
    salario1 = salario + (salario * 0.10)
    print(f'Seu salário com aumento é de {salario1}')