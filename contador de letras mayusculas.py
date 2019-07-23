

frase_usuario= input("Introduce una frase: ")

mayusculas=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

n_mayusculas= 0

for letra in frase_usuario:
    if letra in mayusculas:
        n_mayusculas += 1
    else:
        n_mayusculas += 0

print("En tu oración hay {} mayúsculas".format(n_mayusculas))