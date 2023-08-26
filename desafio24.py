'''CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA 
SE ELA COMEÇA OU NÃO COM O NOME SANTO'''

nome = str(input('Digite um nome de uma cidade: ')).strip()
print(nome[:5].lower() == 'santo')