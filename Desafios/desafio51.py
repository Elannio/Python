'''Ler o primeiro termo e a razão de uma PA. No final, 
mostre os 10 primeiros termos dessa progressão.'''

num = int (input('Digite o primeiro termo: '))
razao = int (input('Digite a razão da PA: '))
decimo = num + (10-1) * razao

for n in range (num, decimo +1, razao):
    print(n, end=' * ')