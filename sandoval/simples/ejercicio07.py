import os
# INPUT
velocidad_inicial=int(os.sys.argv[1])
velocidad_final=int(os.sys.argv[2])
tiempo=int(os.sys.argv[3])

# PROCESSING
altura=((velocidad_inicial+velocidad_final)/2)*tiempo

# VERIFICADOR
comprobador=(altura>=80)

# OUTPUT
print("##################################")
print("# ALTURA DE UN CUERPO EN CAIDA LIBRE  ")
print("####################################")
print("#")
print("# DATOS:                   VALOR:           ")
print("# velocidad inicial:      ",velocidad_inicial,"  ")
print("# velocidad final:        ",velocidad_final,"   " )
print("# tiempo:                 ",tiempo,"             ")
print("# altura:                 ",altura,"             ")
print("##################################################")

# CONDICIONALES SIMPLES
if (comprobador==False):
    print(" LA ALTURA ES ACEPTABLE ")

# fin_if
