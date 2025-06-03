def abc(n,i):
    if i==1:
        return 0
    while not n%i:
        n=n//i
    return not (n-1)%i
n=int(input())
e={}
for i in range(1,int(pow(n,0.5))+1):
    if not n%i:
        if abc(n,i):
            e[i]=0
        if abc(n,n//i):
            e[n//i]=0
n-=1

c=0
for i in range(1,int(pow(n,0.5))+1):
    if not n%i:
        c+=1
        if i!=n//i:
            c+=1
print(len(e)+c-1)
