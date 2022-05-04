#Por  Johnatan David Caicedo Valencia - martes, 3 de mayo de 2022, 20:09

valor= float(input("ingrese el precio del producto: "))

unidades= float(input("ingrese cantidad que lleva: "))

iva= (valor*0.19)

iva_total= (iva*unidades)

precio_bruto= valor*unidades

valor_bruto= (precio_bruto+iva_total)


if valor_bruto > 500000:

    print(f"el valor sin descuento es: {valor_bruto}")

    descuento=(0.65*valor_bruto)

    print(f"pero con el descuento es: {descuento}")

else:

    print(f"total a pagar: {valor_bruto}")

    

print("feliz dia")