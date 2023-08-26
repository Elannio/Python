#km percorridos por um carro alugado, e dias pelos quais ele foi;
#alugado, preço sabendo que o carro custa 60 por dia e;
#0.15 por km rodado

km = float(input('Quantos km você percorreu com o carro? '))
dia = int(input('Quantos dias você alugou o carro? '))

pre = (60 * dia) + (0.15 * km)

print(f'O preço a pagar por tudo é {pre}')