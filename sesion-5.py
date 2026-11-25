#Sesion 5

#Diccionarios

Televisores = {
    "Marca": "Samsung",
    "Precio":5400000,
    "pulgadas": 55,
    "color": "Negro",
    "resolucion": "4K" }

print(Televisores["Marca"])
print(Televisores["Precio"])
print(Televisores["pulgadas"])
print(Televisores["color"])
print(Televisores["resolucion"])

#Consultar informacion get
#corchetes

print(Televisores.get("Disponible"))
print(Televisores.get("Precio"))
print(Televisores.get("pulgadas"))

#Agregar informacion

Televisores["Disponible"] = True
print(Televisores)

#modificar informacion 

Televisores["Precio"] = 6000000
print(Televisores)

#Eliminar informacion 

del Televisores ["Disponible"]
print  (Televisores)

#Consultar grupos de datos

print (Televisores.keys())
print (Televisores.values())
print (Televisores.items())

#Coleccion de registros 

electrodomesticos_cocina = [
    {
        "producto":     "microhondas",
        "marca": "LG",
        "litros": 25,
        "color": "Blanco",
        "disponible": True
    },
    {
        "producto":     "horno",
        "marca": "Samsung",
        "litros": 30,
        "color": "Negro",
        "disponible": True
    }
]

print (electrodomesticos_cocina[0]["marca"])
print (electrodomesticos_cocina[1]["marca"])

#actividad 

producto_1 = {
    "codigo": "P001",
    "nombre": "Cuaderno",
    "precio": 4500,
    "categoria": "Papelería",
    "marca": "Norma",
    "stock": 20,
    "descuento": 10
}

producto_2 = {
    "codigo": "P002",
    "nombre": "Mouse",
    "precio": 35000,
    "categoria": "Tecnología",
    "marca": "Logitech",
    "stock": 8,
    "descuento": 5
}

producto_3 = {
    "codigo": "P003",
    "nombre": "Teclado",
    "precio": 65000,
    "categoria": "Tecnología",
    "marca": "Logitech",
    "stock": 5,
    "descuento": 15
}

inventario = [producto_1, producto_2, producto_3]

print("Primer producto:", inventario[0]["nombre"])
print("Precio:", inventario[0]["precio"])
print("Stock:", inventario[0]["stock"])

inventario[0]["precio"] = 5000

print("Nuevo precio:", inventario[0]["precio"])

canales = {"instagram", "facebook", "Tiktok"}
print(canales)

#Agregar un canal 
canales.add("Linkedin")
print(canales)

#comprobar si un canal existe
print("instagram" in canales)
print("Twitter" in canales)

#Unir conjuntos 

campania_a = {"Instagram", "Facebook", "TikTok"}
campania_b = {"Linkedin", "Youtube", "TikTok"}

campania_c = campania_a | campania_b
print(campania_c)

campania_d = campania_a &  campania_b
print(campania_d)

campania_e = campania_a - campania_b
print(campania_e)