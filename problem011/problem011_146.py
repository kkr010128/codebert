x, y = [int(n) for n in input().split()]
while True:
    tmp = x % y
    if tmp == 0:
        break
    x, y = y, tmp
print(y)