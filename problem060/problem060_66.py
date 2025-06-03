n,m,l=map(int,input().split())
A=[list(map(int,input().split())) for i in range(n)]
B=[list(map(int,input().split())) for i in range(m)]
C=[[0]*l for i in range(n)]

for x in range(n):
    for y in range(l):
        for z in range(m):
            C[x][y] += A[x][z]*B[z][y]

for row in range(n):
    print("%d"%(C[row][0]),end="")
    for col in range(1,l):
        print(" %d"%(C[row][col]),end="")
    print()

