#Simulador de lucha pokemon

enemigo=input("contra que enemigo quieres luchar? (Bulbasaur/Charmander/Squirtle): ").upper()

vida_pikachu=100
vida_enemigo= 0

if enemigo == "SQUIRTLE":
    vida_enemigo= 90
    nombre_enemigo="Squirtle"
elif enemigo== "CHARMANDER":
    vida_enemigo= 80
    nombre_enemigo="Charmander"
else:
    vida_enemigo= 100
    nombre_enemigo="Bulbasaur"

while vida_pikachu > 0 and vida_enemigo >0:

    ataque_elegido=input("que ataque quieres usar? (Chispazo/Bola Voltio): ").upper()

    if ataque_elegido=="CHISPAZO":
        vida_enemigo -=10
    elif ataque_elegido=="BOLA VOLTIO":
        vida_enemigo -=12
    else:
        print("Tu pikachu no conoce ese ataque")

    print("La vida del {} enemigo ahora es de {}" .format(nombre_enemigo,vida_enemigo))

    if enemigo== "SQUIRTLE":
        ataque_enemigo=8
    elif enemigo== "CHARMANDER":
        ataque_enemigo=7
    else:
        ataque_enemigo=10

    vida_pikachu -= ataque_enemigo

    print("{} te hace un ataque de {} de daño".format(nombre_enemigo,ataque_enemigo))
    print("la vida de tu pikachu es de {}".format(vida_pikachu))

if vida_enemigo <=0:
    ganador="Pikachu"
else:
    ganador=nombre_enemigo

print("El combate ha terminado, el ganador es {}".format(ganador))
f