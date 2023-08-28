'''Faça um programa que leia o ano de nascimento de um 
jovem e informe, de acordo com sua idade: Se ele ainda 
vai se alistar no serviço militar, se é a hora de se 
alistar, se ja passou o tempo do alistamento. Seu 
programa também deverá mostrar o tempo que falta ou 
que passou o prazo.'''
from datetime import date

ano = int(input('Qual o seu ano de nascimento? '))
atual = date.today().year
falta = atual - ano

if falta == 18:
    print('É hora de você se alistar, você já tem 18! ')
elif falta < 18:
    print(f'Você ainda vai se alistar no serviço militar, faltam {18 - falta} anos')
else:
    print(f'Você já passou da época de se alistar no serviço militar, passaram {(18 - falta) + 18} anos')