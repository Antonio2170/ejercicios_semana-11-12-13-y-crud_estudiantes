# Programa: Encontrar el menor de tres números reales

def menor_de_tres(a, b, c):
    return min(a, b, c)

# Solicitar los tres números al usuario
try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    num3 = float(input("Ingresa el tercer número: "))

    resultado = menor_de_tres(num1, num2, num3)
    print(f"El menor de los tres números es: {resultado}")
except ValueError:
    print("Por favor, ingresa solo números reales válidos.")
