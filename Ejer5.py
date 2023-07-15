#5.	Dada una lista de nombres, crea una lista que contenga solo los nombres que comiencen con la letra "A".
print("Programa de nombres con A de una lista")
lista=[]
listadea=[]
tamaño=int(input("Digite la cantidad de nombres de la lista: "))
for i in range(tamaño):
    print("Dato",i+1,"Ingrese el nombre: ")
    nom=str(input())
    lista.append(nom)

for i in lista:
    #print(i[0])
    if i[0]=="a" or i[0]=="A":
        listadea.append(i)

print("Los nombres con A son: ",len(listadea))

for i in listadea:
    print(i)