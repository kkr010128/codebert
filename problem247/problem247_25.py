def gcd(a, b):
    if a < b:
        return gcd(b, a)
    while b > 0:
        a, b = b, a % b
    return a

n, m = map(int, input().split())
a = list(map(int, input().split()))

x = 1
for i in range(n):
    b = a[i] // 2
    x = x * b // gcd(x, b)
if any(2 * x // y % 2 == 0 for y in a):
    print(0)
    quit()
print((m - x) // (2 * x) + 1)


