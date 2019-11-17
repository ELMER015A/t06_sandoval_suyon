import os
# INPUT
base_mayor=int(os.sys.argv[1])
base_menor=int(os.sys.argv[2])
altura=int(os.sys.argv[3])

# PROCESSING
area_del_trapecio=((base_mayor+base_menor)*altura)/2
print("area del trapecio:", area_del_trapecio)

# VERIFICADOR
comprobar_area=(area_del_trapecio>=100)

# OUTPUT
print("###############################")
print("    AREA DEL TRAPECIO           ")
print("####################################")
print("#")
print("#  DATOS:                VALOR:      ")
print("#  Base mayor:         ",base_mayor," ")
print("#  Base menor:         ",base_menor," ")
print("#  Altura:             ",altura,"     ")
print("#  Area trapecio:      ",area_del_trapecio," ")
print("#######################################")

# CONDICIONALES SIMPLES
if (comprobar_area>=True):
    print(" EL AREA DEL TRAPECIO ES ACEPTABLE ")
if (comprobar_area<100 and comprobar_area>500):
    print(" EL AREA DEL TRAPECIO NO ES ACEPTABLE")
if (area_del_trapecio>100):
    print(" NO CUMPLE MAYOR A 100")
