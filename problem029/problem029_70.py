x1, y1, x2, y2 = map(float, input().split())

x = abs(x2 - x1)
y = abs(y2 - y1)

dis = (x ** 2 + y ** 2) ** (1 / 2)
dis = round(dis, 8)

print("{}" .format(dis))
