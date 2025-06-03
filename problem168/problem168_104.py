n, m = map(int, input().split())
a = list(map(int, input().split()))
x = 0
for i in range(m):
    x += a[i]
if n - x >= 0:
    print(n - x)
else:
    print(-1)