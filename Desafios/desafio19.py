# o professor quer sortear um dos 4 alunos para apagar o quadro
'''import random

a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
lista = [a1, a2, a3, a4]

a = random.choice(lista)
print(f'O aluno escolhido foi {a}')'''

from random import choice

a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
lista = [a1, a2, a3, a4]

a = choice(lista)
print(f'O aluno escolhido foi {a}')