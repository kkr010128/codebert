from collections import deque

n = int(input())
dq = deque()
for _ in range(n):
    query = input()
    if query == "deleteFirst":
        dq.popleft()
    elif query == "deleteLast":
        dq.pop()
    else:
        op, arg = query.split()
        if op == "insert":
            dq.appendleft(arg)
        else:
            tmp = deque()
            while dq:
                item = dq.popleft()
                if item == arg:
                    break
                else:
                    tmp.append(item)
            while tmp:
                dq.appendleft(tmp.pop())
print(*dq)

