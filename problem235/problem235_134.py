import sys
import fractions
input = sys.stdin.readline


mod = 10 ** 9 + 7
N = int(input().strip())
A = list(map(int, input().strip().split(" ")))

lcm = 1
for a in A:
    lcm = a // fractions.gcd(a, lcm) * lcm

print(sum([lcm // a for a in A]) % mod)