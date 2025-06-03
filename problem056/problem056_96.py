n,m=map(int,raw_input().split())
a,b=[],[]
for i in range(n):a.append(map(int,raw_input().split()))
for i in range(m):b.append(input())
for i in range(n):
    ans=0
    for j in range(m): ans+=a[i][j]*b[j]
    print ans