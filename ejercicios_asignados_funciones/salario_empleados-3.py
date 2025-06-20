#Funcion para calcular 10% de renta 
def calcular_descuento(salario):
    return salario * 0.10

#Solicitar cuantos empleados disponen de sueldo
n = int(input("Cuantos empleados desea registrar?: "))

for i in range(1, n + 1):
    salario = float(input(f"Ingrese el salario del empleado {i}: "))
    descuento = calcular_descuento(salario)
    pago_total = salario - descuento
    
    print(f"\nEmpleado {i}")
    print(f"Salario Bruto: C${salario:.2f}")
    print(f"Descuento de renta (10%): C${descuento:.2f}")
    print(f"Total a pagar: C${pago_total:.2f}\n")
    


    
    
    

    


    

