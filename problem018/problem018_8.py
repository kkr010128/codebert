arr = input().split()
stack = list()
for el in arr:
    if el.isdigit():
        stack.append(int(el))
        continue
    elif el == "*":
        stack.append(stack.pop() * stack.pop())
        continue
    elif el == "+":
        stack.append(stack.pop() + stack.pop())
        continue
    elif el == "-":
        stack.append(-stack.pop() + stack.pop())
        continue
print(stack.pop())
