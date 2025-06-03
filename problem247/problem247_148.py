from fractions import gcd
n, m = map(int, input().split())
a = [int(i) // 2 for i in input().split()]
x = 1
for i in range(n):
    x *= a[i] // gcd(x, a[i])
for i in a:
    if x // i % 2 == 0:
        print(0)
        exit()
print((m // x + 1) // 2)