import os
#clacular la compra mensual en un supermercado
#input
compra_semana_1=int(os.sys.argv[1])
compra_semana_2=int(os.sys.argv[2])
compra_semana_3=int(os.sys.argv[3])
compra_semana_4=int(os.sys.argv[4])

#processing
compra_mensual=(compra_semana_1+compra_semana_2+compra_semana_3+compra_semana_4)

#verificador
verificador=compra_mensual>42

#processing
print("######################################")
print("# CANTIDAD DE COMPRAS MENSUAL  ")
print("#########################################")
print("#compra en la semana 1 :",compra_semana_1)
print("#compra en la semana 2 :", compra_semana_2)
print("#compra en la semana 3 :",compra_semana_3)
print("#compra en la semana 4 :",compra_semana_4)
print("#compra mensual:",compra_mensual)
print("########################################")

#condicional simple
#si la compra mensual>42 mostrar, gano un juego de almohada
if(verificador==True):
    print("gano un juego de almohada")
#fin_if


