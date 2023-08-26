'''Melhore o jogo do desafio 028 onde o computador vai
"pensar" em um número entre 0 e 10. só que agora o 
jogador vai tentar adivinhar até acertar, mostrando no 
final quantos palpites foram necessários para vencer.'''

import random

pal = 0
num = random.randint(0,10)
num1 = int(input('Digite um número de 0 a 10: '))

while num1 != num:
    if num1>num:
        print('Menos...')
    else:
        print('Mais...')
    num1 = int(input('Digite um número de 0 a 10: '))
    pal += 1

print(f'Parabéns, o número que o computador pensou era {num}, e você acertou na {pal+1} vez.')