n = int(input())

p, q = [], []
for _ in range(n):
    x, y = map(int, input().split())
    p.append(x + y)
    q.append(x - y)

p.sort()
q.sort()
print(max(max(p) - min(p), max(q) - min(q)))