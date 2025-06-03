from collections import deque

times = int(input())
stack = deque()
for i in range(times):
    op = input().split()
    if op[0] == "insert":
        stack.appendleft(op[1])
    if op[0] == "delete":
        if op[1] in stack:
            stack.remove(op[1])
    if op[0] == "deleteFirst":
        stack.popleft()
    if op[0] == "deleteLast":
        stack.pop()
print(*stack)
