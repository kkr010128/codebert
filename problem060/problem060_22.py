n,m,l=map(int,input().split())
a=[list(map(int,input().split(" "))) for i in range(n)]
b=[list(map(int,input().split(" "))) for i in range(m)]
c=[[0]*l for i in range(n)]

for i in range(n):
    for j in range(l):
        for k in range(m):
            c[i][j]=c[i][j]+a[i][k]*b[k][j]
for d in range(n):
    print(c[d][0],end="")
    for e in range(1,l):
        print(" %d"%c[d][e],end="")

    print()
    
        

            
    
