#sesion 6

#if

# cantidad_productos = 3
# if cantidad_productos <= 3:
#     print("Bajo nivel de inventario")

#     #If-else
#     Total_compra = 150000
# if Total_compra >= 100000:
#     print("Descuento autorizado")
# else:
#     print("Descuento no autorizado")

#     #Actividad 
#     #Ventas 

# clics = 2000
# if clics >= 1000:
#     print("Meta alcanzada")
# else:
#     print("Meta pendiente")

#     #educacion

# nota = 4.5
# if nota >= 3.0:
#     print("Alcanza el criterio")
# else:
#     print("Requiere refuerzo")

#     #Administracion 

# minutos = 10
# if minutos > 20:
#     print("Priorizar atención")
# else:
#     print("Continuar proceso")

#     #desiciones 

# cantidad = 2

# if cantidad == 0:
#     print("Agotado")
# elif cantidad <= 1:
#     print("Inventario bajo")
# else:
#     print("Disponible")

#     cantidad = 4

# if cantidad == 0:
#     print("Producto Agotado")
# elif cantidad <= 5:
#     print("Inventario bajo")
# else:
#     print("Producto disponible")

# # IF ejercicio 
# total_compras_realizadas = 150000
# clientes_frecuentes = True

# if total_compras_realizadas >= 10000 and clientes_frecuentes:
#     print("Descuento autorizado por Owen")
# else:
#     print("No cumple las condiciones")

    
# Lista de vehiculos

flota = [
    {"codigo": "V-101", "kilometraje": 320},
    {"codigo": "V-102", "kilometraje": 780},
    {"codigo": "V-103", "kilometraje": 1250},
    {"codigo": "V-104", "kilometraje": 1680},
    {"codigo": "V-105", "kilometraje": 450},
    {"codigo": "V-106", "kilometraje": 920},
    {"codigo": "V-107", "kilometraje": 1420},
    {"codigo": "V-108", "kilometraje": 1850},
    {"codigo": "V-109", "kilometraje": 610},
    {"codigo": "V-110", "kilometraje": 1100},
    {"codigo": "V-111", "kilometraje": 250},
    {"codigo": "V-112", "kilometraje": 1550}
]


# Contadores

uso_reciente = 0
seguimiento = 0
programar_revision = 0
prioridad_alta = 0

total_kilometros = 0


# Recorrer los vehiculos

for vehiculo in flota:

    codigo = vehiculo["codigo"]
    kilometraje = vehiculo["kilometraje"]

    total_kilometros = total_kilometros + kilometraje

    if kilometraje < 500:
        categoria = "Uso reciente"
        uso_reciente = uso_reciente + 1

    elif kilometraje < 1000:
        categoria = "Seguimiento"
        seguimiento = seguimiento + 1

    elif kilometraje < 1500:
        categoria = "Programar revision"
        programar_revision = programar_revision + 1

    else:
        categoria = "Prioridad alta"
        prioridad_alta = prioridad_alta + 1

    print(codigo, "-", kilometraje, "km -", categoria)


# Calcular promedio

promedio = total_kilometros / len(flota)


# Mostrar resultados

print("\nRESUMEN")

print("Uso reciente:", uso_reciente)
print("Seguimiento:", seguimiento)
print("Programar revision:", programar_revision)
print("Prioridad alta:", prioridad_alta)

print("Total kilometros:", total_kilometros)
print("Promedio:", promedio)

