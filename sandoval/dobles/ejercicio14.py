import os
# INPUT
Distancia=int(os.sys.argv[1])
Tiempo=int(os.sys.argv[2])

# PROCESSING
Velocidad=(Distancia/Tiempo)

# VERIFICADOR
comprobar=(Velocidad>30)

# OUTPUT
print("################################")
print("#   VELOCIADAD DEL AUTOMOVIL    ")
print("######################################")
print("#")
print("#  DATOS:                  VALOR:")
print("# Distancia:             ",Distancia," ")
print("# Tiempo:                ",Tiempo,"     ")
print("# Velocidad:             ",Velocidad,"   ")
print("########################################")

# CONDICIONALES DOBLES
if (comprobar==True):
    print(" VELOCIDAD DEL AUTOMOVIL ES MAYOR A 30m/s")
else:
    print(" LA VELOCIDAD NO CUMPLE LA CONDICION")
