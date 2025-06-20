# Ejercicio 4: Lector de Datos CSV

# Paso 1: Abrir el archivo productos.csv en modo lectura
try:
    with open("productos.csv", "r", encoding="utf-8") as archivo:
        print("Lista de Productos:\n")
        
        # Paso 2: Recorrer el archivo línea por línea
        for linea in archivo:
            # Paso 3: Eliminar salto de línea final
            linea = linea.strip()
            
            # Paso 4: Separar por comas
            partes = linea.split(',')
            
            # Validación opcional por si alguna línea no tiene 3 elementos
            if len(partes) == 3:
                nombre = partes[0]
                precio = partes[1]
                cantidad = partes[2]

                # Paso 5: Imprimir en formato legible
                print(f"Producto: {nombre} | Precio: ${precio} | Stock: {cantidad} unidades")
            else:
                print("Línea con formato incorrecto:", linea)

except FileNotFoundError:
    print("El archivo 'productos.csv' no fue encontrado. Asegúrate de que exista en la carpeta.")
