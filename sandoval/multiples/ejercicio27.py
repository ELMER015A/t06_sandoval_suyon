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

# CONDICIONALES MULTIPLES
# El trabajo es mayor a 100 si cumple con las sieguientes condiciones
if (comprobar==True):
    print(" EL TRABAJO ES VERIFICABLE ")
if (comprobar<90 and comprobar>500):
    print(" el trabajo no es verificable")
if (comprobar<100):
    print(" TRABAJO NO RESPALDOPOR LOS FISICOS")
