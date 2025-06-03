N = int(input())
XYS = [list(map(int, input().split())) for _ in range(N)]
s = 0
def perm(ns):
    acc = []
    def fill(ms, remains):
        if remains:
            for m in remains:
                fill(ms + [m], [x for x in remains if x != m])
        else:
            acc.append(ms)
    fill([], ns)
    return acc

s = 0
for indexes in perm(list(range(N))):
    xys = [XYS[i] for i in indexes]
    x0, y0 = xys[0]
    for x1, y1 in xys:
        s += ((x0 - x1)**2 + (y0 - y1)**2) ** 0.5
        x0 = x1
        y0 = y1

nf = 1
for i in range(1, N+1):
    nf *= i
ans = s / nf

print(ans)