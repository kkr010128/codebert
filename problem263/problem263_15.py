N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(60):
    cnt1 = 0
    for j in range(N):
        cnt1 += (A[j]>>i)&1
    ans += cnt1 * (N-cnt1) * 2**i
    ans %= 10**9+7

print(ans)