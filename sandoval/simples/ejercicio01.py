import os
# boleta de venta
# declarar variables
# INPUT
cliente=os.sys.argv[1]
pedido01=int(os.sys.argv[2])
pedido02=int(os.sys.argv[3])
pedido03=int(os.sys.argv[4])
pu1=float(os.sys.argv[5])
pu2=float(os.sys.argv[6])
pu3=float(os.sys.argv[7])
IGV=float(os.sys.argv[8])

# PROCESSING
total_camisas=pedido01*pu1
total_pantalones=pedido02*pu2
tolal_corbatas=pedido03*pu3
total=(total_camisas+total_pantalones+tolal_corbatas)*IGV

# VERIFICADOR
comprobar=(total>=894)

# OUTPUT
print("######################################")
print("    BOLETA DE VENTA : TIENDA JOSE             ")
print("###########################################")
print("#")
print("# cliente:              ",cliente,"    ")
print("##################################################")
print("   DATOS:        CANTIDAD:     PU:       TOTAL:")
print("# camisas:         ",pedido01,"      ",pu1,"       ",total_camisas,"  ")
print("# pantalones:      ",pedido02,"      ",pu2,"       ",total_pantalones,"")
print("# corbatas:        ",pedido03,"      ",pu3,"       ",tolal_corbatas,"")
print("# IGV:             ",IGV,"          ")
print("# total:           ",total,"      ")
print("###########################################")

# condicional simple
# verificar la boleta de compra del cliente
if (comprobar==True):
    print(" GANASTES 20 PUNTOS POR TU COMPRA")
# fin_if
