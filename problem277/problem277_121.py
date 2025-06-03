H,W,K = map(int,input().split())
S = [input().strip() for _ in range(H)]
Ar = []
for i in range(H):
    for j in range(W):
        if S[i][j]=="#":
            Ar.append(i)
            break
Ar.append(H)
if len(Ar)==2:
    Ac = []
    for j in range(W):
        if S[Ar[0]][j]=="#":
            Ac.append(j)
    A = [[1 for _ in range(W)] for _ in range(H)]
    Ac.append(W)
    Ac[0]=0
    if len(Ac)>2:
        for k in range(len(Ac)-1):
            for j in range(Ac[k],Ac[k+1]):
                for i in range(H):
                    A[i][j] = k+1
else:
    Ac = {i:[] for i in range(len(Ar)-1)}
    for i in range(len(Ar)-1):
        for j in range(W):
            if S[Ar[i]][j]=="#":
                Ac[i].append(j)
    A = [[1 for _ in range(W)] for _ in range(H)]
    Ar[0] = 0
    cnt = 1
    for i in range(len(Ar)-1):
        Ac[i][0] = 0
        Ac[i].append(W)
        for j in range(len(Ac[i])-1):
            for j1 in range(Ac[i][j],Ac[i][j+1]):
                for i1 in range(Ar[i],Ar[i+1]):
                    A[i1][j1] = cnt
            cnt += 1
for i in range(H):
    print(*A[i])