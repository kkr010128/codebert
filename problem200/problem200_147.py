a,b,m=map(int,input().split())

A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=[list(map(int,input().split())) for i in range(m)]

lis=[min(A)+min(B)]

for i in range(m):
    lis.append(A[C[i][0]-1]+B[C[i][1]-1]-C[i][2])

print(min(lis))
