#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Creado por  : davoc
# En : Clase 6 Ciclos, ejemplos ciclo 1 mision tic 2022. 9 Mayo 2022 
# # version ='1.0' VsCodium

#Si quiero escribir un programa que pregunte al usuario un número y le diga si es un primo o no

numero = int(input("Ingrese un número: "))
canditad_divisores = 0

x = 2
while x < numero:  #porque es menor al anterior que la persona, no justo en el limite
    if numero % x == 0:
        canditad_divisores = canditad_divisores + 1
    x = x +1
if canditad_divisores >0 or numero < 2:# o < 1El or lo uso por la consideración especial
    print("Bro el número no es primo")
else:
    print("Bro el número es primo")


#Si quiero escribir un programa que pregunte sucesivamente al usuario un número mayor que cero y le diga si es un primo o no
#Si el usuario digita 0, el programa debe terminar
#https://www.youtube.com/watch?v=HiXLkL42tMU&t=1064s

numero = 1
while numero != 0:
    numero = int(input("Ingrese un número (para temrinar ingrese 0): ")) #lo ponemos aqui porque queremos que se repita esta pregunta, por eso no esta fuera del while
    if numero ==0:
        print("Fin del programa")
    else:
        canditad_divisores = 0
        x = 2
        while x < numero:  #porque es menor al anterior que la persona, no justo en el limite
            if numero % x == 0:
                canditad_divisores = canditad_divisores + 1
            x = x +1
        if canditad_divisores >0 or numero < 2:# o < 1El or lo uso por la consideración especial
            print("Bro el número no es primo")
        else:
            print("Bro el número es primo")