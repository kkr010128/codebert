import sys
from fractions import gcd

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def merge(a, b):
    g = gcd(a, b)
    a //= g
    b //= g
    if a % 2 == 0:
        return 0
    if b % 2 == 0:
        return 0
    n = a * b * g
    if n > 10 ** 9:
        return 0
    return n


n, m = map(int, readline().split())
a = list(map(int, readline().split()))

a = [x >> 1 for x in a]

for i in range(n-1):
    a[i+1] = merge(a[i], a[i+1])

z = a[n-1]

if z == 0:
    print("0")
else:
    ans = (m//z) - (m//(z+z))
    print(ans)
