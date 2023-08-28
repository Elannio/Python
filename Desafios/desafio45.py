'''Crie um programa que faça o computador jogar pedra 
papel e tesoura com você.'''

from random import randint
from time import sleep

itens = ('Pedra','Papel','Tesoura')

computador = randint(0,2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogador = int(input('Qual a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print('-=' * 14)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 14)

if computador == 0:
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Jogador Vence!')
    elif jogador == 2:
        print('Computador Vence!')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1:
    if jogador == 0:
        print('Computador vence!')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Jogador vence!')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2:
    if jogador == 0:
        print('Jogador vence!')
    elif jogador == 1:
        print('Computador vence!')
    elif jogador == 2:
        print('Empate!')
    else:
        print('JOGADA INVÁLIDA!')
else:
    print('Inválido!1')