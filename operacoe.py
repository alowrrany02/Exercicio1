def calcular_numeros():
    while True:
        try:
            num1 = float(input("Digite o primeiro número:"))
            num2 = float(input("Digite o segundo numero:"))
        except ValueError:
            print("Por favor digite um numero valido!!")
            continue

        print("As opções disponiveis são:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")

        opcao = input("Digite o numero da opção que vc escolheu:").strip()

        if opcao == '1':
            resultado = num1 + num2
            print(f"A soma dos numeros {num1} e {num2} é: {resultado}")
        elif opcao == '2':
            resultado = num1 - num2
            print(f"O resultado da subtração dos numeros {num1} e {num2} é: {resultado}")
        elif opcao == '3':
            resultado = num1 * num2
            print(f"O resultado da multiplicação dos numeros {num1} e {num2} é: {resultado}")
        elif opcao == '4':
            if num1 == 0:
                print("Erro: Nao é possivel dividir por 0")
            else:
                resultado = num1 / num2
                print(f"O resultado da divisão dos numeros {num1} e {num2} é {resultado}")
        elif opcao == 5:
            print("Pronto fechei!")
            break
        else:
            print("Opção invalida, verifique as opçoes e tente novamente!")

        while True:
            continuar = input("Voce quer continuar?(s/n)").strip().lower()
            if continuar == 's':
                break
            elif continuar == 'n':
                print("Ok, fechei aqui!")
                return
            else:
                print("Por favor escolha s para continuar e n para sair")



calcular_numeros()