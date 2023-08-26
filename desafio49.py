'''Refaça o desafio 9 mostrando a tabuada de um número 
que o usuário escolher, só que agora utilizando o laço 
for.'''

num1 = int(input("Digite um número: "))

for c in range(1, 11):
    print(f'{num1} x {c} = {num1 * c}')