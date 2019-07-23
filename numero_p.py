

lista_numeros=[]
numero_usuario=""

while len(lista_numeros) < 10:
    while not numero_usuario.isdigit():
        numero_usuario=input("Introduce un número: ")
    lista_numeros.append(numero_usuario)
    numero_usuario=""
    print("Número añadido")

print("El número más pequeño es el {}".format(min(lista_numeros)))
