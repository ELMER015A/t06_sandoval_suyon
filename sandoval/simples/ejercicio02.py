import  os
# BOLETA ELECTRONICA
# INPUT
cliente=os.sys.argv[1]
paga=int(os.sys.argv[2])
interes=float(os.sys.argv[3])

# PROCESSING
total_a_pagar=paga+interes*paga

# VERIFICADOR
comprobando_total=(total_a_pagar<465)

# OUTPUT
print("#####################################")
print("  BOLETA ELECTRONICA            ")
print("#")
print(" cliente:      ",cliente,"      ")
print("#")
print("# pagar:         ",paga,"       ")
print("# interes:       ",interes,"    ")
print("# total a pagar:  ",total_a_pagar," ")
print("#################################")

# condicional simple
# el dinero de senior es mayor a 500
if (comprobando_total<=True):
    print(" DEPOSITA SU DINERO EN UNA CUENTA")

# fin_if
