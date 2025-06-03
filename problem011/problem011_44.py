def GSD(x, y):
    while True:
        x0 = max(x, y)
        y0 = min(x, y)
        if x0 % y0 == 0:
            return y0
        x = x0 % y0
        y = y0
x, y = map(int, input().split(' '))
print(GSD(x, y))
