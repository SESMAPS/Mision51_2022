#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Creado por  : davoc
# Tema: Clase 7. Ejemplos usando Diccionarios.
# Para: mision tic 2022. 11 Mayo 2022 
# # version ='1.0' VsCodium

# Programa que le pide al usauario ingresar el nombre y las 3 notas de un estudiante
# Posteriormente, el  Programa mostrará en pantalla el nombre del estudiante, las 3 notas, la nota final y 
# si el estudiante aprueba la materia o no
#Para el calculo de la nota final, la nota1 tiene un porcentaje del 30%, la nota 2 del 40%,
#y la nota 3 del 30%


info_Estudiante = {}

info_Estudiante['Nombre'] = input("Ingrese el nombre del estudiante: ")
info_Estudiante['Nota1'] = float(input("Ingrese la primera nota: "))
info_Estudiante['Nota2'] = float(input("Ingrese la segunda nota: "))
info_Estudiante['Nota3'] = float(input("Ingrese la tercera nota: "))

info_Estudiante['NotaFinal'] = info_Estudiante['Nota1'] * 30/100 + info_Estudiante['Nota2'] * 40/100 + info_Estudiante['Nota3'] * 30/100

if info_Estudiante['NotaFinal'] > 3:
    info_Estudiante['Aprueba'] = 'SI' #Con esto tambien creamos una nueva etiqueta dentro del dicc
else:
    info_Estudiante['Aprueba'] = "NO"

for etiqueta in info_Estudiante:
    print(f"{etiqueta} : {info_Estudiante[etiqueta]}")

# Tips de vcode https://www.udemy.com/course/vscode-mejora-tu-velocidad-para-codificar/
#Ahora queremos hacerlo pero con una funcion que nos devuelva un nuevo diccionario

def calculo_final(info:dict):
    info['NotaFinal'] = info['Nota1'] * 30/100 + info['Nota2'] * 40/100 + info['Nota3'] * 30/100

    if info['NotaFinal'] > 3:
        info['Aprueba'] = 'SI'
    else:
        info['Aprueba'] = "NO"
    return info

datos_Finales = calculo_final(info_Estudiante)

for etiqueta in datos_Finales:
    print(f"{etiqueta} : {datos_Finales[etiqueta]}")

