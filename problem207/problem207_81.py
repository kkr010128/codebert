a1=input("").split(" ")
a2=input("").split(" ")
a3=input("").split(" ")
lista=[]
listmp=[]
for k in range(3):
    listmp+=[int(a1[k])]
lista+=[listmp]
listmp=[]
for k in range(3):
    listmp+=[int(a2[k])]
lista+=[listmp]
listmp=[]
for k in range(3):
    listmp+=[int(a3[k])]
lista+=[listmp]
n=int(input(""))
listn=[]
for i in range(n):
    t=int(input(""))
    listn+=[t]
for i in range(3):
    for k in range(3):
        if(lista[i][k] in listn):
            lista[i][k]=0
p=0
for i in range(3):
    s=0
    for k in range(3):
        s+=lista[i][k]

    if(s==0):
            p=1
for i in range(3):
    s=0
    for k in range(3):
        s+=lista[k][i]

    if(s==0):
            p=1
s=0
for i in range(3):
    s+=lista[i][i]
if(s==0):
    p=1
s=0
for i in range(3):
    s+=lista[i][2-i]
if(s==0):
    p=1
if(p==1):
    print("Yes")
else:
    print("No")
    
    

    
