import re

data = input().split()
stack = []

for elem in data:
    if re.match('\d+', elem):
        stack.append(int(elem))
    else:
        a = stack.pop()
        b = stack.pop()
        if elem == "+":
            stack.append(b+a)
        elif elem == "-":
            stack.append(b-a)
        elif elem == "*":
            stack.append(b*a)

print(stack[0])