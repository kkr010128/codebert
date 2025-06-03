import math

def solve(x):
    y = 0
    for i in range(n):
        if a[i] >= x / f[i]:
            y += math.ceil(a[i] - x / f[i])
    if y <= k:
        return True
    else:
        return False

def binary_search(c1, c2):
    m = (c1 + c2 + 1) // 2
    if abs(c1 - c2) <= 1:
        return m
    else:
        if solve(m):
            c1 = m
        else:
            c2 = m
        return binary_search(c1, c2)

n, k = map(int, input().split())
a = list(map(int, input().split()))
f = list(map(int, input().split()))
a.sort()
f.sort(reverse = True)
M = 0
for i in range(n):
    M = max(M, a[i] * f[i])
ans = binary_search(M, -1)
print(ans)