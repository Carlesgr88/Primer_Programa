

frase_usuario=input("Introduce una frase: ")

vocales=["a","e","i","o","u"]

n_vocales= 0
n_consonantes=0
for letra in frase_usuario:
    if letra in vocales:
        n_vocales += 1
    else:
        n_consonantes +=1

print("En tu frase hay {} vocales y {} consonantes".format(n_vocales,n_consonantes))
