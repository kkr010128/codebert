k, n = list(map(int, input().split()))
a = list(map(int, input().split()))
d = []
for i in range(n):
    if i == n - 1:
        d.append(a[0] + (k - a[i]))
    else:
        d.append(a[i + 1] - a[i])
d.sort()
print(sum(d[:-1]))