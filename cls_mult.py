

lista_numeros=[]
numeros_usuario=int(input("Introduce un número (escribe <0> para terminar): "))
print("Número añadido correctamente ")
print(lista_numeros)

while numeros_usuario != 0:
    lista_numeros.append(numeros_usuario)
    numeros_usuario=int(input("Introduce un número (escribe <0> para terminar):"))
    print("Número añadido correctamente ")
    print(lista_numeros)

multiplos_dos=[]
multiplos_tres=[]
multiplos_cinco=[]
multiplos_siete=[]

for indice in range(len(lista_numeros)):
    numeros=lista_numeros[indice]

    if lista_numeros[indice] % 2 == 0:
        multiplos_dos.append(numeros)
    if  lista_numeros[indice] % 3 == 0:
        multiplos_tres.append(numeros)
    if  lista_numeros[indice] % 5 == 0:
        multiplos_cinco.append(numeros)
    if  lista_numeros[indice] % 7 == 0:
        multiplos_siete.append(numeros)

print("Los multiplos de dos son {}".format(multiplos_dos))
print("Los multiplos de tres son {}".format(multiplos_tres))
print("Los multiplos de cinco son {}".format(multiplos_cinco))
print("Los multiplos de siete son {}".format(multiplos_siete))

