'''Faça um programa que leia um número qualquer e mostre
 o seu fatorial. Ex: 5! = 5x4x3x2x1=120'''

num = int(input('Digite um número para fazer o fatorial: '))

while num > 1:
    num2 = num * num-1
print('f{num2}')