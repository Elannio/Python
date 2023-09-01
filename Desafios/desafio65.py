'''Crie um programa que leia vários números inteiros do 
teclado. No final, mostre a média entre todos os valores
 e qual foi o maior e o menor valores lidos. O programa 
 deve perguntar ao usuário se ele quer ou não continuar 
 a digitar valores.'''
 
media = 0
maior = float('-inf')  # Iniciar com um valor muito baixo para encontrar o maior
menor = float('inf')   # Iniciar com um valor muito alto para encontrar o menor
soma = 0
cont = 0  # Iniciar o contador em 0

while True:
    num = int(input("Digite um número. Se quiser parar, digite 0: "))
    
    if num == 0:
        break  # Sai do loop quando o usuário digitar 0
    
    cont += 1
    soma += num
    
    if num > maior:
        maior = num
    
    if num < menor:
        menor = num

if cont > 0:
    media = soma / cont

print(f"A média dos valores é de {media}, o maior número é {maior}, o menor número é {menor}.")
