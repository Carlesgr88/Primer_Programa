
lista_numeros =[]
numeros_usuario =input("Introduce un numero: ")
print("Número añadido correctamente")

while numeros_usuario != "fin":
    lista_numeros.append(numeros_usuario)
    numeros_usuario =input("Introduce un numero: (Escribe <fin> para terminar)")
    print("Número añadido correctamente")

suma =0
for i in lista_numeros:
 suma += i
print(suma)