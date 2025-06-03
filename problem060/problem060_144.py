n,m,l=map(int,raw_input().split())
A=[]
B=[]
for i in range(n):
    A.append(map(int,raw_input().split()))
for i in range(m):
    B.append(map(int,raw_input().split()))
for i in range(n):
    print(' '.join(map(str,[sum([A[i][j]*B[j][k] for j in range(m)]) for k in range(l)])))