def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

n, m = map(int, input().split())
a = list(map(int, input().split()))
l = a[0] // 2
for i in range(n):
    a[i] //= 2
    l = lcm(l, a[i])
c = 0
while True:
    for i in range(n):
        if a[i] % 2 == 1:
            c += 1
        else:
            a[i] //= 2
    if not c == 0:
        break
print(((m // l) + 1) // 2 if c == n else 0)