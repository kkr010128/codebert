x, y, a, b, c = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p.sort()
q.sort()

for _ in range(x):
    r.append(p.pop())

for _ in range(y):
    r.append(q.pop())

r.sort()
ans = 0

for _ in range(x+y):
    ans += r.pop()

print(ans)
