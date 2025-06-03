# A - Range Flip Find Route
H,W = map(int,input().split())
INF = 1000000
s = [input() for _ in range(H)]
a = [[INF]*(W+1) for _ in range(H+1)]
for i in range(1,H+1):
    for j in range(1,W+1):
        if (i,j)==(1,1):
            a[i][j] = int(s[0][0]=='#')
        elif i==1:
            a[i][j] = a[i][j-1]+int(s[i-1][j-2]=='.' and s[i-1][j-1]=='#')
        elif j==1:
            a[i][j] = a[i-1][j]+int(s[i-2][j-1]=='.' and s[i-1][j-1]=='#')
        else:
            a[i][j] = min(
                a[i][j-1]+int(s[i-1][j-2]=='.' and s[i-1][j-1]=='#'),
                a[i-1][j]+int(s[i-2][j-1]=='.' and s[i-1][j-1]=='#')
            )
print(a[H][W])