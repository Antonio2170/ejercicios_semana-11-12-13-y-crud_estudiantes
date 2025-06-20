import os 
#se importa el modulo os para usar la funcion: os.path.exists(ruta)
ARCHIVO = "estudiantes.txt"

def cargar_estudiantes():
    estudiantes = []
    # La funcion os.path.exists() verifica si un archivo o carpeta existe en una ruta determinada 
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as archivo:
            for linea in archivo:
                codigo, nombre, apellido, carrera, = linea.strip().split(",")
                # linea.strip() Elimina espacios y saltos de linea (\n) al principio o a final.
                # split(",") Divide la cadena en una lista de partes, usando la coma como separador
                estudiantes.append({
                    "codigo": codigo,
                    "nombre": nombre,
                    "apellido": apellido,
                    "carrera": carrera
                })
    return estudiantes


def guardar_estudiante(estudiante):
    with open(ARCHIVO, "w") as archivo:
        for est in estudiante:
            linea = f"{est['codigo']}, {est['nombre']}, {est['apellido']},{est['carrera']}\n"
            archivo.write(linea)
            
            
def crear_estudiante(estudiante):
    codigo = input("codigo del estudiante: ")
    # verificar si el codigo ya existe
    # La funcion any() devuelve True si al menos un elemento de un iterable es verdadero.
    if any(est["codigo"] == codigo for est in estudiante):
        return
    
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    carrera = input("Carrera: ")
    
    estudiante.append({
        "codigo": codigo,
        "nombre": nombre,
        "apellido": apellido,
        "carrera": carrera
    })
    guardar_estudiante(estudiante)
    print("Estudiante agregado correctamente. \n")
    
    
def mostrar_estudiantes(estudiante):
    if not estudiante:
        print("No hay estudiantes registrados.\n")
        return
    
    print("\nLista de estudiantes:")
    for est in estudiante:
        print(f"Codigo: {est['codigo']}, Nombre: {est['nombre']}, est{['apellido']}, Carrera: est{['carrera']}")
    print()
    
    
def actualizar_estudiante(estudiante):
    codigo = input("Ingresa el codigo del estudiante a actualizar: ")
    for est in estudiante:
        if est["codigo"] == codigo:
            est["nombre"] = input(f"Nuevo nombre (actual: {est['nombre']}): ") or est["nombre"]
            est["apellido"] = input(f"Nuevo apellido (actual: {est['apellido']}): ") or est["apellido"]
            est["carrera"] = input(f"Nueva carrera (actual: {est['carrera']}): ") or est["carrera"]
            guardar_estudiante(estudiante)
            print("Estudiante actualizado.\n")
            
            
def eliminar_estudiante(estudiente):
    codigo = input("Ingrese el codigo del estudiante a eliminar: ")
    for est in estudiente:
        if est["codigo"] == codigo:
            estudiente.remove(est)
            guardar_estudiante(estudiente)
            print("Estudiante eliminado.\n")
            return
    print("No se encontro un estudiante con ese codigo.\n")
    
    
# Funcion menu principal
def menu():
    estudiante = cargar_estudiantes()
    while True:
        print("==== MENU CRUD ESTUDIANTES ====")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiante")
        print("3. Actualizar estudiante")
        print("4. Eliminar estudiante")
        print("5. salir")
        opcion = input("Selecciona una opcion (1-5:): ")
        
        if opcion == "1":
            crear_estudiante(estudiante)
        elif opcion == "2":
            mostrar_estudiantes(estudiante)
        elif opcion == "3":
            actualizar_estudiante(estudiante)
        elif opcion == "4":
            eliminar_estudiante(estudiante)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opcion no valida.\n")
            
# Insruccion para ejecutar el menu 
menu()        
        
    
    
     