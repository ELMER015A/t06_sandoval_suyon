import os
# INPUT
nombre=os.sys.argv[1]
cargo=os.sys.argv[2]
sueldo=int(os.sys.argv[3])
descuento=int(os.sys.argv[4])

# PROCESSING
total_salario_mensual=sueldo-descuento

# VERIFICADOR
comprobar_el_sueldo=(total_salario_mensual<1500)

# OUTPUT
print("##########################################")
print("       BOLETA DE PAGO                 ")
print("#########################################")
print("#")
print("# Nombre:                  ",nombre,"    ")
print("# Cargo:                   ",cargo,"     ")
print("# sueldo mensual:          ",sueldo,"    ")
print("# descuento del AFP:       ",descuento," ")
print("# total de recibo mensual: ",total_salario_mensual," ")
print("#############################################")

# condicional simples
if (comprobar_el_sueldo>=True):
    print(" PAGO DE UN EMPLEADO ES ACEPTABLE ")
# fin_if
