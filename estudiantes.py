estudiantes= {
       "Juan Perez":{ "edad":17 ,"materias":["matematicas","Fisica"]},
       "Ana gomez": {"edad": 16 ,"materias":["quimica","historia"]},
        "Pedro Lopez": {"edad": 18, "materias": ["Biologia", "Ingles"]}
}

def nuevo_estudiante():
  nombre=input("ingrese su nombre")
  edad=int(input("ingrese su edad")) 
  materias = input("Materias aprobadas (separadas por coma): ").split(",")
  materias = [m.strip().capitalize() for m in materias]
  estudiantes[nombre] = {"edad": edad, "materias": materias}
  print(f"Estudiante '{nombre}' agregado con éxito.")

def mostrar_estudiantes():
    for nombre, info in estudiantes.items():
        print(f"{nombre} - Edad: {info['edad']} - Materias: {', '.(info['materias'])}")
    print()

def buscar_estudiante():
    nombre = input("Nombre del estudiante a buscar: ")
    if nombre in estudiantes:
        info = estudiantes[nombre]
        print(f"{nombre} - Edad: {info['edad']} - Materias: {',(info['materias'])}")
    else:
        print("Estudiante no encontrado.")

def verificar_palabra():
    palabra = input("Palabra clave: ").lower()
    encontrados = [nombre for nombre in estudiantes if palabra in nombre.lower()]
    if encontrados:
        print("Estudiantes encontrados:", ", ".(encontrados), "")
    else:
        print("No se encontro ningun estudiante con esa palabra.")


#menu
#imprimir la opciones
#ingresar la opcion 
#validar la entrada de opciones con el match case
# una vez validada llamamos a cada funcion
#salir 
opcion=input("elegir una opcion")


case "1":
 agregar_estudiante()
case "2":
  mostrar_estudiantes()
case "3":
  eliminar_estudiante()
case "4":
  buscar_estudiante()
case "5":
  verificar_palabra()
case "6":
  print("Saliendo del programa.")
  break
case _:
   print("Opcion invalida")

menu()
