n = int(input())
a = list(map(int, input().split()))

ans = 0

for i in range(n):
    if i == 0:
        continue

    if a[i-1] > a[i]:
        ans += a[i-1] - a[i]
        a[i] += a[i-1] - a[i]

print(ans)
