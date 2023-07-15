#9.	Dada una tupla de números, crea una lista que contenga el cuadrado de cada número.
print("Programa que guarda el cuadrado de cada número")
lista=[]
lista2=[]
tamaño=int(input("Digite la cantidad de numeros de la lista: "))
for i in range(tamaño):
    print("Dato",i+1,"Ingrese el numero: ")
    num=float(input())
    lista.append(num)

for i in lista:
    cuadrado=i*i
    lista2.append(cuadrado)

print("Los cuadrados de los numeros dados son: ")

for i in lista2:
   print(i)