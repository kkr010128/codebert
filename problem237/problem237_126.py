n = int(input())
L = []
for _ in range(n):
    x, l = map(int, input().split())
    left = x - l
    right = x + l
    L.append((left, right))
L = sorted(L, key=lambda x: x[1])
ans = 0
prev = -float('inf')
for r in L:
    if r[0] >= prev:
        ans += 1
        prev = r[1]
print(ans)
