mod = 10 ** 9 + 7
x, y = map(int, input().split())
if (x + y) % 3 != 0 or x * 2 < y or y * 2 < x:
    print(0)
    exit()
l = [1]
for i in range(1, (x + y) // 3 + 100):
    l.append(l[-1] * i % mod)
def comb(n, r, m):
    return l[n] * pow(l[r], m - 2, m) * pow(l[n - r], m - 2, m) % m
a, b = y - (x + y) // 3, x - (x + y) // 3
print(comb(a + b, a, mod) % mod)