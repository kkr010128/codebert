N = int(input())
a = list(map(int, input().split()))
MOD = 10**9+7
ans = 0
for j in range(60):
    count = 0
    for i in range(len(a)):
        a[i], pre = divmod(a[i], 2)
        count += pre
    ans += count*(N-count)*2**j
    ans %= MOD
print(ans)