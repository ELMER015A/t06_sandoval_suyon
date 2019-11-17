import os
# BOLETA
# INPUT
densidad=int(os.sys.argv[1])
altura=int(os.sys.argv[2])
gravedad=float(os.sys.argv[3])

# PROCESSING
presion=densidad*altura*gravedad

# VERIFICADOR
comprobar=(presion>42.3)

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

# CONDICIONALES MULTIPLES
if (comprobar==True):
    print("LA PRESION ES ACEPTABLE")
if (comprobar>=30 and comprobar>=800):
    print(" LA PRECION NO ES ACEPTABLE ")
if (comprobar>=452):
    print(" LA PRESION ES MENOR A 100")
