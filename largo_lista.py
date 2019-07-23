

lista_numeros=[]
largo_lista=0
numero_usuario = input("Introduce un número: ")
print("Número añadido correctamente")

while numero_usuario != "fin":
    lista_numeros.append(numero_usuario)
    numero_usuario = input("Introduce un número: ")
    print("Número añadido correctamente")

for item in lista_numeros:
    largo_lista +=1
print("La lista tiene una longitud de {} elementos".format(largo_lista))
