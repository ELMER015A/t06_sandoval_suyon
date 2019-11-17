import os
# BOLETA
# INPUT
densidad=int(os.sys.argv[1])
altura=int(os.sys.argv[2])
gravedad=float(os.sys.argv[3])

# PROCESSING
presion=densidad*altura*gravedad

# VERIFICADOR
comprobar=(presion<42.3)

# OUTPUT
print("#################################")
print("#    PRESION DE UN CUERPO         ")
print("###################################")
print("#")
print("#  DATOS:             VALOR:      ")
print("# densidad:          ",densidad," ")
print("# altura:            ",altura,"   ")
print("# gravedad:          ",gravedad,"  ")
print("# presion:           ",presion,"  ")
print("###################################")

# CONDICIONALES SIMPLES
if (comprobar!=True):
    print(" ES ACEPTABLE LA PRESION ")
# fin_if
