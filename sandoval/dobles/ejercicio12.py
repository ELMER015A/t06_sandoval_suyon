import os
# INPUT
Fuerza=int(os.sys.argv[1])
Distancia=int(os.sys.argv[2])

# PROCESSING
Trabajo=Fuerza*Distancia
print("Tabajo:",Trabajo)

# VERIFICADOR
comprobar=(Trabajo>91)

# OUTPUT
print("#############################################")
print("  BOLETA DE TRABAJO AL REALIZA UNA PERSONA")
print("# Fuerza:              ",Fuerza,"    ")
print("# Distancia:           ",Distancia," ")
print("# Trabajo:             ",Trabajo,"   ")
print("########################################")

# CONDICIONALES DOBLES
if (comprobar==True):
    print(" EL TRABAJO ES VERIFICABLE ")
else:
    print("EL TRABAJO NO ES VERIFICABLE")
