#7.	Dada una lista de palabras, crea una nueva lista que contenga solo las
# palabras que tengan más de 5 caracteres.
print("Lista con palabras de mas de 5 carateres")
lista=[]
lista2=[]
tamaño=int(input("Digite la cantidad de palabras de la lista: "))
for i in range(tamaño):
    print("Dato",i+1,"Ingrese la palabra: ")
    nom=str(input())
    lista.append(nom)

for i in lista:
    if len(i)>5:
        lista2.append(i)

print("Las palabras con más de 5 caracteres son: ",len(lista2))

for i in lista2:
    print(i)