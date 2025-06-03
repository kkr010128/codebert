X, Y, A, B, C = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p.sort(reverse=True)
q.sort(reverse=True)
r.sort(reverse=True)

p = p[:X]
q = q[:Y]

all = p + q + r
all.sort(reverse=True)
ans = sum(all[:X + Y])
print(ans)
