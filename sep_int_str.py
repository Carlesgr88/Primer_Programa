

lista_datos=["daf",2,5,"hea",55,"asd","ynv",9]
lista_str=[]
lista_int=[]
for items in lista_datos:
    if type(items)== type(2):
        lista_int.append(items)
    else:
        lista_str.append(items)
print("Los datos {} son un int".format(lista_int))
print("Los datos {} son una str".format(lista_str))
