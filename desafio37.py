'''Escreva um programa que leia um número inteiro 
qualquer e peça para o usuário escolher qual será a 
base da conversão: 1 para binário, 2 para octal e 3 
para hexadecimal'''

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')

opcao = int(input('Sua Opção: '))

if opcao == 1:
    print(f'O {num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif opcao == 2:
    print(f'O {num} convertido para BINÁRIO é igual a {oct(num)[2:]}')
elif opcao == 3:
    print(f'O {num} convertido para BINÁRIO é igual a {hex(num)[2:]}')
else: 
    print('Opção inválida!')