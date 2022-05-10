#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Creado por  : davoc
# En : Clase 5 Ciclos ciclo 1 mision tic 2022. 9 Mayo 2022 
# # version ='1.0' VsCodium
# Programa para escribir en pantalla los números de 1 al 10:

x = 1
while x <= 10: #Un while es un Mientras en psudocodigoAqui definimos el limite hasta donde llegará
    print(x)
    x = x + 1 #Cuando hacemos un while tenemos que asegurarnos que la variable de control siga aumentando, para poder que acabe en algun momento

y = 1
while y <= 10: # Generalmente tenemos una variable de control. Pero no siempre estará
    print(y)
    y = y + 2 #Imprime numeros pares

z = 9
u = 1

while z <= 90: 
    print(f"Multiplicar 9 por {u + 1} da como resultado: {z}") # si uso + para concatenar ejemplo + str(z) iria despues de ""final, si está dentro de comilla es {}
    z = z + 9

a = 1
while a <= 90: # Si se hace así funciona diferente. 
    a = a + 9
    print(a)