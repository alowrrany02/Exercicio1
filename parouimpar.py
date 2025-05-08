def veri_paridade(num):
    if num % 2 == 0:
        print(f"O numero {num} é par")
    else:
        print(f"O o numero {num} é impar")

def pedir_num ():
    while True:
        entrada = input("Digite um numero inteiro:")
        try:
            num = int(entrada)
            return num
        except ValueError:
            print("Por favor digite um numero válido!")

def pedir_continuar():
    while True:
        resposta = input("Voce deseja continuar?(s/n)").strip().lower()
        if resposta == 's':
            return True
        elif resposta == 'n':
            return False
        else:
            print("Por favor, digite s para continuar ou n para parar!")


def main():
    print("=== Teste de Paridade ===")
    while True:
        num = pedir_num()
        resposta = veri_paridade(num)
        print(resposta)

        if not pedir_continuar():
            print("Pronto fechei")
            break
if __name__ == "__main__":
    main()