#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Creado por  : davoc
# Tema: Clase 10 Nuevo tema . Parte 1 Estructura de datos, listas.
# . 
# Para: mision tic 2022. 16 Mayo 2022 
# # version ='1.0' VsCodium
#En las listas los datos estan ordenados, y no tienen etiquetas, se hacen con un []

lista_vacia = []
lista_numeros = [1,2,3,4,5,6,7,8,9,10]

lista_numeros2 = [9,8,7,6,5,4,3,2,1]
# la lista 1 y lista 2 son diferentes.
#La longitud del lista es la cantidad de elementos que tiene la lista, 
#Pero la posicion o indice siempre va desde 0 hasta la longitud max - 1
#osea estan ubicados en la posicion de 0 a 24

#Para acceder a los elementos de la lista
#va, el nombre seguido de [] dentro se pone el indice del elemento
lista_numeros[5]  # esto nos arrojaria el 6 .variable con el indice
lista_numeros[5] = 20 # aqui estariamos actualizando el valor en esa posicion

print(lista_numeros[9])

lista_datos = ['Maria','18/05/2022',3000,2000,5000,20000,14000,750]

lista_datos.insert(2,50000)
print(lista_datos)

if 2000 in lista_datos:
    lista_datos.remove(2000)
print(lista_datos)  

lista_datos.pop(0)
print(lista_datos)

posicion_fecha = lista_datos.index('18/05/2022')
print(posicion_fecha)

print(len(lista_datos))





#para que es que se usa el : en una lista?



