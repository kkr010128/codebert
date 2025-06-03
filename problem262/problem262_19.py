N=int(input())
D=[{} for _ in range(N+1)]

for i in range(1,N+1):
    A=int(input())
    for k in range(A):
        p,x=map(int,input().split())
        D[i][p]=x

Max=0
for x in range(2**N):
    y=x

    B=["*"]*(N+1)
    for i in range(N):
        B[i+1]=y%2
        y>>=1

    Flag=True
    for i in range(1,N+1):
        if B[i]==1:
            for k in D[i]:
                Flag&=(B[k]==D[i][k])

    if Flag:
        Max=max(Max,B.count(1))

print(Max)
