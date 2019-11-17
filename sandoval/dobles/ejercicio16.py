import os
# INPUT
velocidad=int(os.sys.argv[1])
gravedad=float(os.sys.argv[2])

# PROCESSING
altura_maxima=velocidad**2/(2*gravedad)

# VERIFICADOR
validar_altura_maxima=(altura_maxima<100)

# OUTPUT
print("##################################")
print("## BOLETA DE FISICA ")
print("###################################")
print("# velocidad:  ",velocidad," ")
print("# gravedad:   ", gravedad, "  ")
print("# altura maxima: ",altura_maxima," ")
print("#################################")

# CONDICIONAL DOBLES
if ( validar_altura_maxima<100):
    print(" la altura es true")
else:
    print("es aceptable")
