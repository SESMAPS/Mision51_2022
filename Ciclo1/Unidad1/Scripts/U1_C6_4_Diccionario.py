#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Creado por  : davoc
# En : Clase 5. Parte 4 . Diccionarios mision tic 2022. 9 Mayo 2022 
# # version ='1.0' VsCodium
# Programa para escribir en pantalla los números de 1 al 10:
# El corchete indica que es un diccionario

datosusuario = {"Nombre":"Ana", "Apellido":"López","Teléfono":3333333,"Estatura":1.60,"Casado":True,"Edad":30} #La primera es la etiqueta, la segunda es el dato a almacenar
nacimiento = 2022 - datosusuario["Edad"] # Calculo aproximado de edad

print(str(nacimiento) + "Se llama: " + datosusuario["Nombre"])

#Si queremos sobre escribir el nombre de Ana usamos:
datosusuario["Nombre"] = "Diana"

print(f"Hola : {datosusuario["Nombre"]} {datosusuario["Apellido"]}, su año aproximado de nacimiento es: {nacimiento}")
    """Cuando estamos trabajando con estructuras de datos, es muy util plantear 
    los ciclos for. 
    """

for key in datosusuario: # para una variable de control "key" en el diccionario, a la variable key le voy asignando cada valor de lo que tengo en el diccionario
    #y asi va iterando uno a uno, recorriendo todo el dicc. El toma es el nombre de la etiqueta mas no del valor.
    #ejemplo, la key va a tomar nombre, y  luego imprime el valor almacenado en nombre.
    print(datosusuario[key])
