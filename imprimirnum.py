lista_ori = list(range(0,21))

lista_pares = []

for num in lista_ori:
    if num % 2 == 0:
        lista_pares.append(num)

print(lista_pares)