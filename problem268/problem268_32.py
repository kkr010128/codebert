import sys
N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
mod = 10**9 + 7
ans = 1
cnt = [0] * N
for a in A:
    if a > 0:
        ans *= (cnt[a - 1] - cnt[a])
    cnt[a] += 1
    ans %= mod
for i in range(cnt[0]):
    ans *= 3 - i
print(ans % mod)