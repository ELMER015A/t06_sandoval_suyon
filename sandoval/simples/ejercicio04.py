import os
# INPUT
masa=int(os.sys.argv[1])
volumen=int(os.sys.argv[2])

# PROCESSING
Densidad=masa/volumen

# VERIFICADOR
comprobador=(Densidad>=80)

# OUTPUT
print("#####################################")
print("#      DENSIDAD DE UN CUERPO      ")
print("######################################")
print("#")
print("# DATOS:             VALOR:   ")
print("# masa:             ",masa,"     ")
print("# volumen:          ",volumen,"   ")
print("# densidad:         ",Densidad,"   ")
print("######################################")

# condicionales simples
if (comprobador==False):
    print(" DESIDAD DE UN CUERPO ES ACEPTABLE")
# fin_if
