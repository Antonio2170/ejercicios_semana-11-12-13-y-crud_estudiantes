# Programa: Filtrado de líneas por palabra clave

def filtrar_lineas(nombre_entrada, nombre_salida, palabra_buscada):
    try:
        with open(nombre_entrada, 'r', encoding='utf-8') as archivo_entrada, \
             open(nombre_salida, 'w', encoding='utf-8') as archivo_salida:

            palabra_buscada = palabra_buscada.lower()

            for linea in archivo_entrada:
                if palabra_buscada in linea.lower():
                    archivo_salida.write(linea)

        print(f"Las líneas que contienen '{palabra_buscada}' se han guardado en '{nombre_salida}'.")

    except FileNotFoundError:
        print(f"El archivo '{nombre_entrada}' no fue encontrado.")

# Solicitar palabra al usuario
palabra = input("Ingresa la palabra a filtrar: ")
filtrar_lineas("libro.txt-8", "filtrado.txt-8", palabra)
