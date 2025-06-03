import math

def koch(start, end, n, r):
    if n > 0:
        #途中の頂点をa, b, cとする
        a = [(start[0]*2 + end[0]*1) / 3, (start[1]*2 + end[1]*1) / 3]
        c = [(start[0]*1 + end[0]*2) / 3, (start[1]*1 + end[1]*2) / 3]

        x = c[0] - a[0]
        y = c[1] - a[1]

        b = [x * math.cos(math.pi/3) - y * math.sin(math.pi/3) + a[0], x * math.sin(math.pi/3) + y * math.cos(math.pi/3) + a[1]]

        koch(start, a, n-1, r)
        koch(a, b, n-1, r)
        koch(b, c, n-1, r)
        koch(c, end, n-1, r)

    else:
        r.append(start)

n = int(input())

r = []

koch([0, 0], [100, 0], n, r)
r.append([100, 0])

for rr in r:
    print(str(rr[0]) + ' ' + str(rr[1]))
