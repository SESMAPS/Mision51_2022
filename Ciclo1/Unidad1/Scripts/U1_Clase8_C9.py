#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Creado por  : davoc
# Tema: Clase 8 no se escribio codigo. Clase 9. Parte 1. 
# Para: mision tic 2022. 16 Mayo 2022 
# # version ='1.0' VsCodium

""" programa que le pregunte al usuarii (profesor) el nombre del alumno, el numero de notas
que desea ingresar y los porcentajes correspondientes a cada una de ellas.
Posteriormente, de acuerdo con el numero de notas deseado, el programa debe preguntar al usuario el valor de cada una
de esas notas, para finalmente desplegar en pantalla el informe completo de notas del estuciante,
así (teniendo en cuenta que aprueba el curso con una nota mayor o igual a 3.0):
Nombre del estudiante: xxxx
Nota No. n: X.X
.
.
.
Nota final: X.X
Aprueba: Si/No
Ej: Si son 2 notas: {'nombre': 'Juanito',0: 3.5, 'porcentaje_0':50,1: 4.0, 'porcentaje_1':50} """
#En los diccionarios no se almacenan por orden jerargico. Y las etiquetas pueden ser número directamente 0: 1.1
#La etiqueta no indica orden.

datos = {}
datos['nombre'] = str(input("Ingrese el nombre del alumno: ")) #Almacenamos directamente la entrada del usuario
num_notas = float(input("¿Cuantas notas tiene el alumno?: "))
#Debemos crear un cilo para que itere hasta num_notas. Llevando  la cuenta

contador_notas = 0
while contador_notas < num_notas:
    datos[contador_notas] = float(input(f"Ingrese la nota {contador_notas+1}: "))
    etiqueta_porcentaje = 'porcentaje_' + str(contador_notas) #a
    datos[etiqueta_porcentaje] = float(input("Ingrese el porcentaje correspondiente a esta nota: "))#b
    contador_notas = contador_notas + 1 #O escribirla asi: contador_notas += 1
    #datos[f'porcentaje_{contador_notas}'] = float(input("Ingrese el porcentaje de la nota: "))
    #Esta es otra forma, para ahorrarnos una linea de a y b , ingresando directamente en la equita al preguntar

#Ahora vamos a calcular la nota final
contador_notas = 0
while contador_notas < num_notas:
    etiqueta_porcentaje = 'porcentaje_'+str(contador_notas)
   #datos['nota_final'] = datos['nota_final'] + datos[contador_notas] * datos[porcentaje_+str(contador_notas)]/100
    datos['nota_final'] = datos['nota_final'] + datos[contador_notas] * datos[etiqueta_porcentaje]/100 #FIXME: Falla en esta linea
    contador_notas += 1

if datos['nota_final'] >= 3.0:
    datos['Aprueba'] = "Si"
else:
    datos['Aprueba'] = "No"

#Ahora imprimimos el informe
print(f"Nombre del estudiante: {datos['nombre']}")

for i in range(0, num_notas):#va a ir desde el 0,1,2,3..
    print(f"Nota No. {i+1} : {datos['i']}") # en ciclo for , datos que tengo guardado con la etiqueta 0 que viene siendo 0 o 1 ,,,

print(f"Nota final: round{datos['nota_final']},2") #con round redondeo 
print(f"Aprueba: {datos['Aprueba']}")
