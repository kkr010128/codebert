s=list(input()) ;k=int(input()) ;n=len(s)
ss=s*2
import sys
mod=10**9+7 ; inf=float("inf")
from math import sqrt, ceil
from collections import deque, Counter, defaultdict #すべてのkeyが用意されてる defaultdict(int)で初期化
input=lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(11451419)
from decimal import ROUND_HALF_UP,Decimal as D  #変換後の末尾桁を0や0.01で指定
  #Decimal((str(0.5)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
from functools import lru_cache
from bisect import bisect_left as bileft, bisect_right as biright
from fractions import Fraction as F  #F(a,b)で正確なa/b
#メモ化再帰defの冒頭に毎回 @lru_cache(maxsize=10**10)
#引数にlistはだめ
#######ここまでテンプレ#######
#ソート、"a"+"b"、再帰ならPython3の方がいい
#######ここから天ぷら########


if n==1:
    print(k//2);exit()

def qq(s,n):
    ans=0
    if n==2:
        if s[0]==s[1]:return 1
        return 0
    nows=s[0];now=1
    for i in range(1,n):
        if s[i]==nows:
            now+=1
        else:
            ans+= now//2
            now=1 ;nows=s[i]
    else:
        ans+=now//2
    return ans 

if len(Counter(s))==1:
    print((n*k)//2)
    exit()
if s[0]!=s[-1]:
    print(qq(s,n)*k)
    exit()
st=1; go=1
for i in range(1,n):
    if s[i]==s[0]:
        st+=1
    else:
        break
for i  in range(-2,-n-1,-1):
    if s[i]==s[-1]:
        go+=1
    else:break
print(qq(s,n)*k - (st//2+go//2-(st+go)//2)*(k-1))
