x, y = map(int, input(). split())
while True:
    if x % y == 0:
        break
    tmp = x % y
    x = y
    y = tmp
print(y)