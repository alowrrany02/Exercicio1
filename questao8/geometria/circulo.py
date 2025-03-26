import math

def area_circulo(raio):
    """Calcula a área de um círculo dado seu raio"""
    if raio < 0:
        raise ValueError("Raio não pode ser negativo")
    return math.pi * raio ** 2