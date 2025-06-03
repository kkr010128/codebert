def solve(x, y, a, b, c, p, q, r):
    p = sorted(p)[::-1]
    q = sorted(q)[::-1]
    r = sorted(r)[::-1]
    v = sorted(p[:x] + q[:y])
    n = len(v)
    t = sum(v)
    for i in range(min(n,c)):
        if v[i] < r[i]:
            t += r[i] - v[i]
    return t

x, y, a, b, c = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
print(solve(x, y, a, b, c, p, q, r))