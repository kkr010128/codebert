
N = int(input())
X = list(map(int, input().split()))

MOD = 10 ** 9 + 7
ans = 0
for b in range(61):
    ctr = [0, 0]
    for i in range(N):
        ctr[X[i] >> b & 1] += 1

    ans += (1 << b) * ctr[0] * ctr[1]
    ans %= MOD

print(ans)
