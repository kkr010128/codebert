n, k = map(int, input().split())
mod = 10 ** 9 + 7
ans = 0
coma = 1
comb = 1
for i in range(min(k+1, n)):
    ans += coma * comb
    ans %= mod
    coma *= (n-i) * pow(i+1, mod-2, mod)
    coma %= mod
    comb *= (n-i-1) * pow(i+1, mod-2, mod)
    comb %= mod

print(ans)