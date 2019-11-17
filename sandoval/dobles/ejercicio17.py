import os
# INPUT
velocidad_tangencial=int(os.sys.argv[1])
radio=float(os.sys.argv[2])

# PROCESSING
aceleracion_centripeta=velocidad_tangencial**2/(radio)

# VERIFICADOR
validar_aceleracion=aceleracion_centripeta>=40

# OUTPUT
print("#####################################")
print("## ACELERACION CENTRIPETA")
print("####################################")
print("## velocidad tangencial:  ", velocidad_tangencial)
print("## radio :                ", radio                    )
print("## aceleracion centripeta: ", aceleracion_centripeta)
print("################################################")

# PROCESSING
if (validar_aceleracion>=True):
    print(" CONDIONA AL VERIFICADOR")
else:
    print("cumple lo anterior")
