def II(): return int(input())
def MI(): return map(int, input().split())
A,B,N=MI()
def f(x):
  return A*x//B-A*(x//B)
if B-1<=N:
  ans=f(B-1)
else:
  ans=f(N)
print(ans)