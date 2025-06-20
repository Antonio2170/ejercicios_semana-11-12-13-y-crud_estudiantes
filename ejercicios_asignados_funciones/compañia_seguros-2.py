# Función para calcular la comisión total de 3 ventas
def calcular_comision(venta1, venta2, venta3):
    comision = (venta1 + venta2 + venta3) * 0.10
    return comision

# Función principal para calcular el sueldo total de un vendedor
def calcular_pago_semanal(sueldo_base, venta1, venta2, venta3):
    comision = calcular_comision(venta1, venta2, venta3)
    sueldo_total = sueldo_base + comision
    return comision, sueldo_total

# Ejemplo de uso
n = int(input("Ingrese el número de vendedores: "))

for i in range(1, n+1):
    print(f"\nVendedor {i}:")
    sueldo_base = float(input("Ingrese el sueldo base: "))
    venta1 = float(input("Ingrese el monto de la venta 1: "))
    venta2 = float(input("Ingrese el monto de la venta 2: "))
    venta3 = float(input("Ingrese el monto de la venta 3: "))
    
    comision, total = calcular_pago_semanal(sueldo_base, venta1, venta2, venta3)
    
    print(f"Comisión por las tres ventas: C${comision:.2f}")
    print(f"Pago total semanal: C${total:.2f}")
