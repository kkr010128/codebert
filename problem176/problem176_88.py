n, k = map(int, input().split())
ans = 0

cnt = dict(zip(range(1,k+1), [0] * k))
for i in range(1, k+1)[::-1]:
    cnt[i] = pow((k // i), n, 10**9+7)

    for j in range(2*i, k+1, i):
        cnt[i] -= cnt[j]
    
    ans += i * cnt[i]

print(ans % (10 ** 9 + 7))