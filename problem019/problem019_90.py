time = 0
n, q = map(int, input().split())
qname = list(range(n))
qtime = list(range(n))
ename = []
etime = []
for i in range(n):
    inp = input().split()
    qname[i], qtime[i] = inp[0], int(inp[1])
while len(qtime) > 0:
    if qtime[0] <= q:
        time += qtime.pop(0)
        ename.append(qname.pop(0))
        etime.append(time)
    else:
        time += q
        qname.append(qname.pop(0))
        qtime.append(qtime.pop(0)-q)
for (a, b) in zip(ename, etime):
    print(a, b)