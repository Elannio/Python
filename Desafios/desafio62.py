'''Melhore o desafio 061, perguntando ao usuário se ele 
quer mostrar mais alguns termos. O programa encerra 
quando ele disser que quer mostrar 0 termos.'''

num = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termo = 1

while termo <= 10: 
    termo_atual = num + (termo - 1) * razao
    print(f'Termo {termo}: {termo_atual}')
    termo += 1
    mais_termos = int(input('Você quer mostrar mais termos?'))
    if mais_termos != 0:
        termão = termo_atual + mais_termos
        termão = num + (termo - 1) * razao
        print(f'Termo {termo}: {termão}')
        termo += 1
        