x, y = map(int, input().split())

if x > y:
    x, y = y, x

while x:
    x, y = y % x, x

print(y)