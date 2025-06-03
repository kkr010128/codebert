kn=input("").split(" ")
k=int(kn[0])
n=int(kn[1])
aa=input("").split(" ")
lista=[]
for i in aa:
    lista+=[int(i)]
for i in range(n):
    lista[i]%=k
lista.sort()

s=k-lista[n-1]+lista[0]
t=lista[n-1]-k
for i in range(n):
    ss=lista[i]-t
    
    if(ss>s):
        s=ss
        
    t=lista[i]
print(k-s)
    
    
