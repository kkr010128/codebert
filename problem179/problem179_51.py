n, m = map(int, input().split())
a = sorted(map(int, input().split()))[::-1]
i = 0
for j in range(n):
    i = i + a[j]
x = i / (4 * m)
print("Yes" if a[m - 1] >= x else "No")