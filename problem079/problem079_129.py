s = int(input())
mod = 10**9 + 7
a = [0] * (2001)
a[3] = a[4] = a[5] = 1
for i in range(6, s + 1):
    a[i] = a[i - 1] + a[i - 3]
    a[i] %= mod
print(a[s])
