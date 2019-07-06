#Calculadora de operaciónes básicas

operacion=input("¿Que operación quieres realizar?(Sumar/Restar/Multiplicar/Dividir): ").upper()
primer_numero=int(input("Dime el primer número: "))
segundo_numero=int(input("Dime el segundo número: "))


if operacion== "SUMAR":
    resultado=primer_numero+segundo_numero
elif operacion=="RESTAR":
    resultado=primer_numero-segundo_numero
elif operacion=="MULTIPLICAR":
    resultado=primer_numero*segundo_numero
elif operacion=="DIVIDIR":
    resultado=primer_numero/segundo_numero
else:
     print("no has seleccionado ninguna de las opciones anteriores")
print("El resultado de la operación es {}".format(resultado))