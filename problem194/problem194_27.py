H,W=map(int,input().split())

def g(j):
    if j==".":
        return 1 #白
    else:
        return 0 #黒
    
S=[]
for j in range(H):
    S.append(list(map(g,input())))


Z=[[0]*W for i in range(H)]

for y in range(H):
    if y==0:
        for x in range(W):
            if x==0:
                Z[0][0]=1-S[0][0]
            else:
                Z[y][x]=Z[y][x-1]+(S[y][x-1]==1 and S[y][x]==0)
    else:
        for x in range(W):
            if x==0:
                Z[y][x]=Z[y-1][x]+(S[y-1][x]==1 and S[y][x]==0)
            else:
                Z[y][x]=min(Z[y][x-1]+(S[y][x-1]==1 and S[y][x]==0),Z[y-1][x]+(S[y-1][x]==1 and S[y][x]==0))

print(Z[H-1][W-1])