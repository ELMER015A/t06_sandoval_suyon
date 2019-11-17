import os
# clacular el numero de ventas
#input
trabajador=os.sys.argv[1]
venta1=float(os.sys.argv[2])
venta2=float(os.sys.argv[3])
venta3=float(os.sys.argv[4])

#processing
total_de_ventas_al_dia=(venta1+venta2+venta3)

#verificador
verificador=total_de_ventas_al_dia>520

#ouput
print("####################################")
print("# VENTAS DEL DIA ")
print("#######################################")
print("#trabajador:",trabajador)
print("venta1:",venta1)
print("#venta2:",venta2)
print("#venta3:",venta3)
print("#total de ventas al dia:",total_de_ventas_al_dia)
print("##############################################")

#condicional simple
#si el total de ventas>520 mostrar, ganaste 20 soles adicionales
if(verificador==True):
    print("ganaste 20 soles adicionales")
#fin_if
