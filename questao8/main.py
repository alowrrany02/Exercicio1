from geometria import area_circulo, area_retangulo

def main():
    print("Calculadora de Áreas")
    print("1. Círculo")
    print("2. Retângulo")
    
    opcao = input("Escolha uma opção (1-2): ")
    
    try:
        if opcao == "1":
            raio = float(input("Digite o raio do círculo: "))
            area = area_circulo(raio)
            print(f"Área do círculo: {area:.2f}")
        elif opcao == "2":
            base = float(input("Digite a base do retângulo: "))
            altura = float(input("Digite a altura do retângulo: "))
            area = area_retangulo(base, altura)
            print(f"Área do retângulo: {area:.2f}")
        else:
            print("Opção inválida!")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()