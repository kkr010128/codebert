def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]
mod = 10**9+7
n = I()
if n == 1:
  print(0)
else:
  ##（すべての順列）-（0をつかってないもの）-（9をつかってないもの）+（0も9もつかってないもの）
  print((10**n-2*9**n+8**n)%mod)