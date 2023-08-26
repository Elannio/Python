#Crie um programa que leia um número real e mostre sua porção inteira
#exemplo: 5.567 tem que ser 5
from math import trunc

num = float(input('Digite um número real: '))
print(trunc(num))
print(int(num))