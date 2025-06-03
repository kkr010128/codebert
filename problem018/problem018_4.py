a = input().split()
b = []
for i in range(len(a)):
    if a[i] == "+":
        b[-2] = b[-2] + b[-1]
        b.pop()
    elif a[i] == "-":
        b[-2] = b[-2] - b[-1]
        b.pop()
    elif a[i] == "*":
        b[-2] = b[-2] * b[-1]
        b.pop()
    else:
        b.append(int(a[i]))
print(b[-1])
