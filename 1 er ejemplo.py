print ("\n\t\t\t    bienvenido tu lugar online")
nombre = input("\n    ingrese nombre: ")
edad = int(input("    ingrese edad: "))
ciudad = (input("    ingrese ciudad: "))
peso = float(input("    ingrese peso: "))

#f-sting
mensaje = f'tu nombre es:{nombre} \t tu edad: {edad} \ntu ciudad: {ciudad} \t tu peso: {peso}'
print ("Los datos que has registrado \n hasta ahora son: ")
print(mensaje)