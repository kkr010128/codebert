n,m = map(int,input().split())
A=[[] for i in range(n)]
for i in range(n):
    A[i] = list(map(int,input().split()))
b = []
c = list(map(int,'0'*n))
for i in range(m):
    b.append(int(input())) 
for i in range(n):
    for j in range(m):
        c[i] += A[i][j]*b[j]
for i in range(n):      
    print(c[i])
