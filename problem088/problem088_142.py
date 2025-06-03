n = int(input())
a = list(map(int, input().split()))
m, s = 0, 0
for i in range(n):
    m = max(m, a[i])
    s += m - a[i]
print(s)