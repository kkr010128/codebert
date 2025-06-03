from collections import Counter
s = input()
n = len(s)
dp = [0]
mod = 2019
a = 0
for i in range(n):
    a = a + int(s[n-i-1]) * pow(10, i, mod)
    a %= mod
    dp.append(a%mod)
ans = 0
c = Counter(dp)
for value in c.values():
    ans += value * (value-1) / 2
print(int(ans))