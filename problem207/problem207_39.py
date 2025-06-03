A=[list(map(int, input().split())) for _ in range(3)]
N=int(input())
B=[0]*N
for _ in range(N):
    B[_]=int(input())

G=[['.']*3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        if A[i][j] in B:
            G[i][j]='#'
# print(G)

if any(all(G[i][j]=='#' for i in range(3)) for j in range(3)) or \
   any(all(G[i][j]=='#' for j in range(3)) for i in range(3)) or \
   all(G[i][2-i]=='#' for i in range(3)) or \
   all(G[i][i]=='#' for i in range(3)):
    print('Yes')
else:
    print('No')