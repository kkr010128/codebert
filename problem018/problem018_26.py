A = raw_input().split()
S = []
for x in A:
    if x in ['+', '-', '*']:
        b = int(S.pop())
        a = int(S.pop())
        if x == '+':
            S.append(a + b)
        elif x == '-':
            S.append(a - b)
        else:
            S.append(a * b)
    else:
        S.append(x)

print S.pop()