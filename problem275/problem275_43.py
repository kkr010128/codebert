x, y = map(int, input().split())
if x == 1 and y == 1:
    print(100000 * (8 - (x + y)) + 400000)
elif x <= 3 and y <= 3:
    print(100000 * (8 - (x + y)))
elif x <= 3:
    print(100000 * (4 - x))
elif y <= 3:
    print(100000 * (4 - y))
else:
    print(0)