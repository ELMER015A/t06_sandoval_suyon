import os
#calcular el area total de la piramide

#input
area_lateral_piramide=int(os.sys.argv[1])
area_base_piramide=int(os.sys.argv[2])

#processing
area_total_piramide= area_lateral_piramide + area_base_piramide

#verificador
verificador=(area_total_piramide<=72)

#output
print("#################################################")
print("#        BOLETA DEL AREA TOTAL DE LA PIRAMIDE    #")
print("#################################################")
print("# datos  "                                        )
print("#area lateral de la piramide:    ",area_lateral_piramide)
print("#area de la base de la piramide:    ",area_base_piramide)
print("#area total de la piramide     ",area_total_piramide)
print("###################################################")

#condicional multiple
#si el area de la piramide <72 mostrar,piramide estable
if(verificador==True):
    print("piramide estable")
if(area_total_piramide>=72 and area_total_piramide<98):
    print("piramide inestable")
if(area_total_piramide>=98 and area_total_piramide<100):
    print("piramide imaginaria")
#fin_if
