import os
# INPUT
velocidad_inicial=int(os.sys.argv[1])
aceleracion=int(os.sys.argv[2])
tiempo=int(os.sys.argv[3])

# PROCESSING
velocidad_final=velocidad_inicial+(aceleracion*tiempo)
print("velocidad final:", velocidad_final)

# VERIFICADOR
comprobar_v_final=(velocidad_final<61)

# OUTPUT
print("#################################")
print("  VELOCIDAD FINAL DEL AUTOMOVIL  ")
print("#################################")
print("#")
print("# DATOS:                          VALOR:"  )
print("# velocidad inicial:     ",velocidad_inicial," ")
print("# aceleracion:           ",aceleracion,"    ")
print("# tiempo:                ",tiempo,"        ")
print("# velocidad final:       ",velocidad_final,"  ")
print("################################################")

# CONDICIONALES DOBLES
if (comprobar_v_final<=False):
    print(" LA VELOCIDAD FINAL LE ES FAVORABLE  ")
else:
    print(" LLEGA A TIEMPO ")
