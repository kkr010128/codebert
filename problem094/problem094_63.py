import sys
mod=10**9+7 ; inf=float("inf")
from math import sqrt, ceil
from collections import deque, Counter, defaultdict #すべてのkeyが用意されてる defaultdict(int)で初期化
# input=lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(11451419)
from decimal import ROUND_HALF_UP,Decimal  #変換後の末尾桁を0や0.01で指定
  #Decimal((str(0.5)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
from functools import lru_cache
#メモ化再帰defの冒頭に毎回 @lru_cache(maxsize=10**10)
#引数にlistはだめ
#######ここまでテンプレ#######
#ソート、"a"+"b"、再帰ならPython3の方がいい
#######ここから天ぷら########

h,w,k=map(int,input().split())
# R=[]
A=[[0]*w for i in range(h)]
dp=[[[0 for j in range(w)] for i in range(h)] for i in range(4)]

for s in sys.stdin.readlines():
    x,y,v=map(int,s.split())
    x-=1;y-=1
    A[x][y]=v
    # dp[x][y][1]=v
    # dp[x][y][2]=v
    # dp[x][y][3]=v;
dp[1][0][0]=A[0][0]
for i in range(h):
    for j in range(w):
        for k in range(4):
            here=dp[k][i][j]
            if i<h-1:
                dp[0][i+1][j] = max(here,dp[0][i+1][j])
                dp[1][i+1][j] = max(here+A[i+1][j], dp[1][i+1][j])
            if j<w-1:
                dp[k][i][j+1] = max(dp[k][i][j+1], here)
                if k<=2:
                    dp[k+1][i][j+1]= max(dp[k+1][i][j+1],here+ A[i][j+1])
ans=0
for i in range(4):
    ans=max(ans, dp[i][-1][-1])
print(ans)