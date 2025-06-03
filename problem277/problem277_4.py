H,W,K,*s = open(0).read().split()
H = int(H)
W = int(W)
K = int(K)
ans = [[0] * W for _ in range(H)]
using = 0
unpainted = -1
for i in range(H):
    appeared = -1
    for j in range(W):
        if s[i][j] == '#':
            if appeared < 0:
                appeared = 1
                using += 1
                for k in range(j+1):
                    ans[i][k] = using
            else:
                using += 1
                ans[i][j] = using
        else:
            if appeared > 0:
                ans[i][j] = using
    if appeared < 0:
        if using > 0:
            ans[i] = ans[i-1]
        else:
            unpainted += 1
if unpainted >= 0:
    for i in range(unpainted,-1,-1):
        ans[i] = ans[i+1]
for x in ans:
    print(*x)
