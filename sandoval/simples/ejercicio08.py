import os
# INPUT
Masa=int(os.sys.argv[1])
Aceleracion=int(os.sys.argv[2])

# PROCESSING
Fuerza=Masa*Aceleracion
print("Fuerza:", Fuerza)

# VERIFICADOR
comprobar=(Fuerza<=80)

# OUTPUT
print("################################################")
print("  LA FUEZA QUE APLICA UNA PERSONA A UNA PIEDRA  ")
print("################################################")
print("#")
print("# DATOS:                 VALOR:                ")
print("# Masa:                 ", Masa , "            ")
print("# Aceleracion:         ", Aceleracion , "      ")
print("# Fuerza:              ",Fuerza ,"             ")
print("###############################################")

# CONDICIONALES SIMPLES
if (comprobar==False):
    print(" LA FUERZA DE LA GRUA ES ACEPTABLE")
# fin_if
