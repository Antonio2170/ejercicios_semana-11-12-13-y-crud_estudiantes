# Programa: Contador de palabras en un archivo

def contar_palabra(nombre_archivo, palabra_buscada):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read().lower()  # Convertimos a minúsculas para coincidencia sin importar mayúsculas
            palabra_buscada = palabra_buscada.lower()
            palabras = contenido.split()
            contador = palabras.count(palabra_buscada)
            print(f"La palabra '{palabra_buscada}' aparece {contador} veces en el archivo.")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")

# Solicitar palabra al usuario
palabra = input("Ingresa la palabra que deseas buscar: ")
contar_palabra("articulo.txt-2", palabra)
