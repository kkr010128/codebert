import sys

nm = input().split()
N = int(nm[0])
M = int(nm[1])

As = [int(a) for a in input().split()]

s = sum(As)

if N >= s:
    ans = N - s
    print(ans)
else:
    print("-1")

