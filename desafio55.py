'''Faça um programa que leia o peso de cinco pessoas 
e no final mostre qual o maior e o menor peso lidos.'''

maior = 0
menor = 0

for n in range (1, 6):
    peso = float(input(f'Qual o peso da {n} pessoa? '))
    if peso == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso é {maior}.')
print(f'O menor peso é {menor}.')