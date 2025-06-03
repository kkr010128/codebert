n = int(input())
a, b = [0] * n, [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())
a.sort()
b.sort()
if n % 2:
    min_m, max_m = a[n // 2], b[n // 2]
    ans = max_m - (min_m - 1)
else:
    min_m2 = a[n // 2] + a[n // 2 - 1]
    max_m2 = b[n // 2] + b[n // 2 - 1]
    ans = max_m2 - min_m2 + 1
print(ans)