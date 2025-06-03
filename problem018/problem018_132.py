from collections import deque as D
line, stack = D(input().split()), D()
while line:
    hoge = line.popleft()
    if hoge.isdigit():
        stack.append(hoge)
    else:
        a, b = int(stack.pop()), int(stack.pop())
        if hoge == "*":
            stack.append(a*b)
        elif hoge == "+":
            stack.append(a+b)
        elif hoge == "-":
            stack.append(b-a)
        else:
            stack.append(b//a)
print(stack.popleft())