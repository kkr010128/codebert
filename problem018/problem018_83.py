arr = list(map(str, input().split()))

i = 0

operand = []

while i < len(arr):
    if arr[i] == '+':
        a = operand.pop(-1)
        b = operand.pop(-1)
        operand.append(b + a)
    elif arr[i] == '-':
        a = operand.pop(-1)
        b = operand.pop(-1)
        operand.append(b - a)
    elif arr[i] == '*':
        a = operand.pop(-1)
        b = operand.pop(-1)
        operand.append(b * a)
    else:
        operand.append(int(arr[i]))
    i += 1

print(operand[0])

