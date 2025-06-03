H,W = map(int, input().split())
S = [input() for _ in range(H)]

inf = 10**6
L = [[inf]*W for _ in range(H)]
if S[0][0] == ".":
    L[0][0] = 0
else:
    L[0][0] = 1

for i in range(H):
    for j in range(W):
        n1 = inf
        n2 = inf
        if i > 0:
            if S[i-1][j] == "." and S[i][j] == "#":
                n1 = L[i-1][j] + 1
            else:
                n1 = L[i-1][j]
        if j > 0:
            if S[i][j-1] == "." and S[i][j] == "#":
                n2 = L[i][j-1] + 1
            else:
                n2 = L[i][j-1]
        L[i][j] = min(L[i][j], n1, n2)

print(L[-1][-1])