n, m = [int(el) for el in input().split(' ')]
c = [int(el) for el in input().split(' ')]

t = [0] + [float('inf') for _ in range(n)]

for i in range(m):
    for j in range(c[i], n+1):
        t[j] = min(t[j], t[j-c[i]] + 1)
print(t[n])