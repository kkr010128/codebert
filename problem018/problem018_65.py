import operator

func = {'+':operator.add, '-':operator.sub, '*':operator.mul}

stack  = []
for symbol in input().split():
    if symbol.isdigit():
        stack.append(int(symbol))
    else:
        a = stack.pop()
        b = stack.pop()
        stack.append(func[symbol](b, a))
        
print(stack[0])