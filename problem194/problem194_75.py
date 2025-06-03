h, w = map(int, input().split())
S = []
for _ in range(h):
    s = str(input())
    S.append(s)

DP = [[0 for _ in range(w)] for _ in range(h)]

if S[0][0] == '.':
    DP[0][0] = 0
else:
    DP[0][0] = 1

ren = False
if DP[0][0] == 1:
    ren = True

for i in range(1,h):
    if S[i][0] == '.':
        DP[i][0] = DP[i-1][0]
        ren = False
    elif ren == False and S[i][0] == '#':
        DP[i][0] = DP[i-1][0] + 1
        ren = True
    elif ren == True and S[i][0] == '#':
        DP[i][0] = DP[i-1][0]
        ren = True

ren = False
if DP[0][0] == 1:
    ren = True
for j in range(1,w):
    if S[0][j] == '.':
        DP[0][j] = DP[0][j-1]
        ren = False
    elif ren == False and S[0][j] == '#':
        DP[0][j] = DP[0][j-1] + 1
        ren = True
    elif ren == True and S[0][j] == '#':
        DP[0][j] = DP[0][j-1]
        ren = True

for i in range(1,h):
    for j in range(1,w):
        if S[i][j] == '.':
            DP[i][j] = min(DP[i-1][j], DP[i][j-1])
        elif S[i][j] == '#':
            res_i = 0
            res_j = 0
            if S[i-1][j] == '.':
                res_i = 1
            if S[i][j-1] == '.':
                res_j = 1
            DP[i][j] = min(DP[i-1][j] + res_i, DP[i][j-1] + res_j)

print(DP[h-1][w-1])