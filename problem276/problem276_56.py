import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = [int(x) for x in input().split()]

from itertools import accumulate

a_csum = list(accumulate(a))

ans = 10**10

for i in range(n - 1):
    ans = min(ans, abs(a_csum[i] - (a_csum[-1] - a_csum[i])))

print(ans)