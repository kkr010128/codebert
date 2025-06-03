def gcd(x, y):
    while y > 0:
        r = x % y
        x = y
        y = r
    return x

def lcm(x, y):
    return x // gcd(x, y) * y

n, m = map(int, input().split())
a = list(map(int, input().split()))

l = 1
for i in range(n):
    a[i] //= 2
    l = lcm(a[i], l)

flg = True
for x in a:
    if (l // x) % 2 == 0:
        flg = False
        break

if flg:
    print(m // l - m // (l * 2))
else:
    print(0)