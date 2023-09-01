'''Crie um programa que leia vários números inteiros 
pelo teclado. O programa vai parar quando o usuário 
digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual 
foi a soma entre eles (Desconsiderando o flag)'''

num = 0
cont = 1
soma = 0

while num != 999:
    num = int(input("Digite um número, quando você digitar 999 irei parar de pedir."))
    cont += 1
    soma += num
print (f"O total de números que você digitou foi {cont} e a soma entre eles foi de {soma-999}")
    