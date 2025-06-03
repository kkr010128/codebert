# E - Rotation Matching

n, m = map(int, input().split())

l, r = 1, n
for i in range(m):
    if 2 * (r - l) == n or 2 * (r - l + 1) == n:
        l += 1
    print(l, r)
    l, r = l + 1, r - 1
