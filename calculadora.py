"""
Calculadora básica que realiza operaciones aritméticas simples.
"""

def suma(a, b):
    """Realiza la suma de dos números."""
    return a + b

def resta(a, b):
    """Realiza la resta de dos números."""
    return a - b

def multiplicacion(a, b):
    """Realiza la multiplicación de dos números."""
    return a * b

def division(a, b):
    """Realiza la división de dos números."""
    if b != 0:
        return a / b
    else:
        return "Error: División por cero no permitida"

# Ejemplo de uso:
print(suma(2, 3))
print(resta(5, 2))
print(multiplicacion(4, 6))
print(division(10, 2))