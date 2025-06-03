in_l = [a for a in input().split()]
stack = []

while len(in_l) > 0:
    i_e = in_l.pop(0)

    if not i_e in "+-*/":
        stack.append(int(i_e))

    else:
        tmp1 = stack.pop(len(stack)-1)
        tmp2 = stack.pop(len(stack)-1)
        if i_e == '+':
            stack.append(tmp2+tmp1)
        elif i_e == '-':
            stack.append(tmp2-tmp1)
        elif i_e == '*':
            stack.append(tmp2*tmp1)
        elif i_e == '/':
            stack.append(tmp2/tmp1)

print(stack.pop(0))