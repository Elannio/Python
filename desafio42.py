'''Refaça o desafio 35 dos triângulos, acrescentando 
o recurso de mostrar que tipo de triângulo será 
formado: equilátero: todos os lados iguais; 
isósceles: dois lados iguais; escaleno: todos os lados diferentes'''

lado1 = float(input('Digite o lado1: '))
lado2 = float(input('Digite o lado2: '))
lado3 = float(input('Digite o lado3: '))

if lado1 + lado2 > lado3 and lado3 + lado2 > lado1 and lado2 + lado3 > lado1:
    print('\033[31;44mPode formar um triângulo \033[m', end='')
    if lado3 == lado2 == lado1:
        print('\033[32;46mEQUILÁTERO\033[m')
    elif lado3 != lado2 != lado1 and lado3 != lado1:
        print('\033[37;45mESCALENO\033[m')
    else:
        print('\033[32;46mISÓSCELES\033[m')
else:
    print('\033[35;40mNão pode formar um triângulo\033[m')