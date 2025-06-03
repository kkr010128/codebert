inputs = input().split()
a = int(inputs[0])
b = inputs[1]
b = 100 * int(b[0]) + 10 * int(b[2]) + int(b[3])

print(a * b // 100)