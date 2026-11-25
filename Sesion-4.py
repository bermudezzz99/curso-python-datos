
#Consultar cadenas de texto 

producto = "Camiseta"
print(producto[0]) #C
print(producto[1]) #a
print(producto[2]) #m
print(producto[3]) #i
print(producto[4]) #s
print(producto[5]) #e       
print(producto[6]) #t
print(producto[7]) #a

# f strings  construir mensajes con variables

print(f"El producto es: {producto}")

# posiciones negativas y positivas
print(producto[0]) 
print(producto[-2]) 

#Extraer partes de una cadena de texto
print(producto[0:4]) #Cami
print(producto[4:]) #seta

#longitud de una cadena de texto
producto = "memoria ram 16gb"
longitud = len(producto)
print("La longitud de la cadena es:", longitud)

#metodos de cadenas de texto
# convertir a mayusculas

producto = "memoria ram 16gb"
print(producto.upper()) 
print(producto.lower())
print(producto.capitalize())
print(producto.replace("ram", "ROM"))
print(producto + " es un componente de computadora")
print(producto.split(" "))
print(producto.strip())

#Limpiar base de datos

nombre = "   OWEN STEVEN BERMUDEZ ARIAS    "
print(f"El nombre del clientes es: {nombre.strip().title()}")

#actividad 
nombres = [" MARIA GOMEZ ", "juan perez", " ANA LOPEZ "]

print(nombres[0].strip().title())
print(nombres[1].strip().title())
print(nombres[2].strip().title())

#listas 

listas = ["Camiseta", "Pantalón", "Zapatos", "Sombrero"]
print(listas)

#Agregar elementos a la lista
listas.append("Chaqueta")
print(listas)

#Insertar elementos en una posición especifica
listas.insert(2, "Bufanda")
print(listas)   

#Eliminar elementos de la lista
listas.remove("Zapatos")
print(listas)

#Borrar posiciones de la lista
del listas[1]
print(listas)

# ordar por orden alfabetico
listas.sort()
print(listas)

# ordar por orden alfabetico inverso
listas.sort(reverse=True)
print(listas)

listas2 = ["Gorra", "Guantes", "Esqueleto", "Cinturon", "Saco"]
listas3 = listas + listas2
print(listas3)

#convertir una lista en una cadena de texto
cadena  = "camiseta, pantalón, zapatos, sombrero"
lista4 = cadena.split(", ")
print(lista4)

# contar
print(len(lista4))

# lista de actividad maarketing 
clics = [120, 150, 180, 140, 200]

print("Lista inicial:", clics)

print("Clics del primer dia:", clics[0])

clics[1] = 160
print("Despues de modificar:", clics)

clics.append(220)
print("Despues de agregar:", clics)

clics.remove(180)
print("Despues de eliminar:", clics)

clics.sort()
print("Despues de ordenar:", clics)

#tuplas
ubicaciones_geograficas = ("latitud", "longitud", "altitud")
print(ubicaciones_geograficas)

coordenadas = (4.7110, -74.0721, 2600)
print(coordenadas)

estadistica_media = (10, 20, 30, 40, 50)
print(estadistica_media)

datos_personales = ("nombre", "cedulla", "edad", "apellidos")
print(datos_personales)
