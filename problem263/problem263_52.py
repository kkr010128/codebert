import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

MOD = 10 ** 9 + 7

N = int(input())
A = list(map(int, input().split()))
B = [bin(a) for a in A]

maxA = max(A)
mask = 1

count = 0
i = 0
while maxA >> i:
    zeros = sum([1 for a in A if (mask * 2**i) & a == 0]) % MOD
    ones = (len(A) - zeros) % MOD
    count += zeros * ones * ((2**i) % MOD)
    count %= MOD
    i += 1

print(count)