a = list(input().split())
l = []
for c in a:
    if c == '+':
        l.append(l.pop() + l.pop())
    elif c == '-':
        l.append((l.pop() - l.pop()) * -1)
    elif c == '*':
        l.append(l.pop() * l.pop())
    else:
        l.append(int(c))
print(l.pop())