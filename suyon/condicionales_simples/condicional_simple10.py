import os
#calcular la compra de gasolina por galones de un vehiculo pesado el grifo Primax

#input
compra1=int(os.sys.argv[1])
compra2=int(os.sys.argv[2])
compra3=int(os.sys.argv[3])

#processing
compra_total=compra1+compra2+compra3

#verificador
verificador=compra_total>=300

#output
print("#################################")
print("# BOLETA DE GALONES (PRIMAX)")
print("#################################")
print("#compra1:",compra1)
print("#compra2:",compra2)
print("#compra3:",compra3)
print("#compra total:",compra_total)
print("########################################")

#condicional simple
#si la compra total>300 mostrar, felicitaciones ganaste un celular nokia 2.1
if(verificador==True):
    print("felicitaciones , ganaste un celular nokia 2.1")
#fin_if
