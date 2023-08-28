#Ler um numero inteiro e mostre seu dobro, triplo e raiz quadrada.

num = int(input("Digite um numero."))
raiz = pow(num, (1/2))
print(f"O dobro de {num} é {num+num}, o triplo é {num*3} e a raiz quadrada é {raiz}")