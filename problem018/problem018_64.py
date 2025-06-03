operators = ['+', '-', '*', '/']
stack = list(input().split())
# stack = list(open('input.txt').readline().split())


def calc(ope):
    c = stack.pop()
    a = c if c not in operators else calc(c)
    c = stack.pop()
    b = c if c not in operators else calc(c)
    return str(eval(b+ope+a))

print(calc(stack.pop()))