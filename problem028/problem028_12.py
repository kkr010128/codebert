n, m = map(int, raw_input().split())
c = map(int, raw_input().split())

INF = 1000000000

t = [INF] * (n + 1)
t[0] = 0

for i in range(m):
    for j in range(c[i], n + 1):
        t[j] = min([t[j], t[j - c[i]] + 1])

print(t[n])