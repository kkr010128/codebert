list = input().split(' ')

OPERATOR = {
  '+': lambda a, b: a + b,
  '*': lambda a, b: a * b,
  '-': lambda a, b: a - b,
  '/': lambda a, b: a / b,
}

stack = []
for item in list:
  if item in OPERATOR:
    b = stack.pop()
    a = stack.pop()
    stack.append(OPERATOR[item](a, b))
  else:
    stack.append(int(item))

print(stack.pop())

