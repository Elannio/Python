'''Elabore um programa que calcule o valor a ser pago 
por um produto, considerando o seu preço normal e 
condição de pagamento: a vista dinheiro/cheque: 10% de 
desconto; a vista no cartão: 5% de desconto; em até 
duas vezes no cartão: preço normal; 3x ou mais no 
cartão: 20% de juros'''

preco = int(input('Qual o preço do produto? '))
print('''Escolha uma das opções de pagamento: 
[ 1 ] À vista, dinheiro/cheque: 
[ 2 ] À vista Cartão: 
[ 3 ] 2X no cartão:
[ 4 ] 3x ou mais no cartão:''')

opcao = int(input('Qual você quer? '))

if opcao == 1:
    preco1 = preco - (preco * 0.10)
    print(f'O preço atual do produto passará a ser {preco1}')
elif opcao == 2:
    preco2 = preco - (preco * 0.05)
    print(f'O preço atual do produto passará a ser {preco2}')
elif opcao == 3:
    print(f'O preço atual do produto passará a ser {preco}')
elif opcao == 4:
    preco4 = preco + (preco * 0.20)
    parcelas = int(input('Quantas vezes? '))
    parcela = preco4 / parcelas
    print(f'Sua compra passará a ser dividida por {parcelas} vezes e o preço atual do produto passará a ser {preco4}')
else:
    total = 0
    print('Opção inválida de pagamento.')
