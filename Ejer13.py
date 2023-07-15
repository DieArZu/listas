#13.	Dada una lista de números, crea una nueva lista que contenga solo los números que sean múltiplos de 3.
print("Programa de multiplos de 3")
lista=[]
lista2=[]
tamaño=int(input("Digite la cantidad de numeros de la lista: "))
for i in range(tamaño):
    print("Dato",i+1,"Ingrese el numero: ")
    num=int(input())
    lista.append(num)
    

for i in lista:
    if i % 3==0:
        lista2.append(i)
        

            
            
print("Los multiplos de 3 son: ")
print(lista2)




