import os
# clacular el area lateral del cilindro
#input
pi=3.1416
radio1=float(os.sys.argv[1])
generatriz1=float(os.sys.argv[2])

#processing
area_lateral_cilindro=(2*pi*radio1*generatriz1)

#verificador
verificador=(area_lateral_cilindro>=34)

#output
print("###############################################")
print("#         BOLETA DEL AREA DEL CILINDRO        #")
print("###############################################")
print("#   datos")
print("#pi:  ",pi                                       )
print("#radio1:    ",radio1)
print("#generatriz1:    ",generatriz1)
print("#area latera del cilindro:    ",area_lateral_cilindro)
print("#################################################")

#condicional doble
#si el area del cilindro>34 mostrar, area del cilindro es regular
if(verificador==True):
    print("el area del cilindro es regular")
else:
    print("el area del triangulo es irregular")
