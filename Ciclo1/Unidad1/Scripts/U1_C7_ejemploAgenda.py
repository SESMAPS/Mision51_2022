#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Creado por  : davoc
# Tema: Clase 7. Ejemplo de agenda de contactos usando Diccionarios.
# Para: mision tic 2022. 11 Mayo 2022 
# # version ='1.0' VsCodium

#Programa que crea una agenda de contactos y permite al usuario agregar un contacto
#buscarlo, eliminarlo, o listar todos los contactos

#opcion 1 : un dicc con etiqueta nombre y valor telefono, otro, seria juan telefono 123
# {'Juan':123, 'Pedro':323 , 'Diana':4545}
# Opcion 2 , un diccionario dentro de otro dicc
# {1:{'Nombre':'Juan', 'Telefono':123}, 2:{'Nombre':'Pedro', 'Telefono':6544}}

#el .key comprueba dentro de un dict si existe el valor que yo le estoy pasando Pero hay que poner mucho cuidado como se quiere consultar
#En algun caso es mejor usar el get. #https://devcode.la/tutoriales/diccionarios-en-python/ https://www.delftstack.com/es/howto/python/python-check-if-value-in-dictionary/

agenda = {}
opcion = 1
while opcion != 5:
    opcion = int(input(""""Elija una opcion:
                        1. Agregar un contacto
                        2. Buscar un contacto
                        3. Eliminar un contacto
                        4. Ver todos los contactos guardados  
                        5. Salir                           
                    """))
    if opcion == 1: #El usuario quiere agregar un contacto
        nombre = input("Ingrese el nombre del nuevo contacto: ")
        agenda[nombre] = input(f"Ingrese el teléfono del contacto de {nombre}: ")
    elif opcion == 2:
        nombre = input("Ingrese el nombre del contacto que des1ea buscar: ")
        if agenda.get(nombre) != None: #FIXME: se arregló la consulta, el metodo es get en lugar de key, o fromkeys-
            print(f"{nombre} : {agenda[nombre]}")
        #if nombre in agenda: # note: esta es otra forma de consultar.
        #    print(f"{nombre} : {agenda[nombre]}")
        #else:
        #    print("No existe un contacto con ese nombre")
        else:
            print("No existe un contacto con ese nombre")
    elif opcion == 3:
        nombre = input("Ingrese el nombre del contacto que1 desee eliminar: ")
        if agenda.fromkeys(nombre) != None:
            del agenta[nombre]
        else:
            print("No existe un contacto con ese nombre !")
    elif opcion == 4:
        for key in agenda:
            print(f"{key} : {agenda[key]}")
