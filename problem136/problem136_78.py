#169D
#Div Game

n=int(input())

def factorize(n):
    fct=[]
    b,e=2,0
    while b**2<=n:
        while n%b==0:
            n/=b
            e+=1
        if e>0:
            fct.append([b,e])
        b+=1
        e=0
    if n>1:
        fct.append([n,1])
    return fct
l=factorize(n)
ans=0
for i in l:
    c=1
    while i[1]>=c:
        ans+=1
        i[1]-=c
        c+=1
print(ans)