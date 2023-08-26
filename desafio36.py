'''Escreva um programa para aprovar um empréstimo pra 
comprar uma casa, o programa vai perguntar o valor da 
casa, o salário do comprador e em quantos anos ele vai
pagar. Calcule o valor da prestação mensal, sabendo que 
ela não pode exceder 30% do salário ou então o 
empréstimo será negado.'''

casa = float(input('Qual o valor da casa? '))
salario = float(input('qual o seu salário? '))
anos = int(input('Em quantos anos você pretende pagar? '))

mensalidade = salario * 0.30
anos1 = anos * 12
presta = casa / anos1

if presta <= mensalidade:
    print(f'Para pagar em {anos1/12} anos a prestação será de {presta:.2f}. Então será aprovado!')
else:
    print('Empréstimo negado!')
