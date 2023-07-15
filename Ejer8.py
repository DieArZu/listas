#8.	Dada una lista de números, suma todos los elementos y guarda el resultado en una variable.
print("Suma de elementos de una lista")
lista=[]
lista2=[]
tamaño=int(input("Digite la cantidad de numeros de la lista: "))
for i in range(tamaño):
    print("Dato",i+1,"Ingrese el numero: ")
    num=float(input())
    lista.append(num)
numero=0
for i in lista:
    suma=sum(lista)
    
       

print("La suma es: ", suma)
