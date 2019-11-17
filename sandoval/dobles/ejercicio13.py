import os
# INPUT
base=int(os.sys.argv[1])
altura=int(os.sys.argv[2])

# PROCESSING
Area_del_rectangulo=base*altura

# VERIFICADOR
comprobar=(Area_del_rectangulo<=90)

# OUTPUT
print("#############################")
print("  CALCULAR EL AREA DEL RECTANGLO ")
print("##################################")
print("#")
print("#  DATOS:                VALOR:           ")
print("# Base:                 ", base,"         ")
print("# Altura:               ",altura ,"       ")
print("# Area de rectangulo:   ",Area_del_rectangulo)
print("###########################################")

# CONDICIONALES DOBLES
if (comprobar<100):
    print(" ES VERIFICABLE EL AREA DEL RECTANGULO ")
else:
    print(" EL RECTANGULO NO ES VERIFICABLE")

