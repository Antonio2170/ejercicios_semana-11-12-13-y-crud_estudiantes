# Programa: Cálculo de importe con descuento

def calcular_importe_final(importe):
    if importe > 500:
        descuento = 0.12
    elif importe > 300:
        descuento = 0.10
    elif importe > 100:
        descuento = 0.05
    else:
        descuento = 0.0
    
    importe_final = importe * (1 - descuento)
    return importe_final, descuento

# Solicitar el importe de la compra al usuario
try:
    compra = float(input("Ingresa el importe de la compra (€): "))
    total_pagar, desc_aplicado = calcular_importe_final(compra)

    if desc_aplicado > 0:
        print(f"Se aplicó un descuento del {int(desc_aplicado*100)}%. Importe final a pagar: €{total_pagar:.2f}")
    else:
        print(f"No aplica descuento. Importe a pagar: €{total_pagar:.2f}")
except ValueError:
    print("Por favor, ingresa una cantidad válida.")
