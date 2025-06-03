array = input().split()
stack = []

while True:
    if len(array) == 0: break
    e = array.pop(0)
    if e.isdigit():
        stack.append(e)
    else:
        num1 = stack.pop()
        num2 = stack.pop()
        stack.append(str(eval(num2 + e + num1)))

print(stack[0])