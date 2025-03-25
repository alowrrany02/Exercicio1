def analise_numeros(lista):
    if not lista:
        return None, None, None
    
    media = sum(lista) / len(lista)
    maior = max(lista)
    menor = min(lista)
    
    return media, maior, menor

numeros = [10, 5, 8, 12, 3]
media, maior, menor = analise_numeros(numeros)

print(f"Média: {media:.2f}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")