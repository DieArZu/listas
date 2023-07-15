#15.	Dada una lista de números, encuentra el segundo número más grande sin utilizar la función sorted().
print("2do mayor número")
lista=[]
lista2=[]

tamaño=int(input("Digite el tamaño de la lista: "))

for i in range(tamaño):
    print("Dato",i+1,"Ingrese el numero: ")
    num=float(input())
    lista.append(num)
    lista2.append(num)

min=lista[0]
max=lista[0]
max2=0

for i in range(tamaño):
    if lista[i]<=min:
        min=lista[i]
    elif lista[i]>=max:
        max=lista[i]
        
lista2.remove(max)
lista3=lista2
print(lista2)

for a in range(tamaño-1):
    if lista3[a]>=max2:
        max2=lista3[a]
       

print("El numero mayor es: ",max)
print("El numero menor es: ",min)
print("el segundo mayor numero es: ", max2)