import os
# INPUT
a=int(os.sys.argv[1])
b=int(os.sys.argv[2])

# PROCESSING
P=((a**2)+(b**2)+(a*b)+(a*b))
print("P:", P)

# VERIFICADOR
comprobar=(P>=78.9)

# OUTPUT
print("###############################")
print("     CALCULAR  P               ")
print("################################")
print("#")
print("#  VARIABLES:          VALOR:  ")
print("# a:                  ",a ,"   ")
print("# b:                  ",b,"    ")
print("# P:                  ",P,"    ")
print("################################")

# CONDICIONALES SIMPLES
if (comprobar==True):
    print(" EL VALOR P ES VAFORABLE AL DESARROLLAR")
# fin_in
