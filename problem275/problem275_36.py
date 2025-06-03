x, y = map(int, input().split())
a = max(0, 100000 * (4 - x))
b = max(0, 100000 * (4 - y))
c = 400000 if x == 1 and y == 1 else 0
print(a + b + c)
