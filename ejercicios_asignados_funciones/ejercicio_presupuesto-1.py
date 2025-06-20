# Programa que recibe el monto total y calcula cuánto dinero va a cada área
def calculo_presupuesto(monto):
    recursos_humanos = monto * 0.50
    manufactura = monto * 0.25 
    empaquetado = monto * 0.15
    publicidad = monto * 0.10

    print("Distribución del presupuesto total:")
    print(f"Recursos Humanos: C${recursos_humanos:.2f}")
    print(f"Manufactura: C${manufactura:.2f}")
    print(f"Empaquetado: C${empaquetado:.2f}")
    print(f"Publicidad: C${publicidad:.2f}")

# Ejemplo de uso del programa:
monto_total = float(input("Ingrese el monto del presupuesto anual: "))
calculo_presupuesto(monto_total)


