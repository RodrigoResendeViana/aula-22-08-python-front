def preenche_lista():

    lista = []
    for i in range(10):
        numero = int(input('Número: '))
        lista.append(numero)
    print(lista)

    maior = max(lista)
    menor = min(lista)
    media = sum(lista) / len(lista)

    return maior, menor, media   #retorna uma tupla

resultado = preenche_lista()
print(resultado)
print(f'Maior: {resultado[0]}')
print(f'Menor: {resultado[1]}')
print(f'Média: {resultado[2]}')