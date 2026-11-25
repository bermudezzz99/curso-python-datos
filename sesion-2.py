# Sesion 2
# ctrl+# Para comentar una linea 
# Ctrl+/ para comentar varias lineas
# print("Hola mundo")

# programa de bienvenida
# print("Bienvenido al curso de Python")
# nombre = input("Ingrese su nombre: ")
# print("Bienvenido", nombre)

# concatenar el nombre con un mensaje
# mensaje = "Bienvenido " + nombre + " al curso de Python"
# print(mensaje)

# variables
# edad= input("Por favor ingrese su edad: ")
# print("Su edad es:", edad)

# expresiones y combinaciones 
# edad = int(edad) #convertir a entero
# edad = edad * 2 
# print("Su edad multiplicada por 2 es:", edad)

# Registro de una venta

# producto = input("Ingrese el producto: ")
# cantidad = int(input("Ingrese la cantidad: "))
# precio_unitario = int(input("Ingrese el precio unitario: "))

# total = cantidad * precio_unitario

# print("Producto:", producto)
# print("Cantidad:", cantidad)
# print("Precio unitario:", precio_unitario)
# print("Total de la venta:", total)

# Información de la actividad formativa

actividad = input("Curso de análisis de datos") 
cupos = int(input("Ingrese el número de cupos disponibles: "))
duracion_horas = float(input("Ingrese la duración en horas: "))
requiere_inscripcion = bool(input("¿Requiere inscripción? (True/False): "))


print("Nombre de la actividad:", actividad)
print("Cupos disponibles:", cupos)
print("Duración en horas:", duracion_horas)
print("¿Requiere inscripción?:", requiere_inscripcion)


print("Tipo de actividad:", type(actividad))
print("Tipo de cupos:", type(cupos))
print("Tipo de duración:", type(duracion_horas))
print("Tipo de inscripción:", type(requiere_inscripcion))