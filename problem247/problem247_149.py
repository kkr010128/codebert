n, m = map(int, input().split())
a = list(map(int, input().split()))

num1 = a[0]
num2 = 0
while num1 % 2 == 0:
    num1 //= 2
    num2 += 1
gc = 2 ** num2

b = []
for i in a:
    if i % gc != 0 or (i // gc) % 2 == 0:
        print(0)
        exit()
    else:
        b.append(i // gc)

from fractions import gcd
lcm = 1
for i in b:
    lcm = (lcm * i) // gcd(lcm, i)

ans = m // (lcm * (gc // 2))
ans = (ans + 1) // 2
print(ans)