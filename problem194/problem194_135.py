import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
H,W = map(int,readline().split())
S = ''.join(read().decode().split())
 
INF = 10 ** 9
N = H*W
U = 250
dp = [[INF] * U for _ in range(N)]
# そのマスをいじる回数 → 総回数の最小値
dp[0] = list(range(U))
for n in range(H*W):
    for i in range(U-1,0,-1):
        if dp[n][i-1]> dp[n][i]:
            dp[n][i-1] = dp[n][i]
    for i in range(1,U):
        if dp[n][i-1] + 1 < dp[n][i]:
            dp[n][i] = dp[n][i-1] + 1
    s = S[n]
    if s == '#':
        for i in range(0,U,2):
            dp[n][i] = INF
    else:
        for i in range(1,U,2):
            dp[n][i] = INF
    x,y = divmod(n,W)
    to = []
    if y < W - 1:
        to.append(n+1)
    if x < H - 1:
        to.append(n+W)
    for m in to:
        for i in range(U):
            if dp[m][i] > dp[n][i]:
                dp[m][i] = dp[n][i]
 
print(min(dp[-1]))