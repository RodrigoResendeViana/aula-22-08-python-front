def conta_vogais(frase):

    frase = frase.lower()
    quantidade = frase.count('a')
    quantidade += frase.count('e')
    quantidade += frase.count('i')
    quantidade += frase.count('o')
    quantidade += frase.count('u')
    return quantidade

frase = input('Digite uma frase: ')
print(f'o número de vogais na frase é {conta_vogais(frase)}')