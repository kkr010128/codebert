n=int(input())
x=[i for i in range(n+3)]
x[0]=0
x[1]=1
i=2
while i<=n+1:
    j=2*i
    if x[i]==i:
        
        while j<=n+1:
            if x[j]==j:x[j]=i
            j+=i
    i+=1
def f(k):
    if k==1:
        return 1

    z=[]
    p=x[k]
    m=1
    ans=1
    while k>=2:
        k=k//p
        if p==x[k]:
            m+=1
        else:
            z.append(m)
            m=1
            p=x[k]

    for i in range(len(z)):
        ans*=z[i]+1
    return ans
s=0
for i in range(1,n+1):
    s+=i*f(i)
print(s)
