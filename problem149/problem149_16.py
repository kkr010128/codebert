n,m,x = map(int, input().split())

N=[]
NI=[]
for i in range(n) :
    N = list(map(str, input().split()))
    NI.append(N)

ans=-1

for i in range(1<<n) :
    A=[0]*(m+1)
    for j in range(n) :
        # print(NI[j])
        if (1<<j)&i :
            A=[x+int(y) for(x,y)in zip(A,NI[j])]
    # print(A)
    a = A[0]
    del A[0]
    if min(A)<x :
        a=-1
    elif ans==-1:
        ans = a
    elif ans>a :
        ans = a
print(ans)
