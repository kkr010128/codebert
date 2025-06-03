n, m = map(int, input().split())
h = list(map(int, input().split()))
a = [0] * m
b = [0] * m

ok = [True]*n

for i in range(m):
    a[i], b[i] = map(int, input().split())

    if h[a[i]-1] <= h[b[i]-1]:
        ok[a[i]-1] = False
    if h[b[i]-1] <= h[a[i]-1]:
        ok[b[i]-1] = False

ans = 0
for i in range(n):
    if ok[i] == True:
        ans += 1

print(ans)
