# Programa: Tabla de multiplicar de un número

def imprimir_tabla(numero):
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Solicitar número entero al usuario
try:
    numero = int(input("Ingresa un número entero: "))
    imprimir_tabla(numero)
except ValueError:
    print("Por favor, ingresa un número entero válido.")
