import os
# calcular la presion hidrostatica

#input
densidad=float(os.sys.argv[1])
gravedad=float(os.sys.argv[2])
altura=float(os.sys.argv[3])

#processing
presion_hidrostatica=(densidad*gravedad*altura)

#verificador
verificador=(presion_hidrostatica>=13)

#output
print("#########################################################")
print("#    BOLETA DE LA FORMULA DE LA PRESION HIDROSTATICA    #")
print("#########################################################")
print("#    datos")
print("#densidad0:   ",densidad)
print("#gravedad0:   ",gravedad)
print("#altura0:   ",altura)
print("#presion hidrostatica:   ",presion_hidrostatica)
print("##########################################################")

#condicional multiple
#si la presion hidrostatica>=13 mostrar, la presion hidrostatica es acepatable
if(verificador==True):
    print("la presion hidrostatica es aceptable ")
if(presion_hidrostatica<13 and presion_hidrostatica>1):
    print("presion hidrostatica no aceptable")
if(presion_hidrostatica<=1):
    print("ERROR")
#fin_if
