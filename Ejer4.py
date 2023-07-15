#4.	Dada una lista de números, duplica el valor de cada elemento de la lista y guárdalo en una nueva lista.
print("Duplicado de lista en otra lista")
lista=[]
listax2=[]
tamaño=int(input("Digite la cantidad de numeros de la lista: "))
for i in range(tamaño):
    print("Dato",i+1,"Ingrese el numero: ")
    num=float(input())
    lista.append(num)

for i in range(tamaño):
    multipli= lista[i]*2
    #print(lista[i],"* 2 es=",multipli)
    listax2.append(multipli)

print("Los duplicados de los numeros dados son:")
for i in listax2:
    print(i)