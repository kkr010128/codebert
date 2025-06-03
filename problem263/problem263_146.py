N, *A = map(int, open(0).read().split())

mod = 10 ** 9 + 7
ans = 0
for bit in range(60):
    ctr = [0, 0]
    for i in range(N):
        ctr[A[i] >> bit & 1] += 1
    ans += (1 << bit) * (ctr[0] * ctr[1])
    ans %=mod
print(ans)
