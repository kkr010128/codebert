n,m=map(int,raw_input().split())
A=[]
b=[]
for i in range(n):
    A.append(map(int,raw_input().split()))
for i in range(m):
    b.append(input())
for i in range(n):
    sum=0
    for j in range(m):
        sum+=A[i][j]*b[j]
    print('%d'%sum)