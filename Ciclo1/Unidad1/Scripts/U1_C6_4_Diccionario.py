#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Creado por  : davoc
# En : Clase 6 y clase 7. Parte 1. Diccionarios mision tic 2022. 11 Mayo 2022 
# # version ='1.0' VsCodium

# El corchete indica que es un diccionario
#Poner mucho cuidado con el uso de las comillas, si cosas dentro de diccionario es ', en los print va la doble ""

datosUsuario = {'Nombre':'Ana', 'Apellido':'López','Teléfono':3333333,'Estatura':1.60,'Casado':True,'Edad':30} #La primera es la etiqueta, la segunda es el dato a almacenar
nacimiento = 2022 - datosUsuario['Edad'] # Calculo aproximado de edad

print(str(nacimiento) + 'Se llama: ' + datosUsuario['Nombre'])

#Si queremos sobre escribir el nombre de Ana usamos:
datosUsuario['Nombre'] = 'Diana'

print(f"{datosUsuario['Nombre']} {datosUsuario['Apellido']}, su año de nacimiento es: {nacimiento}")

'''Cuando estamos trabajando con estructuras de datos, es muy util plantear 
    los ciclos for. 
    '''

for key in datosUsuario: # para una variable de control 'key' en el diccionario, a la variable key le voy asignando cada valor de lo que tengo en el diccionario
    #y asi va iterando uno a uno, recorriendo todo el dicc. El toma es el nombre de la etiqueta mas no del valor.
    #ejemplo, la key va a tomar nombre, y  luego imprime el valor almacenado en nombre.
    print(datosUsuario[key])

for key in datosUsuario: 
       print(f"{key} : {datosUsuario[key]}")  #ahora yo quiero que tambien me imprima la etiqueta
