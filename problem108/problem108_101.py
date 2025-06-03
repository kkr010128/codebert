n = int(input())
x = 0

while True:
    if n % 1000 == 0:
        break
    n += 1
    x += 1

print(x)