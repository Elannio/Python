'''Crie um programa que leia duas notas de um aluno e 
mostre sua média: média abaixo de 5.0: reprovado, média 
entre 5.0 e 6.9: recuperação, média 7.0 ou superior: 
aprovado.'''

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print('Reprovado')
elif media >= 5.0 and media < 7.0:
    print('Recuperação')
else:
    print('Aprovado')