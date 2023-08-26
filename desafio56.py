'''Desenvolva um programa que leia, nome, idade e sexo 
de quatro pessoas. No final o programa mostra: a média 
de idade do grupo; qual é o nome do homem mais velho; 
quantas mulheres têm menos de 20 anos'''

tot = 0

for n in range (0, 4):
    nome = str(input('Qual o seu nome? '))
    idade = int(input('Qual a sua idade? '))
    sexo = str(input('Digite M para sexo masculino e F para sexo feminino: '))
    media = (tot + idade) / 4

print(f'A média das idades é de {media}')

#VOLTAR DEPOIS NESSE EXERCÍCIO!