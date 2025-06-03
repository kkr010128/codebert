def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]
mod = 10**9+7
import math
s = I()
t = 0
ans = 0
for i in range(1,s+1):##iは数列の項の数
  if s - 3*i <0:
    continue
  else:
    t = s-3*i
    #玉の数がt個、仕切りの数がi-1個
    ans += math.factorial(i+t-1)//(math.factorial(t)*math.factorial(i-1))
    ans = ans%mod
print(ans)