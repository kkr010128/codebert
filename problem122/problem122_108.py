n = int(raw_input())
a = [int(x) for x in raw_input().split()]
q = int(raw_input())
op = []
for _ in xrange(q):
    v = raw_input().split()
    op.append([int(x) for x in v])

d = {}
total = 0
for v in a:
    d[v] = d.get(v, 0) + 1
    total += v

for src, dest in op:
    c = d.pop(src, 0)
    d[dest] = d.get(dest, 0) + c
    total += c * (dest - src)
    print total