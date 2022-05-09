#Por Danilo Castaño Puerto - miércoles, 4 de mayo de 2022, 11:08

articulo = (input("Ingrese el nombre del articulo: "))
valor = float(input("Ingrese el valor del articulo: "))
cantidad = int(input("Ingrese el numero de unidades del articulo ingresado: "))
iva = 0.19
precio_bruto = valor + (valor*iva)
factura = precio_bruto * cantidad

print(f"El artículo {articulo} tiene un valor de {precio_bruto} (IVA incluido)")

if precio_bruto > 500000:
    factura = factura - (factura*0.065)
    print(f"FELICIDADES! Su compra tiene el 6.5% de descuento; el valor a pagar es {factura}")
else:
    print(f"El valor de su factura es: $ {factura}")
print("Gracias por su compra")