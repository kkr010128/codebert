x, y = [ int(i) for i in input().split()]

if x > y:
    x, y = y, x

while True:
    if x % y:
        x, y = y, x % y
        continue
    break

print(y)
