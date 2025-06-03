MOD = 10 ** 9 + 7

N, K = map(int, input().split())
lst = [0] * (K + 1)
ans = 0
for i in range(K, 0, -1):
    tmp = K // i
    tmp = pow(tmp, N, MOD)
    for j in range(2 * i, K + 1, i):
        tmp -= lst[j]
    ans += (i * tmp)
    ans %= MOD
    lst[i] = tmp

print (ans)
