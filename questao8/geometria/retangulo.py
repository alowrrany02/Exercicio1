def area_retangulo(base, altura):
    """Calcula a área de um retângulo"""
    if base < 0 or altura < 0:
        raise ValueError("Dimensões não podem ser negativas")
    return base * altura