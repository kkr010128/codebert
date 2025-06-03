import sys
n, k = [int(i) for i in sys.stdin.readline().split()]
MOD = 10**9 + 7
_sum = 0
for i in range(k,n+2):
    _sum += ((n + (n-i+1)) * i // 2) - ((i-1) * i) // 2 + 1
    _sum %= MOD
print(_sum)