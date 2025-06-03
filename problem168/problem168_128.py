n, m = map(int, input().split())
a = list(map(int, input().split()))

total = 0
for i in range(m):
    total = total + a[i]
if (n -total) < 0:
    print(-1)
else:
    print(n - total)