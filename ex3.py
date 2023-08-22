def remove_espacos(frase):
    
    return frase.replace(' ','')

frase = input('Frase: ')
print(f'Frase sem espaços: {remove_espacos(frase)}')