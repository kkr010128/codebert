from math import gcd

n, m = map(int, input().split())
A = list(map(int, input().split()))
A = [a//2 for a in  A]
lcm = 1

for i in range(n):
    lcm = lcm * A[i] // gcd(lcm, A[i])
    if lcm > m:
        print(0)
        exit()
        
for a in A:
    if lcm // a % 2 == 0:
        print(0)
        exit()

print((m//lcm + 1) // 2)
