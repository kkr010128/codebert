from math import gcd

n, m = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
B = [a // 2 for a in set(A)]

lcm = 1
div2_count = -1
for b in B:
    lcm = lcm * b // gcd(lcm, b)
    if lcm > m:
        print(0)
        exit()
    count = 0
    while b % 2 == 0:
        b //= 2
        count += 1
    if div2_count == -1 or div2_count == count:
        div2_count = count
    else:
        print(0)
        exit()

limit = m // lcm
ans = (limit + 1) // 2
print(ans)