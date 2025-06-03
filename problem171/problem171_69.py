N = int(input())
a = map(int,input().split())
A = sorted([(b,a) for a, b in enumerate(a)])[::-1]
dp = [[-1 for _ in range(N+10)]for _ in range(N+10)]
#dp[x][y]: 活発度順でx+y人詰めた時,左にx人右にy人詰めたときの最大値
dp[0][0] = 0
import sys
sys.setrecursionlimit(100000000)

def memo(x, y):
    if x < 0 or y < 0: return -1000000000000 #ありえん
    if dp[x][y] != -1: return dp[x][y]
    val, pre = A[x+y-1][0], A[x+y-1][1]
    dp[x][y] = max(
            #x-1からくるパターン
            memo(x - 1,y) + abs(pre - (x - 1)) * val,
            #y-1からくるパターン
            memo(x, y - 1) + abs(pre - (N - y )) *val,
            )
    return dp[x][y]
ans = 0
for i in range(N): ans = max(ans, memo(i,N - i))
print(ans)
