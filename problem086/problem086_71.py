N, X, T = map(int,input().split())

add = 0
if N % X > 0:
  add = 1

ans = int(N//X + add)*T
print(ans)