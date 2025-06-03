def f(x):
    if x=="r":
        return 2
    elif x=="s":
        return 0
    else:
        return 1

N,K=map(int,input().split())
L=list(map(int,input().split()))
T=["*"]+list(map(f,input()))


Z=[[0,0,0] for _ in range(N+1)]

for x in range(1,N+1):
    for a in range(3):
        if x<=K:
            Z[x][a]=L[a]*(T[x]==a)
        else:
            b=(a+1)%3
            c=(b+1)%3

            Z[x][a]=max(Z[x-K][b],Z[x-K][c])+L[a]*(T[x]==a)

X=0
for i in range(1,K+1):
    X+=max(Z[-i])
print(X)