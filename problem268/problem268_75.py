n, *a = map(int, open(0).read().split())
mita = [0] * -~n
mita[-1] = 3
mod = 10 ** 9 + 7
c = 1
for i in range(n):
    c = c * (mita[a[i] - 1] - mita[a[i]]) % mod
    mita[a[i]] += 1
print(c)
