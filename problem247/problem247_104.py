from math import gcd
N, M = map(int, input().split())
A = [a//2 for a in map(int, input().split())]

lcm = 1
for a in A:
    lcm = lcm*a//gcd(lcm, a)
    if lcm > M:
        print(0)
        exit()

for a in A:
    div = lcm//a
    if div % 2 == 0:
        print(0)
        exit()

ans = (M//lcm+1)//2
print(ans)
