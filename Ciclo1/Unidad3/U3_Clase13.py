#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Creado por  : davoc
# Tema: Clase 13  Herramientas del lenguaje
# Para: mision tic 2022. 25 Mayo 2022 
# # version ='1.0' VsCodium
#Operadores especiales para simplificar la iteracion dentro de objetos en lugar de recorrerlos con ciclos for

#Operador Lambda - definir unas funciones "desechables" de una forma rapida indicar que hacer con ese 
#conjunto de datos . Pero lambda debe ser para funciones cortas, una sola instrucción
# Sintaxis lambda argumentos : expresion (debe ser una sola instrucción)
#ejemplo: 

def suma(x,y):
    return x+y

f = lambda x,y: x+y #ya está implicito el return
print(f(3,5)) #Aqui le pasamos parametros a la función.

a = lambda s,t: s*t
print(a(5,8))

raiz = lambda x,y: x**y
print(raiz(3,4)) 

r = lambda x: round(x,2)
print(r(5.5678))

promedio = lambda x,y,z : (x+y+z)/3
print(round(promedio(5,3.4,2.3),2))
print(promedio(5,3.4,2.3))

m = lambda palabra: palabra.upper()
print(m("hola mazorca"))


#Operador map : Recibe como parametros de entradas una función y un iterable (set(parecida a tupla,pero no hay elementos repetidos, y no tienen orden),diccionario, lista, tupla)
# Sirve para ejecutar una funcion usando como parametro de entrada cada unos
# de los valores del iterable
#
def por5(numero):
    return numero*5

numeros = [1,7,26,90,15,14,18]

resultado = list(map(por5,numeros)) #aqui quedaria dentro de una lista o tupla si se pone tuple
print(resultado)

#Como lo hariamos antes
for i in range(0, len(numeros)):
    resultado = []
    resultado.append(por5(numeros[i])) #para agregar al final de la lista, si es par insertar es con insert y darle el indice donde va a quedar
    return resultado




    
    

