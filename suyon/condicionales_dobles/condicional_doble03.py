import  os
#calcular tiempo de alcance

#input
distancia=float(os.sys.argv[1])
velocidad1=float(os.sys.argv[2])
velocidad2=float(os.sys.argv[3])

#processing
tiempo_alcance=(distancia)/(velocidad1 - velocidad2)

#verificador
verificador=(tiempo_alcance<45)

#output
print("#########################################")
print("#     BOLETA DE TIEMPO DE ALCANCE       #")
print("#########################################")
print("# datos                                  ")
print("#distancia :   ",distancia)
print("#velocidad 1:   ",velocidad1)
print("#velocidad 2:   ",velocidad2)
print("#tiempo alcance:   ",tiempo_alcance)
print("#########################################")

#condicional doble
# si el tiempo de alcance<45 mostrar,tiempo de alcance minimo
if(verificador==True):
    print("tiempo de alcance minimo")
else:
    print("el tiempo de alcance es maximo")

