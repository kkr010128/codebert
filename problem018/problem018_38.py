l = input().split()
q = []

for e in l:
    if e == '+':
        q.append(q.pop() + q.pop())
    elif e == '-':
        q.append(-q.pop() + q.pop())
    elif e == '*':
        q.append(q.pop() * q.pop())
    else:
        q.append(int(e))

print(q[0])