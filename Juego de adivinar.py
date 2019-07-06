#Juego para dos jugadores, el 1r jugador pone el número a adivinar, mientras el otro, lo tiene que adivinar.(num 1 al 10)

numero_adivinar=int(input("Dime el numero que quieres adivinar (1 al 10): "))
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()

print("Empieza el juego:")
numero_usuario=int(input("Adivina el numero (1 al 10): "))
while numero_usuario != numero_adivinar:
    if numero_usuario <= 10 and numero_usuario > 0:
        numero_usuario=int(input("Adivina el numero: "))
    else:
        print("el numero tiene que ser entre el 1 y el 10, el {} no cuenta".format(numero_usuario))
        numero_usuario = int(input("Adivina el numero: "))

print("Enhorabuena has acertado el numero era el {}".format(numero_adivinar))