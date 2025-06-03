n=int(input(""))
lista=[0]*n
a=input("").split(" ")
for i in a:
    lista[int(i)-1]+=1
for i in lista:
    print(i)

    
