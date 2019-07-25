

lista_numeros=[1,2,3,4,5,6,7,8,9,10,11,12,15,532,64,45,44,99]
for numero in range(len(lista_numeros)):
    numeros=lista_numeros[numero]

    if numeros % 3 == 0 or numeros % 5 == 0:
        lista_numeros[numero]=""

        if numeros % 3 == 0:
            lista_numeros[numero] +="Fizz"
        if numeros % 5 == 0:
            lista_numeros[numero] +="Buzz"

print(lista_numeros)