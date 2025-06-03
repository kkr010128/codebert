from fractions import gcd
def lcm(a, b):
    return (a * b) // gcd(a, b)

def f(x):
    res = 0
    while x % 2 == 0:
        x //= 2
        res += 1
    return res

n, m = map(int, input().split())
a = [int(i) // 2 for i in input().split()]
t = f(a[0])
flag = True
for i in range(n):
    if f(a[i]) != t:
        flag = False
    else:
        a[i] >>= t
m >>= t
l = 1
for i in range(n):
    l = lcm(l, a[i])
    if l > m:
        flag = False
m //= l
print(-(-m // 2) if flag else 0)