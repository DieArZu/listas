#1.	Crea una lista vacía y agrega los números del 1 al 10 a la lista utilizando un bucle después nuestra 
#estos datos multiplicados por 2.
lista=[]

for i in range(10):
    print("Dato",i+1,"Ingrese el numero: ")
    num=float(input())
    lista.append(num)

for i in range(10):
    multipli= lista[i]*2
    print(lista[i],"* 2 es=",multipli)
    

