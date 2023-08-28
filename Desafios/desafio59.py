'''Crie um programa que leia dois valores e mostre um 
menu na tela: 
[ 1 ]Somar
[ 2 ]multiplicar
[ 3 ]maior
[ 4 ]novos números
[ 5 ]sair do programa
Seu programa deverá realizar a operação solicitada em cada caso'''

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
valor = 0


while valor != 5:
    print ('''[ 1 ]Somar
[ 2 ]multiplicar
[ 3 ]maior
[ 4 ]novos números
[ 5 ]sair do programa''')
    valor = int(input("Digite de 1 a 5: "))
    if valor == 1:
        num3 = num1 + num2
        print (f'o valor será: {num3}')
    elif valor == 2:
        num3 = num1 * num2
        print (num3)
    elif valor == 3: 
        if num1 > num2:
            print (f'{num1} é maior.')
        else:
            print(f'{num2} é maior.')
    elif valor == 4:
        num1 = int(input("Digite o primeiro valor: "))
        5
        num2 = int(input("Digite o segundo valor: "))
    elif valor == 5:
        print("Você saiu")
    else:
        print('Operação inválida.')
print ('Fim do programa.')
