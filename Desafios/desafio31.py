'''Desenvolva um programa que pergunte a distância de 
uma viagem em Km. Calcule o preço da passagem, cobrando 
R$0,50 por Km para viagens de até 200km e R$0,40 para 
viagens mais longas.'''

viagem = int(input('Qual a distância da viagem em km? '))

valor1 = (viagem * 0.50)
valor2 = (viagem * 0.40)

if viagem <= 200:
    print(f'Sua viagem vai custar {valor1}')
else:
    print(f'Sua viagem vai custar {valor2}')