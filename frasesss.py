frase = 'Curso em Vídeo Python'
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[1:15:2])
print(frase[::2])
print(frase.count('o'))
print(len(frase))
print(frase.find('Vídeo'))
print(frase.replace('Vídeo', 'Áudio'))
print('Vídeo' in frase)
print('vídeo' in frase)
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip()) #Removeria tds os espaços inúteis
print(frase.rstrip()) #Removeria tds os espaços da direita
print(frase.lstrip()) #Removeria tds os espaços da esquerda
print(frase.split())
print('*'.join(frase))