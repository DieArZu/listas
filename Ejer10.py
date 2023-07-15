#10.	Dada una lista de números, encuentra la suma de los elementos en índices pares 
#y la suma de los elementos en índices impares.
print("Programa suma de números en indices pares o impares")
lista=[]
lista2=[]
tamaño=int(input("Digite la cantidad de numeros de la lista: "))
for i in range(tamaño):
    print("Dato",i+1,"Ingrese el numero: ")
    num=float(input())
    lista.append(num)

listapar=lista[0:tamaño:2]
listaimpar=lista[1:tamaño:2]
print("Los numetos en indices pares son: ")
print(listapar)
for i in listapar:
    sumapar=sum(listapar)
print("Y la suma de ellos da: ",sumapar)
print("Los numetos en indices inpares son: ")
print(listaimpar)    
for i in listaimpar:
    sumaimpar=sum(listaimpar)
print("Y la suma de ellos da: ",sumaimpar)
