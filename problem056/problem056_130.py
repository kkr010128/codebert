n,m=map(int,raw_input().split())

A = [[0 for j in range(m)] for i in range(n)]
b = [0 for j in range(m)]

for i in range(n):
    A[i]=map(int, raw_input().split())
for j in range(m):
    b[j]=input()
 
for i in range(n):
    c=0
    for j in range(m):
        c+=A[i][j]*b[j]
    print(c)