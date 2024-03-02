print ("\n\t\t\t    bienvenido tu calculadora de trabajo online")
Nombre = input("\n    ingrese nombre: ")
HT = int(input("   ingrese horas : "))
VH = float(input("    valor hora: "))
SS = HT*VH
#f-sting
Mensaje = (f'tu nombre es:{Nombre} \t horas tabajadas: {HT} '
           f'\n valor hora: {VH} ')
print ("SUS DATOS \n ingresados son: ")
print(Mensaje)
print(SS)