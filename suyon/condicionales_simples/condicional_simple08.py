import os
#calcular el numero de electrones
#imput
numero_de_atomico=int(os.sys.argv[1])
carga=int(os.sys.argv[2])

#processing
numero_de_electrones=(numero_de_atomico+carga)

#output
print("###########################################")
print("#   NUMERO DE ELECTRONES          ")
print("###########################################")
print("#numero de atomico:",numero_de_atomico)
print("#carga:",carga)
print("#el numero de electrones:",numero_de_electrones)
print("##############################################")

#condicional simple
#si el numero de elctrones>12 mostrarle,maximo numero de electrones
if(numero_de_electrones>12):
    print("maximo numero de electrones ")
#fin_if
