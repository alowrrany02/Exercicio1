import math

def area_circulo(raio):
    """Calcula a área de um círculo dado seu raio"""
    return math.pi * raio ** 2

def fatorial(numero):
    """Calcula o fatorial de um número inteiro não negativo"""
    if numero < 0:
        raise ValueError("Fatorial não definido para números negativos")
    return math.factorial(numero)