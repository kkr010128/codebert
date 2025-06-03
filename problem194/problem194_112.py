H, W = map(int, input().split())
S = [list(input()) for h in range(H)]
table = [[0 for w in range(W)] for h in range(H)]

table[0][0] = int(S[0][0]=='#')
for i in range(1, H):
    table[i][0] = table[i-1][0] + int(S[i-1][0]=='.' and S[i][0]=='#')
for j in range(1, W):
    table[0][j] = table[0][j-1] + int(S[0][j-1]=='.' and S[0][j]=='#')
for i in range(1, H):
    for j in range(1, W):
        table[i][j] = min(table[i-1][j] + int(S[i-1][j]=='.' and S[i][j]=='#'),
         table[i][j-1] + int(S[i][j-1]=='.' and S[i][j]=='#'))

print(table[-1][-1])