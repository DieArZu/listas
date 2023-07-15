#2.	Dada una lista de números, imprime el número más grande y el número más pequeño sin utilizar las funciones max() y min().
print("Max y min de lista")
lista=[]

tamaño=int(input("Digite el tamaño de la lista: "))

for i in range(tamaño):
    print("Dato",i+1,"Ingrese el numero: ")
    num=float(input())
    lista.append(num)

min=lista[0]
max=lista[0]
for i in range(tamaño):
    if lista[i]<=min:
        min=lista[i]
    elif lista[i]>=max:
        max=lista[i]

print("El numero mayor es: ",max)
print("El numero menor es: ",min)


    


