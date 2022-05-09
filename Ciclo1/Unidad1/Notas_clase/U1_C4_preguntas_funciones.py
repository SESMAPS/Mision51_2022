#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Creado por  : davoc
# En : Reto 1 ciclo 1 mision tic 2022. 7 Mayo 2022 
# # version ='1.0' VsCodium
#Dudas sobre funciones de la presentación


def imprime_Cosas():
    print("La clase esta genial")
    print('Python es lo máximo')

imprime_Cosas() # aqui se llama a la funcion?

def repetir_funciones():
        print("\n")
        imprime_Cosas() # esta sería una variable dentro de la nueva funcion y no tiene que corresponder a la variable con el mismo nombre que se definio antes?
        imprime_Cosas()

def repetir_funciones():
    print("\n")
    imprime_Cosas()
    imprime_Cosas()
    repetir_funciones()

#repetir_funciones()

def imprime_Cosas():
    print("La clase esta genial")
    print('Python es lo máximo')
    
def otra_suma(numero1, numero2):
    print(numero1 + numero2)
    print("\n")
    
resultado = otra_suma(5,6)
print(resultado)
    
##########

def sumarDosnumeros(): # porque no se incluyen los parametros?
    num1 = float(input("Ingrese el numero 1: "))
    num2 = float(input("Ingrese el numero 2: "))
    print("la suma de", int(num1), " + ", int(num2)) # porque un print y no un return? cuando usar uno o el otro?

sumarDosnumeros()


def raizCuadrada():
    valor = float(input("Por favor, ntroduzca un numero a calcaluar su raiz cuadrada: "))
    raiz = valor ** 0.5
    return print("La raiz cuadrada de : ", valor, " es ", valor ** 0.5)
raizCuadrada()
