import sys
import math

n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

s = sum(a)
a.sort(reverse=True)
border = s / (4 * m)

ans = True

for i in range(m):
    if (a[i] >= border):
        pass
    else:
        ans = False
        break

if (ans):
    print("Yes")
else:
    print("No")
