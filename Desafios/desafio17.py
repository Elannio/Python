# faça um programa que leia o comprimento de um cateto adjacente de um tri
# retângulo, calcule e mostre o comprimento da hipotenusa
'''cat = float(input('Qual o primeiro comprimento do cateto adjacente do triângulo retângulo? '))
cat1 = float(input('Qual o segundo comprimento do cateto adjacente do triângulo retângulo? '))

hip = cat**2 + cat1**2
hip1 = pow(hip, (1/2))

print(f'O comprimento da hipotenusa é de {hip1:.2f}')'''

import math

cat = float(input('Qual o primeiro comprimento do cateto adjacente do triângulo retângulo? '))
cat1 = float(input('Qual o segundo comprimento do cateto adjacente do triângulo retângulo? '))
hi = math.hypot(cat, cat1)
print(f'O comprimento da hipotenusa é de {hi:.2f}')


