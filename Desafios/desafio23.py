'''Faça um programa que leia um número de 0 a 9999 e mostre
na tela cada um dos dígitos separados. ex: digite 1834, unidade: 4;
dezena:3; centena: 8; milhar:1'''

numero = int(input('Digite um número de 0 a 9999: '))

U = numero // 1 % 10
D = numero // 10 % 10
C = numero // 100 % 10
M = numero // 1000 % 10

print(f'Unidade {U}')
print(f'dezena {D}')
print(f'Centena {C}')
print(f'Milhar {M}')