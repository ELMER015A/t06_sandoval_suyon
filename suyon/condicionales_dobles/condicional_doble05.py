import os
#calcular el volumen de la piramide

#input
area_base_de_la_piramide=float(os.sys.argv[1])
altura=float(os.sys.argv[2])

#processing
volumen_piramide=(area_base_de_la_piramide*altura)/3

#verificador
verificador=(volumen_piramide>21)

#output
print("##################################################")
print("#       BOLETA DEL VOLUMEN DE UNA PIRAMIDE   #")
print("##################################################")
print("#datos")
print("#area de la base de la piramide:",area_base_de_la_piramide)
print("#altura:",altura)
print("#volumen de la piramide:",volumen_piramide)
print("###################################################")

#condicional doble
#si el volumen de la piramide>21 mostrar , es aceptable el volumen
if(verificador==True):
    print("es aceptable el volumen")
else:
    print("no es aceptable el volumen")
