def calculator(op, x, y):
    if op == '+':
        return x + y
    elif op == '-':
        return y - x
    else:
        return x * y


raw = [r for r in input().split()]
for i in range(len(raw)):
    try:
        raw[i] = int(raw[i])
    except:
        continue

arr = []
buff = 0
for i in range(len(raw)):
    if isinstance(raw[i], int):
        arr.append(raw[i])
    else:
        buff = calculator(raw[i], arr.pop(), arr.pop())
        arr.append(buff)

print(*arr)

