n, m = map(int, input().split())
h = list(map(int, input().split()))
to = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    to[a - 1] += [b - 1]
    to[b - 1] += [a - 1]
print(sum(to[j] == [] or h[j] > max(h[i] for i in to[j]) for j in range(n)))