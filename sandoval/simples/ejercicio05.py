import os
# INPUT
Radio=int(os.sys.argv[1])
Pi=float(os.sys.argv[2])

# PROCESSING
area=((Radio**2)*Pi)

# VERIFICADOR
comprobador=(area>=145)

# OUTPUT
print("####################################")
print("#      AREA DEL CIRCULO          ")
print("######################################")
print("#")
print("#  DATOS:                 VALOR:   ")
print("# radio:                ",Radio,"   ")
print("# Pi:                   ",Pi,"      ")
print("# Area:                 ",area,"    ")
print("#####################################")

# CONDICIONALES SIMPLES
if (comprobador==True):
    print(" EL AREA DEL CIRCULO ES COMPATIBLE ")
# fin_if
