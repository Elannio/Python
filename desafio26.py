'''Ler uma frase pelo teclado e mostre: Quantas vezes aparece a letra "A";
 Em que posição ela aparece a primeira vez; Em que posição ela aparece a última vez'''

frase = str (input('Digite uma frase: ')).upper().strip()

print(f'A letra A, aparece {frase.count("A")}')
print(f'A letra A aparece a primeira vez na posição {frase.find("A")+1}')
print(f'A letra A aparece a última vez na posição {frase.rfind("A")+1}')