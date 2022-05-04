#Kristian Danilo Rincón González - martes, 3 de mayo de 2022, 20:23
print("Bienvenido aqui conoceras el precio total de los articulos")
v_art = float(input("Ingrese el valor del articulo que desea comprar: "))#sin iva
cantidad = int(input("Ingrese la cantidad de articulos que desea: "))

iva = v_art * cantidad * 0.19
precioB = v_art * cantidad + iva

if (precioB > 500000):
    conDescuento = 6.5 * precioB / 100
    print("Felicidades! tiene un descuento del 6.5% por su compra :)")
    print(f"el valor total a pagar es: ${precioB - conDescuento}")
else:
    print(f"El valor total a pagar es: ${precioB}")
    print("Gracias por su compra")