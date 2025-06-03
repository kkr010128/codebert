import itertools
import sys

N = int(input())
s = input().rstrip().split(' ')
L = [int(j) for j in s]

if len(L) < 3:
    print(0)
    sys.exit()

ans = 0

for i,j,k in itertools.combinations(L,3):
    if (i == j) or (i == k) or (j == k): continue
    if (i < j+k) and (j < i+k) and (k < i+j):
        ans += 1

print(ans)