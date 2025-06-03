N = int(input())
A = list(map(int, input().split()))
MOD = 10**9+7
num_one_for_digit = [0]*61
for i in range(N):
    b = bin(A[i])[2:].zfill(61)
    for d in range(61):
        if b[d] == "1":
            num_one_for_digit[d] += 1
ans = 0
t = 1
for d in range(60, -1, -1):
    n_1 = num_one_for_digit[d]
    ans += n_1 * (N - n_1) * t % MOD
    ans %= MOD
    t *= 2
print(ans%MOD)