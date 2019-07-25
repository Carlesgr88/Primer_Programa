

lista_datos=[1,2,3,"asd",False,[],True,23,2.1]
lista_tipos=[]

for datos in lista_datos:
    lista_tipos.append(type(datos))

print(lista_tipos)