N, K = map(int, input().split())
mod = 10 ** 9 + 7
cnt = [0] * (K + 1)
answer = 0
for i in range(K, 0, -1):
    tmp = pow(K // i, N, mod) - sum(cnt[::i])
    cnt[i] = tmp
    answer = (answer + tmp * i) % mod

print(answer)
