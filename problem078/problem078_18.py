n = int(input())
state10 = 1
state9 = 1
state8 = 1
mod = 10**9 + 7
for _ in range(n):
  state10 *= 10
  state10 %= mod
  state9 *= 9
  state9 %= mod
  state8 *= 8
  state8 %= mod

ans = state10 - 2*state9 + state8
ans %= mod
print(ans)
