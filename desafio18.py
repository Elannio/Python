#ler um ângulo e mostre na tela o valor do seno, cosseno
#e tangente

import math

ang = float(input('Qual o ângulo? '))

sen = math.sin(math.radians(ang))
print(f'O seno do ângulo {ang}, é de {sen:.2f}')

cos = math.cos(math.radians(ang))
print(f'O cosseno do ângulo {ang}, é de {cos:.2f}')

tan = math.tan(math.radians(ang))
print(f'A tangente do ângulo {ang}, é de {tan:.2f}')