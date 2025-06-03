H,N=map(int,input().split())
L=[0]*N
for i in range(N):
    a,b=map(int,input().split())
    L[i]=(a,b)


DP=[float("inf")]*(H+1)
DP[0]=0

for (A,B) in L:
    for k in range(1,H+1):
        if k>=A:
            DP[k]=min(DP[k],DP[k-A]+B)
        else:
            DP[k]=min(DP[k],B)

print(DP[-1])