n = int(raw_input())
q = []
bottom = 0
for i in range(n):
    cmd = raw_input()
    if cmd[0] == 'i':
        q.append(cmd[7:])
    elif cmd[6] == ' ':
        try:
            q.pop(~q[::-1].index(cmd[7:]))
        except:
            pass
    elif cmd[6] == 'F':
        q.pop()
    else:
        bottom += 1

print(' '.join(q[bottom:][::-1]))