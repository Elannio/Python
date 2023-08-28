'''Crie um programa que leia o nome completo de uma pessoa
e mostre: o nome com todas as letras maiúsculas;
todas as letras minúsculas; quantas letras ao todo(sem considerar espaços);
quantas letras tem o primeiro nome'''

nome = str(input('Digite seu nome completo: ')).strip()

'''maiuscula = 
minuscula = 
totalLetras = 
primeiroNome ='''

print(f'Seu Nome Completo em maiúsculo: {nome.upper()}')
print(f'Seu Nome Completo em minúsculo: {nome.lower()}')
print(f'Letras ao todo: {len(nome) - nome.count(" ")}')
print(f'O primeiro nome tem: {nome.find(" ")} letras')