from sys import stdin
input = lambda: stdin.readline().rstrip()
na, nb, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
min_a = min_b = 10**9
for i in range(na):
    min_a = min(min_a, a[i])
for i in range(nb):
    min_b = min(min_b, b[i])
ans = min_a + min_b
for i in range(m):
    x, y, c = map(int, input().split())
    x -= 1
    y -= 1
    ans = min(ans, a[x] + b[y] - c)
print(ans)
