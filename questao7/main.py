from matematica import area_circulo, fatorial

if __name__ == "__main__":
    raio = float(input("Digite o raio do círculo: "))
    print(f"A área do círculo é: {area_circulo(raio):.2f}")
    
    try:
        num = int(input("Digite um número para calcular o fatorial: "))
        print(f"O fatorial de {num} é: {fatorial(num)}")
    except ValueError as e:
        print(f"Erro: {e}")