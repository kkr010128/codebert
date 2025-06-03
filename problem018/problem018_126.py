a = [i for i in input().split()]

b = []
for i in a:
    if i == "+":
        x = int(b.pop())
        y = int(b.pop())
        z = x + y
        b.append(z)
    elif i == "-":
        x = int(b.pop())
        y = int(b.pop())
        z = y - x
        b.append(z)
    elif i == "*":
        x = int(b.pop())
        y = int(b.pop())
        z = x * y
        b.append(z)
    else:
        b.append(int(i))

print(b[0])
