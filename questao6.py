def gerenciar_lista_compras():
    lista_compras = []
    
    while True:
        print("\n--- MENU LISTA DE COMPRAS ---")
        print("1. Adicionar item")
        print("2. Remover item")
        print("3. Visualizar lista")
        print("4. Sair")
        
        opcao = input("Escolha uma opção (1-4): ")
        
        if opcao == "1":
            item = input("Digite o item a ser adicionado: ").strip()
            if item:
                lista_compras.append(item.lower())
                print(f"'{item}' foi adicionado à lista!")
            else:
                print("Por favor, digite um item válido.")
                
        elif opcao == "2":
            if not lista_compras:
                print("A lista está vazia!")
                continue
                
            print("\nItens na lista:")
            for i, item in enumerate(lista_compras, 1):
                print(f"{i}. {item}")
                
            try:
                num = int(input("Digite o número do item a remover: ")) - 1
                if 0 <= num < len(lista_compras):
                    removido = lista_compras.pop(num)
                    print(f"'{removido}' foi removido da lista!")
                else:
                    print("Número inválido!")
            except ValueError:
                print("Por favor, digite um número válido.")
                
        elif opcao == "3":
            if not lista_compras:
                print("Sua lista de compras está vazia!")
            else:
                print("\n--- SUA LISTA DE COMPRAS ---")
                for i, item in enumerate(lista_compras, 1):
                    print(f"{i}. {item.capitalize()}")
                    
        elif opcao == "4":
            print("Saindo do programa...")
            break
            
        else:
            print("Opção inválida! Por favor, escolha de 1 a 4.")

if __name__ == "__main__":
    gerenciar_lista_compras()