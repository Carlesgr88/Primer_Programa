

lista_numeros=[12,4,6,88,24,4,74]
numero_grande = lista_numeros[0]

for numero in lista_numeros:
    if numero > numero_grande:
        numero_grande=numero

print("El número más grande es {}".format(numero_grande))
