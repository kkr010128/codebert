H,W,K = map(int,input().split())
S = [input() for i in range(H)]

ans = [[None]*W for _ in range(H)]
v = 0
for i,row in enumerate(S):
    sp = row.split('#')
    if len(sp)==1: continue
    if len(sp)==2:
        v += 1
        for j in range(W):
            ans[i][j] = v
        continue
    j = 0
    for k,a in enumerate(sp):
        if k==len(sp)-1:
            for _ in range(len(a)):
                ans[i][j] = v
                j += 1
        else:
            v += 1
            for _ in range(len(a)+1):
                ans[i][j] = v
                j += 1

i = 0
while ans[i][0] is None:
    i += 1
for ii in range(i):
    for j in range(W):
        ans[ii][j] = ans[i][j]

for i in range(1,H):
    if ans[i][0] is None:
        for j in range(W):
            ans[i][j] = ans[i-1][j]

for row in ans:
    print(*row)