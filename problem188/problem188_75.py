X, Y, A, B, C = map(int, input().split())
ps = list(map(int, input().split()))
qs = list(map(int, input().split()))
rs = list(map(int, input().split()))
ps = sorted(ps, reverse=True)[:X]
qs = sorted(qs, reverse=True)[:Y]
rs = sorted(ps+qs+rs, reverse=True)[:X+Y]
r = sum(rs)
print(r)
