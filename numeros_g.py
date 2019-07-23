

lista_numeros=[]
numero_del_usuario=""

while len(lista_numeros) < 10:
    while not numero_del_usuario.isdigit():
        numero_del_usuario= input("Introduce un numero: ")
    lista_numeros.append(numero_del_usuario)
    numero_del_usuario=""
    print("Número añadido")
numero_grande = lista_numeros[0]

for numero in lista_numeros:
    if numero > numero_grande:
        numero_grande=numero

print("El número más grande es {}".format(numero_grande))



