import os
# INPUT
cliente=os.sys.argv[1]
consumo01=int(os.sys.argv[2])
consumo02=int(os.sys.argv[3])
precio01=int(os.sys.argv[4])
precio02=int(os.sys.argv[5])
IGV=float(os.sys.argv[6])

# PROCESSING
cuenta_total=(consumo01*precio01+consumo02*precio02)*IGV

# VERIFICADOR
comprador_compulsivo=cuenta_total>=100

# OUTPUT
print("###############################################")
print("###  BOLETA COMERCIAL  ")
print("##############################################")
print("# cliente:  ", cliente   )
print("# pedidos:     cantida:              p.u      ")
print("# ceviche:     ",consumo01,"         ",precio01," ")
print("# carne seca:  ",consumo02,"         ",precio02," ")
print("# IGV:        ",IGV)
print("# total:      ",cuenta_total)
print("##############################################")

# CONDICIONAL DOBLES
if (comprador_compulsivo==100):
    print(" ganaste 30 puntos ")
else:
    print("LE CLIENTE NO GANO PUNTOS")

