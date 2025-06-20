# Programa: Cálculo del área de un círculo

import math

def area_circulo(radio):
    return math.pi * radio**2

# Solicitar el radio al usuario
try:
    radio = float(input("Ingresa el radio del círculo: "))
    resultado = area_circulo(radio)
    print(f"El área del círculo con radio {radio} es: {resultado:.2f}")
except ValueError:
    print("Por favor, ingresa un número válido.")
