# Función que calcula el pago total según las horas trabajadas
def calcular_pago(horas):
    if horas <= 160:
        pago = horas * 6.5
    else:
        horas_normales = 160
        horas_extra = horas - 160
        pago = (horas_normales * 6.5) + (horas_extra * 7.5)
    return pago

# Programa principal
horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))

total_pagar = calcular_pago(horas_trabajadas)
print(f"Total a pagar: ${total_pagar:.2f}")

