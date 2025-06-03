import sys
input = sys.stdin.readline
import math

big = 10 ** 9 + 7

N = int(input())
A = list(map(int, input().split()))
num = A[0]
for i in range(1, N):
    num = num * A[i] // math.gcd(num, A[i])

res = 0
for a in A:
    res += num // a

print(res % big)
