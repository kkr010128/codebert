operand = input().split()
stack = []
for op in operand:
    if op.isdigit():
        stack.append(op)
    else:
        val1 = stack.pop()
        val2 = stack.pop()
        stack.append(str(eval("("+val2+")" + op + "("+val1+")")))
print (stack[0])