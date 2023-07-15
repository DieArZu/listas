#3.	Dada una lista de palabras, imprime todas las palabras en orden alfabético.
print("Orden alfabetico")
lista=[]

tamaño=int(input("Digite la cantidad de palabras a ordenar : "))

for i in range(tamaño):
    print("Dato",i+1,"Ingrese la palabra: ")
    palabra=input()
    lista.append(palabra)

lista.sort()
print("Las palabras dadas en orden alfabetico quedan asi")
#print(lista)
for i in lista:
    print(i)