while True:
    try: 
        num = int(input("Digite um numero:"))
        if (num % 2 == 0):
            print(f"O numero {num} é par")
        else:
            print(f"O o numero {num} é impar")
    except ValueError: 
       print("Digite um numero valido")
       continue 
    resposta = input("Voce quer continuar?: (s/n)").strip().lower()
    if resposta != 's':
        print("Pronto fechei!")
        break