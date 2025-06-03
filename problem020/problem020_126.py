from collections import deque
import sys
n = int(input())
deq = deque()
sub_deq = {}
for cmd in sys.stdin.readlines():
    if cmd == 'deleteFirst\n':
        while deq:
            data = deq.pop()
            if data[1]:
                data[1] = 0
                break
    elif cmd == 'deleteLast\n':
        while deq:
            data = deq.popleft()
            if data[1]:
                data[1] = 0
                break
    else:
        cmd, val = cmd.split()
        if cmd == 'insert':
            data = [val, 1]
            deq.append(data)
            if val not in sub_deq:
                sub_deq[val] = [data]
            else:
                sub_deq[val].append(data)
        elif cmd == 'delete':
            if val in sub_deq:
                deq_v = sub_deq[val]
                while deq_v:
                    data = deq_v.pop()
                    if data[1]:
                        data[1] = 0
                        break
sys.stdout.write(" ".join(data[0] for data in reversed(deq) if data[1]))
sys.stdout.write('\n')