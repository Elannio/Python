'''Crie um programa que leia uma frase qualquer e diga 
se ela é ou não um palíndromo, desconsiderando os espaços.'''

frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for n in range(len(junto) -1, -1, -1):
    inverso += junto[n]
print(f'Você digitou: {frase} e ele fica {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não é palíndromo! ')





