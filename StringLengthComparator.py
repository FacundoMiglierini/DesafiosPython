cad1=input("Ingrese cadena 1: ")
cad2=input("Ingrese cadena 2: ")
if (len(cad1)>len(cad2)):
    print(cad1)
elif (len(cad2)>len(cad1)):
    print(cad2)
else:
    print("Ambas cadenas tienen igual cantidad de caracteres.")
