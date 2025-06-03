N, *XY = map(int, open(0).read().split())

XY = [(x, y) for x, y in zip(*[iter(XY)] * 2)]
XY = list(set(XY))

Ax, Ay = max(XY, key=lambda t: t[0] + t[1])
Bx, By = max(XY, key=lambda t: -t[0] + t[1])
Cx, Cy = max(XY, key=lambda t: t[0] - t[1])
Dx, Dy = max(XY, key=lambda t: -t[0] - t[1])

print(max(
    max(abs(x - Ax) + abs(y - Ay),
        abs(x - Bx) + abs(y - By),
        abs(x - Cx) + abs(y - Cy),
        abs(x - Dx) + abs(y - Dy),
    ) for x, y in XY
))