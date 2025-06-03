MOD = 10 ** 9 + 7
X, Y = map(int, input().split())

if (X + Y) % 3 or Y > 2 * X or Y < X // 2:
    print(0)
    exit()

n = (X + Y) // 3
r = X - (X + Y) // 3
num, den = 1, 1
if n - r < r:
    r = n - r
for i in range(1, r + 1):
    num *= n - i + 1
    num %= MOD
    den *= i
    den %= MOD

print((num * pow(den, MOD - 2, MOD)) % MOD)