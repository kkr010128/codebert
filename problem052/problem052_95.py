n = int(input())
x = 1
y = ""
z = 1
while True:
    z = 1
    x += 1
    if x % 3 == 0:
        y += " "
        y += str(x)
    else:
        while True:
            b = int(x % 10 ** (z - 1))
            a = int((x - b) / 10 ** z)
            c = a % 10 ** z
            d = a % 10 ** (z - 1)
            if a == 3 or b == 3 or c == 3 or d == 3:
                y += " "
                y += str(x)
                break
            z += 1
            if a < 3 and z > 3:
                break
    if x >= n:
        break
print(y)
