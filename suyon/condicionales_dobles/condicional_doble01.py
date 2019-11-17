import os
#calcular el puntaje del examen ordinario de la Universidad Nacional Pedro Ruis Gallo

#input
postulante=os.sys.argv[1]
puntaje_letras=float(os.sys.argv[2])
puntaje_numeros=float(os.sys.argv[3])
puntaje_humanidades=float(os.sys.argv[4])

#processing
puntaje_total=puntaje_letras+puntaje_numeros+puntaje_humanidades

#verificador
verificador=puntaje_total>=65.5

#output
print("###########################################")
print("# Puntaje del postulante")
print("#########################################")
print("#postulante:",postulante)
print("#puntaje de letras:",puntaje_letras)
print("#puntaje de numeros:",puntaje_numeros)
print("#puntaje de humanidades:",puntaje_humanidades)
print("#puntaje total:",puntaje_total)
print("#############################################")

#condicion doble
#si el postulante tiene un putaje>=65.5 mostrar ,Alcanzo vacante
if(verificador==True):
    print("Alcanzo vacante")
else:
    print("NO alcanzo vacante")

