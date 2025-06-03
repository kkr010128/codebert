

N,M,L = map(int,input().split())

A = [list(map(int,input().split()))for i in range(N)]
B = [list(map(int,input().split()))for i in range(M)]
ANS = [[0]*L for i in range(N)]

for x in range(N):
    for y in range(L):
        for z in range(M):
            ANS[x][y]+=B[z][y]*A[x][z]
            
for row in range(N):
    print("%d"%ANS[row][0],end="")
    for col in range(1,L):
        print(" %d"%(ANS[row][col]),end="")
    print()
