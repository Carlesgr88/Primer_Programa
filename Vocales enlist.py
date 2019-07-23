
lista_vocales=[]
lista_consonantes=[]
frase_usuario= input("Introduce una oración: ").lower()

vocales= ["a","e","i","o","u"]

for letra in frase_usuario:
    if letra in vocales:
        lista_vocales.append(letra)
    else:
        lista_consonantes.append(letra)
for letra in lista_vocales:
    print("En tu oración está la vocal {}".format(letra))
