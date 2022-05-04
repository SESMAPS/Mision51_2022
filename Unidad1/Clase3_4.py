#!/usr/bin/env python3  Line 1
# -*- coding: utf-8 -*- Line 2
#----------------------------------------------------------------------------
# Created By  : Cristian ospina
# Created: Clase 3 ciclo 1 mision tic 2022. Parte 4 , Ejercicio de salario
# version ='1.0'
"""
Created on Tue May  3 13:31:38 2022

@author: davoc
"""
#Calcular y mostrar el valor a pagar por un trabajador, teniendo en cuenta que gana un salario basico x con 
#una carga de horas semanales de 40 horas por el salario basico. Las horas adicionales tienenun valor de 1.5 veces
#la tasa normal- Se debe preguntar al usuario cual es el valor del salario basico y cuantas horas trabajo el empleado.
#Adicionalmente si el salario basico es de menos de $1.000.000, se le debe pagar un auxilio de transporte de $70.000=
#En caso de que la persona trabaje menos de las 40 horas, se le debe pagar el salario basico completo, incluyendo
#el salario basico completo, incluyendo el auxilio de transporte si tiene derecho.


basico = float(input("Ingrese el salario basico del empleado: "))
horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
horas_extras = 0
auxilio_transporte = 0
valor_total_horas_extras = 0
valor_hora_ordinaria = basico /40

if horas_trabajadas > 40:
    horas_extras = horas_trabajadas -40
    valor_total_horas_extras = horas_extras * valor_hora_ordinaria * 1.5

if basico < 1000000:
    auxulio_transporte = 70000

valor_pago = basico + valor_total_horas_extras + auxilio_transporte

print(f"El valor total a pagar al empleado es: {valor_pago}")
print(valor_hora_ordinaria)