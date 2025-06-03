from fractions import gcd
n, m = map(int, input().split())
aa = list(map(int, input().split()))


lcm = 1
def p2(m):
    cnt = 0
    n = m
    while 1:
        if n%2 == 0:
            cnt += 1
            n = n//2
        else:
            break
    return cnt
pp = p2(aa[0])
for a in aa:
    lcm = a * lcm // gcd(a, lcm)
    if pp != p2(a):
        lcm = 10 **18
        break
tmp = lcm // 2
print((m // tmp + 1) // 2)