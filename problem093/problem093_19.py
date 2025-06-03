import sys
mod=10**9+7 ; inf=float("inf")
from math import sqrt, ceil
from collections import deque, Counter, defaultdict #すべてのkeyが用意されてる defaultdict(int)で初期化
input=lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(11451419)
from decimal import ROUND_HALF_UP,Decimal  #変換後の末尾桁を0や0.01で指定
  #Decimal((str(0.5)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
from functools import lru_cache
#メモ化再帰defの冒頭に毎回 @lru_cache(maxsize=10**10)
#引数にlistはだめ
#######ここまでテンプレ#######
#ソート、"a"+"b"、再帰ならPython3の方がいい
#######ここから天ぷら########


n,k=map(int,input().split())
P=list(map(int,input().split()))
P=[i-1 for i in P]
C=list(map(int,input().split()))
ans=-inf
for i in range(n):
    now=i
    total=0
    roop= 0
    po=deque([0])
    for kai in range(1,k+1):
        now=P[now]
        total += C[now]
        roop+=1
        po.append(total)
        ans=max(ans, total)
        if now == i:
            la= kai;break

    else: continue
    if total<0 : continue
    po=list(po)
    ans=max(ans, total* (k//roop) + max(po[:k%roop+1]), total*(k//roop-1) + max(po))
    #print(total, roop,po ,ans)
print(ans)