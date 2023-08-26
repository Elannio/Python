#ler a largura e altura de uma parede em metros, calcule
#sua área e a quantidade de tinta necessária para pintá-la
#sabendo que cada litro de tinta pinta uma área de 2m quadrados

altura = float(input('Qual a altura da parede em metros? '))
largura = float(input('Qual a largura da parede em metros? '))

area = (altura * largura) / 2

print(f'A quantidade de tinta necessária para pintar a parede é de {area} litros')