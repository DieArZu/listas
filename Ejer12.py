#12.	Dada una lista de palabras, crea una lista que contenga el número de caracteres de cada palabra.
print("Cantidad de carateres de cada palabra en una lista")
lista=[]
lista2=[]
tamaño=int(input("Digite la cantidad de palabras de la lista: "))
for i in range(tamaño):
    print("Dato",i+1,"Ingrese la palabra: ")
    nom=str(input())
    lista.append(nom)

for i in lista:
    a=len(i)
    lista2.append(a)
    print("El tamaño de: ", i , "es", a)

print("La cantidad de caracteres en cada palabra de la lista es : ",lista2)

