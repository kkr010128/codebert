from fractions import gcd

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = [a[i]//2 for i in range(n)]
lcm_a = 1
for i in range(n):
    lcm_a = (lcm_a * b[i]) // gcd(lcm_a, b[i])
for i in range(n):
    if (lcm_a//b[i]) % 2 == 0:
        print(0)
        exit()
if m < lcm_a:
    print(0)
else:
    m -= lcm_a
    print(1 + m // (lcm_a*2))