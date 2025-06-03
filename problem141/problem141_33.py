n = int(input())
a = list(map(int, input().split()))
if n == 0 and a[0] != 1:
    print(-1)
    exit(0)
b = [0] * (n + 2)
for i in range(n, 0, -1):
    b[i - 1] = b[i] + a[i]
t = 1 - a[0]
ans = 1
for i in range(n):
    m = min(t * 2, b[i])
    if m < a[i + 1]:
        print(-1)
        exit(0)
    ans += m
    t = m - a[i + 1]
print(ans)
