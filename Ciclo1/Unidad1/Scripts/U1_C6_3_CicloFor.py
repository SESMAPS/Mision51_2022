#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Creado por  : davoc
# En : Clase 6 Ciclos, ciclo FOR. mision tic 2022. 9 Mayo 2022 
# # version ='1.0' VsCodium


#en los ciclos for siempre debera ir la variable de control,. y va a ir cambiando de valores, sea incrementando o decreciendo según el rango
# en estos rangos el primero numero esta incluido, el segundo no. 

for i in range(1,10):
    print(i)

for i in reversed(range(1,10)): #Aqui se imprimen los numeros del 10 al 1. El range se respeta
    print(i)

#Ahora si lo queremos hacer con un ciclo while
i = 10
while i >= 1:
    print(i)
    i = i - 1
