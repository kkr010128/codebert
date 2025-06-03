n=int(input())
a=list(map(int,input().split()))
q=int(input())
b=[0]*q
c=[0]*q
for i in range(q):
    b[i],c[i]=map(int,input().split())
N=[0]*(10**5)
s=0
for i in range(n):
    N[a[i]-1]+=1
    s+=a[i]
for i in range(q):
    s+=(c[i]-b[i])*N[b[i]-1]
    N[c[i]-1]+=N[b[i]-1]
    N[b[i]-1]=0
    print(s)