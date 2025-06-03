s = []
F = {
    '+': lambda: s.append(s.pop() + s.pop()),
    '-': lambda: s.append(-s.pop() + s.pop()),
    '*': lambda: s.append(s.pop() * s.pop())
}

for op in input().split():
    if op in F:
        F[op]()
    else:
        s.append(int(op))

print(s.pop())