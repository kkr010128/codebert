N = int(input())
A = list(map(int, input().split()))

mod = int(1e9+7)

CNT = [0] * (N+10)
CNT[-1] = 3
ans = 1
for a in A:
  CNT[a] += 1
  ans *= CNT[a-1]
  ans %= mod
  CNT[a-1] -= 1

print(ans)