S = list(map(str, input().split()))
count = len(S)
stack = []
for i in range(count):
    if S[i] == "+":
        b = stack.pop()
        a = stack.pop()
        stack.append(a + b)
    elif S[i] == "-":
        b = stack.pop()
        a = stack.pop()
        stack.append(a - b)
    elif S[i] == "*":
        b = stack.pop()
        a = stack.pop()
        stack.append(a * b)
    else:
        stack.append(int(S[i]))

print(stack[0])
