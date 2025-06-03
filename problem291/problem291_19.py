a, b = map(int, input().split())
if a <= 2 * b:
    x = 0
else:
    x = a - 2 * b
print(int(x))