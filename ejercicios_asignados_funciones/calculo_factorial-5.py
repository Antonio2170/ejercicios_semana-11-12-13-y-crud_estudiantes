# Función que calcula el factorial
def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

# Programa principal
numero = int(input("Ingrese un número entero positivo: "))

if numero < 0:
    print("El factorial no está definido para números negativos.")
else:
    resultado = calcular_factorial(numero)
    print(f"El factorial de {numero} es: {resultado}")
