top = 0
def push(x):
    global top
    L.append(x)
    top += 1
def pop():
    global top
    x = L.pop(top)
    top -= 1
    return x

L = [0]
S = input().split()
for i in S:
    if i == "+":
        a = pop()
        b = pop()
        push(a + b)
    elif i == "-":
        a = pop()
        b = pop()
        push(b - a)
    elif i == "*":
        a = pop()
        b = pop()
        push(a * b)
    else:
        push(int(i))

print(str(pop()))