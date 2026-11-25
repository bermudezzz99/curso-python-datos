
#ciclo for 

guias = ["G001", "G002", "G003", "G004", "G005"]

for memoria in guias:
 print("Revisando envios:", memoria)

 #for+range

 for consecutivo in range (2):
   print("Revisando envio:", guias[consecutivo])

# contadores

contador = 0

for guia in guias:
    contador += 1
    print("revisando", guia)

print("total:", contador)

#acumulador de kilometros 

distancias = [15, 22, 10, 18]

distancia_total = 0

for km in distancias:
  distancia_total += km 

print ("distancia total", distancia_total)

#ciclo while 

envios = [
  {"estado": "Entregado"},
  {"estado": "En ruta" },
  {"estado": "Devuelto"},
  {"estado": "Entregado"},
  {"estado": "Devuelto"},
  {"estado": "Entregado"}
  ]

entragados = 0
en_ruta = 0
devueltos = 0 

for envio in envios:
  
  if envio["estado"] == "Entregado":
    entragados += 1

  elif envio ["estado"] == "En ruta":
    en_ruta += 1

  else: 
    devueltos += 1


    #Mostrar resultados 
print("RESUMEN DE ENVIOS")
print("Entregados:", entragados)
print("En ruta:", en_ruta)
print("devueltos:", devueltos)