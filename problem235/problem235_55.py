from fractions import gcd
import sys

input = sys.stdin.buffer.readline
mod = 10 ** 9 + 7


def modinv(a, mod):
    return pow(a, mod - 2, mod)


n = int(input())
if n == 1:
    print(1)
    exit()
A = list(map(int, input().split()))
lcm = A[0]
for i in range(n):
    g = gcd(lcm, A[i])
    lcm *= A[i] // g
ans = 0
for i in range(n):
    gyaku = modinv(A[i], mod)
    ans += lcm * gyaku
    ans %= mod
print(ans)
