'''Refaça o desafio 051, lendo o primeiro termo e a 
razão de uma PA, mostrando os 10 primeiros termos da 
progressão usando estrutura while.'''

num = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termo = 1

while termo <= 10: 
    termo_atual = num + (termo - 1) * razao
    print(f'Termo {termo}: {termo_atual}')
    termo += 1