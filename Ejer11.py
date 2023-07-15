#11.	Dada una lista de números, crea una nueva lista que contenga solo los números primos.
print("Programa lista de numros primos")
lista=[]
lista2=[]
tamaño=int(input("Digite la cantidad de numeros de la lista: "))
for i in range(tamaño):
    print("Dato",i+1,"Ingrese el numero: ")
    num=int(input())
    lista.append(num)
    lista2.append(num)

for i in lista:
    if i == 1:
        lista2.remove(1)
    for n in range(2,i,1):
        if i % n == 0 or i==1:
            print(i," No es primo", n, "es divisor")
            lista2.remove(i)
            break

           

            
            
print("Los primos de la lista son")
print(lista2)




