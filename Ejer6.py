#6.	Dada una lista de números, elimina todos los elementos pares de la lista.
print("Programa de elemina los pares de una lista")
lista=[]
lista2=[]
tamaño=int(input("Digite la cantidad de numeros de la lista: "))
for i in range(tamaño):
    print("Dato",i+1,"Ingrese el numero: ")
    num=float(input())
    lista.append(num)

for i in lista:
    if i % 2 != 0:
        lista2.append(i)

print("Los numeros impares son: ")
for i in lista2:
    
    print(i)
