'''Escreva um programa que leia a velocidade de um carro
. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo
 que ele foi multado. A multa vai custar R$7,00 por cada
  km acima do limite.'''

km = int(input('Quantos quilômetros o carro está? '))

if km > 80:
    km1 = (km - 80) * 7
    print(f'Você foi multado, a sua multa é de {km1}')
else:
    print('Siga em frente')