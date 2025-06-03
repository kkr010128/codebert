def f(x, y):
    if x % y == 0:
        return y
    return f(y, x % y)
a = []
while True:
    try:
        a.append(list(map(int, input().split())))
    except EOFError:
        break
for i in a:
    g = f(i[0], i[1])
    l = (i[0] * i[1]) / g
    print(g, int(l))

