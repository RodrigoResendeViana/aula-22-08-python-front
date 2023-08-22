def lista_palavras(frase):
    return frase.split(' ')


def conta_palavras(frase):

    lista = frase.split(' ')
    return len(lista)


frase = input('Informe uma frase: ')
print(lista_palavras(frase))
print(f'Quantidade de palavras: {conta_palavras(frase)}')