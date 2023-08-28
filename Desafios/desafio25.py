'''Ler o nome de uma pessoa e diga se ela tem "SILVA" no nome.'''

nome = str(input('Qual seu nome: ')).strip()
print('silva' in nome.lower())