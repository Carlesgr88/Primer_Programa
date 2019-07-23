

mi_lista= []
lista= input("Que necesitas comprar?(escribe Fin para terminar)").upper()

while lista != "FIN":
    mi_lista.append(lista)
    lista= input("Que necesitas comprar?(escribe Fin para terminar)").upper()

for item in mi_lista:
    print("tengo que comprar {}".format(item))

print("Esta es la lista de la compra")