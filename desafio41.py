'''A confederação nacional de federação precisa de um 
programa que leia o ano de nascimento de um atleta e 
mostre sua categoria, de acordo com a idade: 
até 9 anos: mirim; até 14 anos: infantil; 
até 19 anos: junior; até 25 anos: sênior; acima: master'''

from datetime import date

ano = int(input('Digite sua data de nascimento: '))
atual = date.today().year
idade = atual - ano

if idade <= 9:
    print('Você é mirim! ')
elif idade <= 14:
    print('Você é infantil! ')
elif idade <= 19:
    print('Você é junior! ')
elif idade <= 25: 
    print('Você é Sênior! ')
else:
    print('Você é Master! ')