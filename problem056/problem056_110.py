n,m=[int(x) for x in input().split()]
A=[[0 for i in range(m)] for i in range(n)]
vector=[0 for i in range(m)]
result=[0 for i in range(n)]
for i in range(n):
    A[i]=[int(x) for x in input().split()]
for i in range(m):
    vector[i]=int(input())
for i in range(n):
    for j in range(m):
        result[i] += A[i][j]*vector[j]
for _ in result:
    print(_)