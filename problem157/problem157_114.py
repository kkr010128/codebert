from collections import *

N = int(input())
A = list(map(int, input().split()))
ans = 0
c = Counter()

for i in range(1, N+1):
    ans += c[i-A[i-1]]
    c[i+A[i-1]] += 1

print(ans)