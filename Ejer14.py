#14.	Dada una tupla de nombres, crea una lista que contenga solo los nombres que tengan más de una vocal.
print("Palabras de la lista q tenga más de 2 vocales")
lista=[]
lista2=[]
lista3=[]
voca=0
voce=0
voci=0
voco=0
vocu=0

tamaño=int(input("Digite la cantidad de palabras de la lista: "))
for i in range(tamaño):
    print("Dato",i+1,"Ingrese la palabra: ")
    nom=str(input())
    lista.append(nom)

for i in lista:
  lista2.clear()
  voca=i.find("a")
  voce=i.find("e")
  voci=i.find("i")
  voco=i.find("o")
  vocu=i.find("u")

  if voca>-1:
     print(i,"La palabra tiene a")
     lista2.append(1)
  if voce>-1:
     print(i,"La palabra tiene e")
     lista2.append(1)
  if voci>-1:
     print(i,"La palabra tiene i")
     lista2.append(1)
    
  if voco>-1:
     print(i,"La palabra tiene o")
     lista2.append(1)
  if vocu>-1:
     print(i,"La palabra tiene u")
     lista2.append(1)
  tama=sum(lista2)
  print(i, "Tiene ",tama," vocales")
  if tama>2:
     lista3.append(i)

print("Las palabras con más de 2 vocales son: ",lista3)
 