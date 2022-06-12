#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Creado por  : davoc
# Tema: Clase 19  Método INIT (semana7)
# Para: mision tic 2022. 08 Junio 2022 
# # version ='1.0' VsCodium

class Vehiculo():
    color = "blanco"
    num_llantas = 4
    cilindraje = 1000
    placa = ""
    capacidad_tanque  = 20 # capacidad del tanque de combustible en litros
    
    #Método constructor : se ejecuta siempre que instancio la calse (siempre que creo un objeto de la clase vehiculo):
    #init se encarga de construir el objeto, aqui lo definimos explicito, para que reciba unos parametros
    #siempre que hagamos una clase debemos tener el constructor,
    def __init__(self,color,cilindraje,placa,capacidad_tanque ):
        self.color = color
        self.cilindraje = cilindraje
        self.placa = placa
        self.capacidad_tanque = capacidad_tanque
        
    def avanzar(self):
        print("Vehiculo avanzando")
    
    def frenar(self):
        print("El vehiculo se ha detenido")
    
    def entregar_valor(self):
        atributos ={"color": self.color,
                    "num_llantas": self.num_llantas,
                    "cilindraje": self.cilindraje,
                    "placa": self.placa,
                    "capacidad_tanque": self.capacidad_tanque,
                    "velocidad_maxima": self.velocidad_maxima                  
                    }
        return atributos
    
micarrito = vehiculo() #Aca estamos instanciando la clase vehiculo (estamos creando un objeto de la clase vehiculo)
carrito = vehiculo("rojo",1200,"ABC123",25)

carrito.avanzar()
carrito.frenar()

print(micarrito.)