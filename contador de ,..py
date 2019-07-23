

frase_usuario=input("Introduce una frase: ")

espacio=" "
punto="."
coma=","
n_espacios=0
n_puntos=0
n_comas=0

for elemento in frase_usuario:
    if elemento in espacio:
        n_espacios += 1
    elif elemento in punto:
        n_puntos += 1
    elif elemento in coma:
        n_comas +=1

print("En tu frase hay {} espacios, {} puntos y {} comas".format(n_espacios,n_puntos,n_comas))