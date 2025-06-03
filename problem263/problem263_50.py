
MOD = 10 ** 9 + 7
MAX = 60

n = int(input())
a = list(map(int, input().split()))

cnt = [0 for i in range(MAX)]
for i in range(n):
    bit = bin(a[i])[2:].zfill(MAX)
    for j in range(MAX):
        cnt[j] += int(bit[j])

ans = 0
for i in range(MAX):
    ans += cnt[MAX - i - 1] * (n - cnt[MAX - i - 1]) * 2 ** i
    ans %= MOD
print(ans)
