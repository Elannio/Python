'''Crie um programa que leia um ano de nascimento de 
sete pessoas. No final, mostre quantas pessoas ainda 
não atingiram a maioridade e quantas já são maiores.'''

from datetime import date

atual = date.today().year
totmaior = 0
totmenor = 0

for n in range (1, 8):
    ano = int(input(f'Em que ano a {n} pessoa nasceu? '))
    idade = atual - ano
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1

print(f'Temos {totmaior} pessoas maiores de idade.')
print(f'Temos {totmenor} pessoas menores de idade.')