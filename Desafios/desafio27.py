'''Ler um nome completo de uma pessoa, mostrando em seguida 
o primeiro e o último nome separadamente. ex: ana maria de sousa,
primeiro = ana; último = sousa'''

nome = str(input('Digite seu nome: ')).strip()
nome = nome.split()

print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[len(nome)-1]}')