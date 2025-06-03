inputs = input().split(" ")
stack = []

for str in inputs:
  if str.isdigit():
    stack.append(int(str))
  else:
    b = stack.pop()
    a = stack.pop()
    if str == '+':
      stack.append(a + b)
    elif str == '-':
      stack.append(a - b)
    elif str == '*':
      stack.append(a * b)

print(stack.pop())
