a, b = map(int, input().split())
x = str(a) * b
y = str(b) * a
x, y = sorted([x, y])
print(x)
