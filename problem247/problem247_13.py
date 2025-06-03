from fractions import gcd
import sys
n, m = map(int, input().split())
a = [int(i) for i in input().split()]
b = [i // 2 for i in a]
def div2check(i):
    count = 0
    while i % 2 == 0:
        count += 1
        i //= 2
    return count
c = [div2check(i) for i in b]
if c.count(c[0]) != n:
    print(0)
    sys.exit()

lcm = b[0]
for i in b[1:]:
    lcm = lcm * i // gcd(lcm, i)
print((m // lcm + 1) // 2)